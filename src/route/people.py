from flask import flash, redirect, url_for, render_template,request
from app import app,limiter


@app.route('/people/data1/', methods=['GET', 'POST'])
@limiter.limit("20/day")
def getPeopleData1():
    """
    獲取人力 一阶段
    ---
    tags:
        - 人
    responses:
        500:
            description: Error !
        200:
            description: Success!
    """
    return "people data1"

@app.route('/people/data2/', methods=['GET', 'POST'])
def getPeopleData2():
    """
    獲取人力 二阶段
    ---
    tags:
        - 人
    responses:
        500:
            description: Error !
        200:
            description: Success!
    """
    return "people data2"

@app.route('/people/data3/', methods=['GET'])
@limiter.exempt
def getPeopleData3():
    """
    獲取人力 三阶段
    ---
    tags:
        - 人
    responses:
        500:
            description: Error !
        200:
            description: Success!
    """
    return "people data3"

@app.route('/people/data4/', methods=['POST'])
def getPeopleData4():
    """
    獲取人力 四阶段
    ---
    tags:
        - 人
    responses:
        500:
            description: Error !
        200:
            description: Success!
    """
    return "people data4"
