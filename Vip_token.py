#构建请求，获取参数
import requests
import json
#------1、获取令牌token------------
def vip_get_token():
    token_url = 'http://47.96.181.17:9090/rest/toController'
    token_data = {"userName":"J201965943","password":"585855932"}
    headers = {"Content-Type":"application/json"}
    resp = requests.post(token_url,data=json.dumps(token_data),headers=headers)
    token = resp.json()['token']
    return token
#-------获取令牌token*****over-----------
if __name__ == '__main__':
    print(vip_get_token())