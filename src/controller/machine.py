# coding: utf-8
# from app.common.pyOracle import connectToOracle
from src.utils.pyOracle import connectToOracle
# from app.common.flaskApp import app as configApp
import src.config.DBconfig as DBConfig
# from app.common.commFunc import nulToStr
from src.utils.commFunc import nulToStr


class BeolCt2:
    def __init__(self):
        self.db = DBConfig.DB3
        self.conn = connectToOracle(self.db)

    def getCT2Llist(self):
        ct2sql = "SELECT * FROM BEOLCT2_V ORDER BY GRADE"
        ct2 = self.conn.sqlSelect2(ct2sql)
        reslist = []
        for index, row in ct2.iterrows():
            InfoDict = {}
            InfoDict["GRADE"] = nulToStr(row[0])  #等级
            InfoDict["red"] = nulToStr(row[1])  # 红灯数
            InfoDict["green"] = nulToStr(row[2])  # 绿灯数
            reslist.append(InfoDict)

        return reslist

    def getApiPhase2(self, typesname):
        if typesname != 'ALL':
            sql = "select * from api_phase2_v where typesname = '{0}'".format(
                typesname)
        else:
            sql = "select * from api_phase2_v"
        ct2 = self.conn.sqlSelect2(sql)
        reslist = []
        for index, row in ct2.iterrows():
            InfoDict = {}
            InfoDict["EQPID"] = nulToStr(row[1])
            InfoDict["PROD"] = nulToStr(row[2])
            InfoDict["A_INPUT"] = nulToStr(row[3])
            InfoDict["A_QTY"] = nulToStr(row[4])
            InfoDict["A_RATE"] = nulToStr(row[5])
            InfoDict["TOP"] = nulToStr(row[6])
            InfoDict["TYPE1"] = nulToStr(row[7])
            InfoDict["ERROR_QTY"] = nulToStr(row[9])
            InfoDict["RATE"] = nulToStr(row[8])
            InfoDict["OWNER"] = nulToStr(row[10])
            InfoDict["SOLUTION"] = nulToStr(row[11])
            reslist.append(InfoDict)

        return reslist
