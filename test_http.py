import requests
class TestHttp:
    def test_get(self):
        r = requests.get('https://home.testing-studio.com/t/topic/1682')
        print(r.status_code)
        print(r.text)
        assert r.status_code == 200

    def test_query(self):
        r = requests.get(
            'https://home.testing-studio.com/search',
            params={'q':'requests'}
        )
        print(r.text)
        assert r.status_code == 200

    def test_form(self):      v
    def test_json(self):
        r = requests.get(
            'https://home.testing-studio.com/categories.json',
            #json={}
        )
        print(r.json())
        assert r.status_code == 200
        assert r.json()['category_list']['categories'][0]['name']=='霍格沃兹测试学院公众号'