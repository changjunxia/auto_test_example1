from selenium import webdriver #导入webdriver模块
import xlwt

driver = webdriver.Chrome(r"D:\chromedriver.exe")#webdriver实例对象   浏览器的遥控器
driver.implicitly_wait(10)
driver.get('http://www.51job.com')
fromEle = driver.find_element_by_id('kwdselectid')
fromEle.send_keys('python')
driver.find_element_by_id('work_position_input').click()

import time
time.sleep(1)

selectedCityEles = driver.find_elements_by_css_selector(
'#work_position_click_center_right_list_000000 em[class=on]'
)
for one in selectedCityEles:
    one.click()
#选择杭州
driver.find_element_by_id('work_position_click_center_right_list_category_000000_080200').click()

#保存城市选择
driver.find_element_by_id('work_position_click_bottom_save').click()

#点击搜索
driver.find_elements_by_css_selector('.ush button').click()

#搜索结果分析
jobs = driver.find_elements_by_css_selector('#resultList div[class=el]')

#创建一个excel workbook对象：
book = xlwt.Workbook()

#增加一个sheet
sh = book.add_sheet('统计')

#写入内容
row = 0
for job in jobs:
    fields = job.find_elements_by_tag_name('span')
    col = 0
    for field in fields:
        text=field.text
        print(text,end='')
        sh.write(row,col,text)
        col += 1
    print('')
    row += 1

#保存文件
book.save('d:\51job.xls')

driver.quit()