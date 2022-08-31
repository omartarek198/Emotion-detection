from flask import Flask, render_template, request
import base64
from PIL import Image
from io import BytesIO


def encode(path):
    with open(path, "rb") as image_file:
        data = base64.b64encode(image_file.read())

        return data

def decode(data):
    im = Image.open(BytesIO(base64.b64decode(data)))
    im.save('image1.png', 'PNG')

app = Flask(__name__)




@app.route('/')
def hello():
    return render_template("index.html")

@app.route("/sub",methods = ['POST'])
def submit():
    if request.method == "POST":
        name = request.form["username"]


        data = encode(name)
        decode(data)


    return render_template("sub.html", n=data)




if __name__ == "__main__":
    app.run()
