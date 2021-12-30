from app.common.pyOracle import connectToOracle
from app.common.flaskApp import app

# def connectOracleDB():
#     usrName = app.config['DB']['usrName']
#     password = app.config['DB']['password']
#     IP = app.config['DB']['IP']
#     port = app.config['DB']['port']
#     dbName = app.config['DB']['dbName']
#     return connectToOracle(usrName, password, IP, port, dbName)
class connectOracleDB():
    def __init__(self):
        pass
    def getPHARSDB(self):
        self.usrName = app.config['DB']['usrName']
        self.password = app.config['DB']['password']
        self.IP = app.config['DB']['IP']
        self.port = app.config['DB']['port']
        self.dbName = app.config['DB']['dbName']

    def getPHBLRDB(self):
        self.usrName = app.config['PHBLR_DB']['usrName']
        self.password = app.config['PHBLR_DB']['password']
        self.IP = app.config['PHBLR_DB']['IP']
        self.port = app.config['PHBLR_DB']['port']
        self.dbName = app.config['PHBLR_DB']['dbName']

def connectOracleDB():
    usrName = app.config['DB']['usrName']
    password = app.config['DB']['password']
    IP = app.config['DB']['IP']
    port = app.config['DB']['port']
    dbName = app.config['DB']['dbName']
    return connectToOracle(usrName, password, IP, port, dbName)