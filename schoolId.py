from email import header
from tokenize import endpats
from wsgiref import headers
import requests
import json

def GetSchoolId(num):
    url = "https://www.patest.cn/api/teams/visible"
    myheaders = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55",
        "Host": "www.patest.cn",
        "Connection": "keep-alive",
        "sec-ch-ua": "' Not A;Brand';v='99', 'Chromium';v='99', 'Microsoft Edge';v='99'",
        "Accept": "application/json; q=1.0, text/*; q=0.8, */*; q=0.1",
        "Cache-Control": "no-cache",
        "sec-ch-ua-mobile": "?0",
        "X-Exam-Type-Id": "1359419395582308352",
        "sec-ch-ua-platform": "'Windows'",
        "Origin": "https://gplt.patest.cn",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://gplt.patest.cn/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
    }
    myfiles = {
        "filter": (None, "{\"examGroupId\":\"1461599053841653760\",\"keyword\":\"\"}"),
        "page": (None, num),  #设置页面
        "limit": (None, '50'),
        "asc": (None, 'true')
    }
    alljson = requests.get(url, headers = myheaders, files = myfiles)
    myjson = alljson.json()
    teamslist = myjson.get("teams")
    schoolIdList = set([])
    for i in teamslist: schoolIdList.add(i['schoolId'])
    # for i in schoolIdList: print('"' + i + '",', end = "")
    # print(len(schoolIdList))

    schoolStr = ''
    for i in iter(schoolIdList):
        schoolStr += '"' + i + '",'
    schoolStr=schoolStr[:-1]    #去除最后一个字符,
    # print(schoolStr)
    return schoolStr