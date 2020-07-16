import xlrd  #读取excel
from xlutils import copy  #复制excel用例
from vip_addUser import vip_add_user
from Vip_token import vip_get_token
import json
#1、读取excel测试用例
excelDir = r'C:\Users\xintian\desktop\松勤VIP接口测试用例-自动化-v4.0.xls'#xlsx另存为xls
#1-1 打开excel表
workbook = xlrd.open_workbook(excelDir,formatting_info=True)
workbooknew = copy(workbook)
worksheetnew = workbooknew.get_sheet(1)
worksheet = workbooknew.sheet_by_name('新增客户61个')

#print(cellData)
#print(cellExp)
#1-获取token
token = vip_get_token()

#4、自动化执行测试用例
for one in range(1,10):
    # 读取指定单元格
    cellData = worksheet.cell(one, 6).value  # 行，列---请求参数
    cellExp = json.loads(worksheet.cell(one, 8).value)  # ----预期结果
    idNum = worksheet.cell(one, 0).value
    # 2-新增用户
    res = vip_add_user(cellData, token, True)["message"]
    # 3、跟预期数据匹配
    if res == cellExp["message"]:
        print('f{idNum}--->测试用例----成功')
        excel_res = 'pass'
    else:
        print('f{idNum}--->测试用例----失败')
        excel_res = 'fail'
#5-测试结果写入测试用例里面去
worksheetnew.write(one,9,json.dumps(res))
worksheetnew.write(one,10,excel_res)
#6-保存
worksheetnew.save(r'C:\users\xintian\DeskTop\松勤VIP接口测试用例-res-v1.5.xls')

#结合unittest框架  ddt数据驱动  测试报告：htmltestrunner   邮件功能