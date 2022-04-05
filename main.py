from flask import Flask, render_template, redirect, url_for, flash, request
import os
import numpy as np
from PIL import Image

UPLOAD_FOLDER = './static/image'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/',  methods=['GET', 'POST'])
def home():
    img_path = "./static/image\Image Color Extract.jpg"
    if request.method == 'POST':
        if 'image_file' not in request.files:
            return 'there is no file1 in form!'
        file1 = request.files['image_file']
        path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
        file1.save(path)
        img_path = path
    my_img = Image.open(img_path)
    img_array = np.array(my_img)
    colors = img_array
    hexalist = []
    def rgb_to_hex(rgb):
        hexacode = '%02x%02x%02x' % rgb
        if hexacode not in hexalist:
                hexalist.append(hexacode)

    for color in colors:

        tuple(color[1])
        rgb_to_hex(tuple(color[1]))
    # print(hexalist)

    return render_template("home.html",img=img_path, codes=hexalist)


if __name__ == "__main__":
    app.run(debug=True)