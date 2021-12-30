from flask import flash, redirect, url_for, render_template
from app import app


@app.route('/material/data1/', methods=['GET', 'POST'])
def getMaterialData1():
    """
    獲取物料 一阶数据
    ---
    tags:
        - 料
    responses:
        500:
            description: Error !
        200:
            description: Success!
    """
    return "material data1"

@app.route('/material/data2/', methods=['GET', 'POST'])
def getMaterialData2():
    """
    獲取物料 二阶段
    ---
    tags:
        - 料
    responses:
        500:
            description: Error !
        200:
            description: Success!
    """
    return "material data2"