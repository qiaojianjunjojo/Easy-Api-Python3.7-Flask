from src.utils.pyOracle import connectToOracle
import pandas as pd


# 將None 轉化為0
def nulToZero(arg):
    if arg == None or pd.isnull(arg):
        arg = 0
    return arg
# 將None 轉化為空
def nulToStr(arg):
    if arg == None or pd.isnull(arg):
        arg=''
    return arg

# columnNameList顯示的欄位名稱，順序要與sql 中的欄位順序對應
def toList(data, columnNameList):
    subContentList = []
    for index,row in data.iterrows():
        subContentDict = {}
        i = 0
        for i in range(data.columns.size):
            subContentDict[columnNameList[i]] = nulToStr(row[i])
        subContentList.append(subContentDict)
        # print(subContentList)
    return subContentList

def toDict(data):
    subContentDict = {}
    for index,row in data.iterrows():
        subContentDict[row[1]] = nulToStr(row[2])
        # print(subContentList)
    return subContentDict