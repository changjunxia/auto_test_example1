import requests
r = requests.get('https://home.testing-studio.com/t/topic/1682')
print(r.status_code)
print(r.text)
