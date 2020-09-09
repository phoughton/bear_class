# bear_class

A simple example bear classifier using colab to create the model and flask to enable a web app.


### Quick install using pip & requirements.txt (recommended)
Create a virtual environment and type this pip command at the command line. (It's a big install and may take a few minutes.)
```bash
pip install -r requirements.txt
```


### Manual setup (not recommended)
Create a virtual environment and manually install each of these (in this order)
```bash
pip install torch===1.6.0 torchvision===0.7.0 -f https://download.pytorch.org/whl/torch_stable.html

pip install fastai
pip install flask
pip install pillow
pip install ipython
```


### Running the app
The below commands will run the server and will output a URL you can use to access it.

Windows:
```bash
set FLASK_APP=views
flask run
```

Linux/Unix/Mac/Bash:
```bash
export FLASK_APP=views
flask run
```
