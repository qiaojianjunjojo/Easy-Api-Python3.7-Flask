## API 开发框架(python-flask版）

环境需求：
python3.7

## Installation

clone:
```
$ git clone https://github.com/qiaojianjunjojo/python3-flask-api-project.git
$ cd python3-flask-api-project
```
使用python自带的venv模块创建虚拟环境并在虚拟环境中安装项目依耐  
create & activate virtual env then install dependency:

with venv/virtualenv + pip:
```
1.创建虚拟环境 windows: python -m venv env || Python3 on Linux & macOS : python3 -m venv env
2.激活虚拟环境 windosw: env\Scripts\activate.bat || Python3 on Linux & macOS : source env/bin/activate 
3.安装项目依耐 pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

```
运行
```
$ flask run 
* Running on http://127.0.0.1:5000/

或者
vscode選中app.py 按F5 開啟斷點調試模式.
```

## 服务器部署
nginx + uwsgi + flask进行部署  


## License

This project is licensed under the MIT License 
