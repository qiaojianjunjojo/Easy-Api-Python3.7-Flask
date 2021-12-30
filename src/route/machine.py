from flask import flash, redirect, url_for, render_template, jsonify, request, Response
from app import app
from src.controller.machine import BeolCt2


@app.route('/machine/data1/', methods=['GET', 'POST'])
def getMachineData1():
    """
    獲取机 一阶数据
    ---
    tags:
        - 机
    responses:
        500:
            description: Error !
        200:
            description: Success!
    """
    obj = BeolCt2()
    data = obj.getCT2Llist()
    return jsonify({"code": 200, "message": "OK", "data": data})


@app.route('/machine/data2/', methods=['GET', 'POST'])
def getMachineData2():
    """
    獲取机 二阶数据
    ---
    tags:
        - 机
    responses:
        500:
            description: Error !
        200:
            description: Success!
    """
    return "machine data2"
