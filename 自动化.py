import requests
from pprint import pprint
#先列出课程
res = requests.get('https://ke.qq.com/course/list/%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95')
list1 =res.json()['retlist']
#添加课程
res1 = requests.post('http://localhost/api/mgr/sq_mgr/',
              data={
                  'action':'add_course',
                  'data':'''{
  "name":"初中化学",
  "desc":"初中化学课程",
  "display_idx":"4"
}
'''

      })
retObj = res1.json()
pprint(retObj,width=30)

if retObj['retcode']==0:
    print('检查点==> 返回结果retcode为0，检查通过')
else:
    print('检查点==> 返回结果retcode不为0，检查不通过')
#列出课程
res = requests.get('https://ke.qq.com/course/list/%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95')
list2 = res.json()['retlist']
# if res.status_code==200:
#     print('检查点通过')
# else:
#     print('检查点不通过')
#取出、多出来的一门课程对象
newcourse = None
for one in list2:
    if one not in list1:
        newcourse = one
       break
#检查是否刚刚添加的课程
assert newcourse!=None
assert newcourse['name']=='猴哥3'
assert newcourse['desc']=='猴哥课程'
assert newcourse['display_idx']==4

print('\n========test case pass==========')