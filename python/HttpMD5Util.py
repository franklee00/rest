#!/usr/bin/python
# -*- coding: utf-8 -*-
#用于进行http请求，以及MD5加密，生成签名的工具类

import http.client#本行是Python3写法，如您使用Python3则无问题。如您使用Python2.7，则应修改为 import httplib .以下语句还有3出修改，分别在第20行，第31行和第33行
import urllib
import json
import hashlib
import time

def buildMySign(params,secretKey):
    sign = ''
    for key in sorted(params.keys()):
        sign += key + '=' + str(params[key]) +'&'
    data = sign+'secret_key='+secretKey
    return  hashlib.md5(data.encode("utf8")).hexdigest().upper()

def httpGet(url,resource,params=''):
    #以下行为Python3写法，如使用Python2.7，则改为 conn = httplib.HTTPSConnection(url, timeout=10)
    conn = http.client.HTTPSConnection(url, timeout=10)
    conn.request("GET",resource + '?' + params)
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    return json.loads(data)

def httpPost(url,resource,params):
     headers = {
            "Content-type" : "application/x-www-form-urlencoded",
     }
     #以下行为Python3写法，如使用Python2.7，则改为 conn = httplib.HTTPSConnection(url, timeout=10)
     conn = http.client.HTTPSConnection(url, timeout=10)
     #以下行为Python3写法，如使用Python2.7，则改为 temp_params = urllib.urlencode(params)
     temp_params = urllib.parse.urlencode(params)
     conn.request("POST", resource, temp_params, headers)
     response = conn.getresponse()
     data = response.read().decode('utf-8')
     params.clear()
     conn.close()
     return data


        
     
