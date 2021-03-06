from flask import Flask
from flask import request, redirect, render_template
from fastai.learner import load_learner
import pathlib
from fastai.vision.core import PILImage
import platform


application = Flask(__name__)
application.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024


# Workaround pytorch issue with models developed on linux being used on Windows
if platform.system() == 'Windows':
    pathlib.PosixPath = pathlib.WindowsPath

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

learn_inf = load_learner('export.pkl', cpu=True)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@application.route("/upload-image/", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            if allowed_file(image.filename):
                pred, pred_idx, probs = learn_inf.predict(PILImage.create(image))
                return render_template("public/upload_image.html", messages=f"Prediction: {pred}; Probability: {probs[pred_idx]:.04f}")
            else:
                return render_template("public/upload_image.html", messages=f"Sorry, invalid image type: Must be a: {ALLOWED_EXTENSIONS}")

    return render_template("public/upload_image.html", messages="")


@application.route('/')
def go_to_upload():
    return redirect("upload-image/")


if __name__ == '__main__':
    application.run()
