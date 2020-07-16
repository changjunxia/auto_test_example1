import requests
class Wework:
    token=""

    def get_token(cls):
        r = requests.get(
            'http://qyapi.weixin.qq.com/cgi-bin/gettoken',
            params={
                'corpid': 'ww6da61649bd66fea',
                'corpsecret': 'heLiPlmyblHRikAgGWZky-KdWqulV22Fex8RfM0'
            }
        )
        print(r.json())

        cls.token = r.json()['access_token']
        return r