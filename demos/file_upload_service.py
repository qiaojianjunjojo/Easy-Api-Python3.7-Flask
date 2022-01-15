import os,sys
from flask import Flask,  request, redirect, url_for,render_template,send_from_directory
from werkzeug.utils import secure_filename
from flask_cors import CORS


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','xls','xlsx','pptx','docs'}

app = Flask(__name__)
CORS(app)

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

#尺寸限制为 100 M 。如果上传了大于这个尺寸的文件， Flask 会抛 出一个 RequestEntityTooLarge 异常。
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024 

# 函数 检查扩展名是否合法
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class SystemNotFoundException(Exception):
    pass

class FileNotFoundException(Exception):
    pass

class NotAllowedFileTypeException(Exception):
    pass

#展示 某个 系統下 所有的file list
@app.route('/getFileList',methods = ['GET'])
def get_filelist():
    try:
        sysid = request.args.get('SYSID',None)
        if not sysid:
            return {"filelist" :[]}
        path = os.path.join(BASE_PATH,'upload',sysid)
        return {"filelist" :os.listdir(path)}
    except:
        return {"filelist" :[]}


@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        sysid = request.form.get("SYSID",None)
        if sysid:
            # file = request.files['file']
            if len(request.files):
                for f in request.files.getlist('file'):
                    if not allowed_file(f.filename):
                        raise NotAllowedFileTypeException("暂不支持此类型文件上传:{0}".format(f.filename))
                if not os.path.exists(os.path.join(BASE_PATH, "upload",sysid)):
                    os.makedirs(os.path.join(BASE_PATH, "upload",sysid))
                for f in request.files.getlist('file'):
                    filename = os.path.join(BASE_PATH, "upload",sysid, f.filename)
                    print(filename)
                    f.save(filename)
                return "上传成功!"
            else:
                raise FileNotFoundException("未发现上传文件!")
        else:
            raise SystemNotFoundException("非法的SYSID!")
    except Exception as e:
        return "文件上传失败," + str(e)

# 
# 
@app.route("/download", methods=["GET"])
def download_file():
    try:
        sysid = request.args.get('SYSID',None)
        filename = request.args.get('Filename',None)
        if not sysid or not filename:
            raise SystemNotFoundException("非法的SYSID!")
        if not os.path.exists(os.path.join(BASE_PATH, 'upload' , sysid,filename)):
            raise FileNotFoundException("文件不存在!")
        dir = os.path.join(BASE_PATH, 'upload',sysid)
        print(dir)
        return send_from_directory(dir, filename, as_attachment=True)
    except Exception as e:
        return "文件下载失败," + str(e) 

def mkdir(dirname):
    dir = os.path.join(BASE_PATH, dirname)
    if not os.path.exists(dir):
        os.makedirs(dir)


if __name__ =="__main__":
    mkdir('upload')
    app.run()



