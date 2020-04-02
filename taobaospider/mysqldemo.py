import pymysql
import sys
# python mysql 创建库、表增删改查标准语句
print('----------------------------')
print('载入mysql模块完成')
con = pymysql.connect(host='localhost', user='root',
                      passwd='123456', charset='utf8')
# con = pymysql.connect(host='localhost', user='root',
# passwd='123456', db='test_db',  charset='utf8') # 直接连入db1库
print('创建连接完成')
cur = con.cursor()
print('获取光标完成')
cur.execute("create database taobao character set utf8;")
print('创建taobao库完成')
cur.execute("use taobao;")
print('进入taobao库完成')
sql = """CREATE TABLE taobao_food (
         shop  CHAR(20),
          title  CHAR(40),
          price  CHAR(20),
          place  CHAR(20),
          buy_num  CHAR(20))"""
cur.execute(sql)
print('创建taobao_food表完成')

#关闭数据库
cur.close()

# count = 0
# while True:
#     sql_insert = 'insert into test_tab(id,name) values(%s,%s);'
#     ID = input('请输入id：')
#     if not ID:
#         break
#     name = input('请输入名字：')
#     try:
#         cur.execute(sql_insert, [int(ID), name])
#         count += 1
#         con.commit()
#         print('添加第%d条记录' % count, int(ID), name)
#     except Exception as e:
#         print('出错回滚完成', e)
#         con.rollback()
#         cur.close()
#         con.close()
#         sys.exit()
# del count
# print('sql写入语句执行完成')
# sql_select = 'select * from test_tab;'
# sql_delete = 'delete from test_tab where id=4;'
# sql_update = 'update table set name ="大胖" where id=3;'
# print('创建sql语句完成')
# try:
#     cur.execute(sql_select)
#     print('sql查询语句执行完成')
#     data_one = cur.fetchone()
#     print(data_one)
#     print('已显示第一条记录')
#     data_many = cur.fetchmany(2)
#     print(data_many)
#     print('已显示后面两条记录')
#     data_all = cur.fetchall()
#     print(data_all)
#     print('已显示后面全部记录')
#     cur.execute(sql_delete)
#     print('sql删除语句执行完成')
#     cur.execute(sql_update)
#     print('sql更新语句执行完成')
#     con.commit()
#     print('sql写入完成')
# except Exception as e:
#     print('出错回滚完成', e)
#     con.rollback()
# cur.close()
# print('关闭光标完成')
# con.close()
# print('关闭连接完成')
# print('程序结束')
# print('----------------------------')