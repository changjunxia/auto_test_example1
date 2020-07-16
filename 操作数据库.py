import MySQLdb
 #查询数据库
conn = MySQLdb.connect(
    host='192.168.1.104',
    user='songqin',
    passwd='songqin',
    db='plesson',
    charset='utf8'
)
#cursor 创建游标对象,目的通过对象发送sql语句
c = conn.cursor()
#执行sql语句
c.execute('select * from sql_course')
for i in range(c.rowcount):
    row = c.fechone()
    #添加的课程是否在数据库里面
    if row[1]=='Python':
        print('检查点=> Python课程找到，通过')
        break