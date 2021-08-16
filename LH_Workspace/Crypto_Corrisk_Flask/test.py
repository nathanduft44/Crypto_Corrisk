from flask import Flask, render_template
import os

picfolder = os.path.join('static', 'pics')

app = Flask(__name__, template_folder="template")

app.config['UPLOAD_FOLDER'] = picfolder


@app.route('/')
def index():
    image = os.path.join(app.config['UPLOAD_FOLDER'], 'image.PNG')
    return render_template("index.html", user_image = image)

@app.route("/index")
def index1():
    return "Hello Corrisk!"

if __name__ == '__main__':
    app.run()