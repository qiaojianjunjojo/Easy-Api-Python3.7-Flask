from flask import Flask,redirect,url_for
from flask_cors import CORS
from flasgger import Swagger
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
CORS(app)  #跨域问题
Swagger(app)  #api 文档生成工具swagger
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["1000/day","100/hour",],
    storage_uri="redis://10.189.127.62:40118/0"
)


app.config['JSON_SORT_KEYS'] = False  #返回json格式時，取消自動按照字母排序

from src.route import people,machine,material #路由与endpoint注册

# 從 '/' 导航到 swagger页面
@app.route('/')
def toSwagger():
    return redirect(url_for('flasgger.apidocs'))

if __name__ == "__main__":
    app.run()
    