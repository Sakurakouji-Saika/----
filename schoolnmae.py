import requests
import json

def GetName(Str):
    url = 'https://www.patest.cn/api/schools'

    jsonbegins = '{"examTypeId":"1359419395582308352","schoolIds":['
    jsonends = ']}'

    startStr = jsonbegins + Str + jsonends
    startStrlen = len(startStr)

    postheader ={
        "accept":"application/json; q=1.0, text/*; q=0.8, */*; q=0.1",
        "accept-encoding":"gzip, deflate, br",
        "accept-language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "content-length":str(startStrlen),
        "content-type":"application/json"
    }

    mypost = requests.post(url,headers=postheader,data=startStr)
    alljson = mypost.json()
    bodyjson = alljson.get("schools")
    schoolNameList = set([])
    for i in bodyjson: schoolNameList.add(i['name'])
    return schoolNameList