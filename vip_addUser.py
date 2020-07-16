import requests

import json
from random import randint
from Vip_token import vip_get_token
#--------2、新增用户请求-------------
def vip_add_user(inData,inToken,inTelState=True):
    addUser_url = 'http://47.94.121.12:9090/rest/ac01crmcontroller'
    addUser_data = json.load(inData)#请求参数转化为字典
    if inTelState:
        tel_num = '13'+str(randint(100000000,999999999))
        addUser_data['aac0030']=tel_num
    addUser_headers = {"Content_Type":"application/json","X-AUTH-TOKEN":inToken}
    addUser_resp = requests.post(addUser_url,data=json.dumps(addUser_data),headers=addUser_headers)
    res = addUser_resp.json()
    return res
#--------2.用户请求over----------
if __name__ == '__main__':
    token = vip_get_token()
    data = '''{
    "aac003":"张三","aac030":"13533456732",
    "crm003":"1",
    "crm004":"1"
    }'''
    print(vip_add_user(data,token,True))