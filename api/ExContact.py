import json

import requests

from api.Wework import Wework


class ExContact:
    def list(self,userid):
        r = requests.get(
            'http://qyapi.weixin.qq.com/cgi-bin/externalcontact/list',
            params={
                'access_token': Wework.token,
                'userid': userid
            }
        )
        self.format(r)
        return r

    def get(self,ex_uid):
        r = requests.get(
            'http://qyapi.weixin.qq.com/cgi-bin/externalcontact/get',
            params={
                'access_token': Wework.token,
                'external_userid': ex_uid
            }
        )
        self.format(r)
        return r

    def remark(self,uid,ex_uid, remark):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/remark',
             params={'access_token':Wework.token},
            json={
                'userid':uid,
                'external_userid':ex_uid,
                'remark':remark
            }
        )
        self.format(r)
        return r

    def format(self, r):
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))