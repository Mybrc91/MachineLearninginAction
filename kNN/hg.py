# -*- coding:utf-8 -*-

import urllib.request
import urllib.parse
import csv
import json

def start():
    u = "http://server.huayibao.cc/app/customer/getCustomerById"
    values = {'deviceId': '55487d3ac554b5a4', 'serviceVersion': 'V4.0', 'deviceType': '1', 'deviceInfo': 'ANDROID', 'appVersion': '2.1.6'}
    with open('info.csv','w',newline='') as cvsf:
        writer = csv.DictWriter(cvsf ,fieldnames=['phone','companyTypeName','uncompanyId','companyName','salesCount','balance','customerId','realName','companyId','telephone'])
        writer.writeheader()
        for i in range(1000):
            values["customerId"]=i
            try:
                print('抓取中No:',i)
                data = urllib.parse.urlencode(values).encode("ascii")
                with urllib.request.urlopen(u ,data) as f:
                    response = f.read().decode('utf-8')
                    jsonstr = json.loads(response)['customer']
                    csvvalue = {'phone':jsonstr['phone'],'companyTypeName':jsonstr['companyTypeName'],'uncompanyId':jsonstr['uncompanyId'],'companyName':jsonstr['companyName'],'salesCount':jsonstr['salesCount'],'balance':jsonstr['balance'],'customerId':jsonstr['customerId'],'realName':jsonstr['realName'],'companyId':jsonstr['companyId'],'telephone':jsonstr['telephone']}
            except Exception as e:
                #raise
                print('出错了No',i)
                pass
            else:
                if csvvalue['phone']!='' and csvvalue['companyName']!='':
                    writer.writerow(csvvalue)
                #print(response)
