## API 开发框架(python-flask版）

环境需求：
python3.7

## Installation

clone:
```
$ git clone http://fsrserver.cminl.oa/data_team/easy-api.git
$ cd easy-api
```
使用python自带的venv模块创建虚拟环境并在虚拟环境中安装项目依耐  
create & activate virtual env then install dependency:

with venv/virtualenv + pip:
```
$ python -m venv env  # use `virtualenv env` for Python2, use `python3 -m venv env` for Python3 on Linux & macOS
$ source env/bin/activate  # use `env\Scripts\activate.bat` on Windows
$ pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

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
