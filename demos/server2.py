import os
from flask import Flask, flash, request, redirect, url_for,render_template,send_from_directory
from werkzeug.utils import secure_filename

# UPLOAD_FOLDER 替换成你server存储的路径
UPLOAD_FOLDER = r'C:\Users\Administrator\Desktop\flask api\downloads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#尺寸限制为 16 M 。如果上传了大于这个尺寸的文件， Flask 会抛 出一个 RequestEntityTooLarge 异常。
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# 函数 检查扩展名是否合法
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/<name>")
def hello(name):
    return f"Hello, {name}!"

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # print(url_for('download_file', name=filename,version = 1))
            return redirect(url_for('download_file', name=filename))
    return render_template('upload.html')


@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name,as_attachment = False)



if __name__ =="__main__":
    app.run()