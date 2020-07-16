import pytest
import requests

from api.Wework import Wework

from api.ExContact import ExContact


class TestWork:
    @classmethod
    def setup_class(cls):
       cls.Wework = Wework()
       cls.wework.get_token()

       cls.excontact=ExContact()

    def test_get_token(self):
        r = Wework.get_token()
        print(r.json())
        assert r.status_code == 200

        token=r.json()['access_token']

        def test_list(self):
            r = self.excontact.list('sihan')
            assert r.status_code == 200
            assert len(r.json()['external_userid']) > 43
            print(r.json)
            uid = r.json()['external_userid'][0]

            r = self.excontact.get(uid)
            print(r.json())
            assert r.status_code == 200

        @pytest.mark.parametrize("uid,remark",[
            ("sihan","阔小阔 童书加盟 备注测试"),
            ("sihan","demo"),
            ("sihan","1"),
            ("sihan",""),
            ("sihan","_")
        ])
        def test_remark(self,uid,remark):
            r = self.excontact.list(uid)
            ex_uid = r.json()['external_userid'][0]
            self.excontact.remark(uid,ex_uid,remark)
            r=self.excontact.get(ex_uid)
            assert r.json()['follow_user'][0]['remark']==remark
