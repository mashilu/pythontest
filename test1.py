import cx_Oracle

db = cx_Oracle.connect('iot_app', 'iot_app', '192.168.205.20:1521/fxpt')

cursor = db.cursor()

sql = """select msisdn
from cm_subs_subscriber s
where s.eccustid = '100015632100100000'"""

cursor.execute(sql)
result = ''

for i in range(1, 200):
    row = cursor.fetchone()
    if row == None:
        break
    else:
        result += row[0]
        result += '_'
        
print("%s" % result)


