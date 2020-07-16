import MySQLdb
conn = MySQLdb.connect(
    host='192.168.1.104',
    user='songqin',
    passwd='songqin',
    db='plesson',
    charset='utf8'
)
#        cursor 创建游标对象,目的通过对象发送sql语句
c = conn.cursor()
for x in range(1000):
     #执行sql语句,f是字符串格式化的写法
     c.execute(xf"insert into sq_course(name,'desc',display_idx)
          values ('测试课程{x+1}','课程测试',6)")
conn.commit()
conn.close()