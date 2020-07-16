#更新和插入一样，只是语句不一样
import MySQLdb
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
c.execute("insert into sq_course(name,'desc',display_idx)
          values ('哈哈2','sddff',6)")
conn.commit()
conn.close()

