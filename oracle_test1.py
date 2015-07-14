import cx_Oracle

db = cx_Oracle.connect('iot_app', 'iot_app', '192.168.200.20:1521/fxpt')

cursor = db.cursor()

stats_subs_simflowday_old_sql = """
select sf.msisdn, sf.smstotal, sf.smsusedflow, sf.gprstotal, sf.gprsusedflow,
sf.voicetotal, sf.voiceusedflow, sf.gprsyesterdayflow, sf.smsyesterdayflow, sf.statsdate
from stats_subs_simflowday_430 sf, cm_subs_subscriber s
where sf.msisdn = s.msisdn and s.provinceid = 
"""

def getResult(db_cursor, file_name, sql):
    db_cursor.execute(sql)
    file_object = open(file_name, 'w')
    while(1):
        row = db_cursor.fetchone()
        if row == None:
            break
        else:
            file_object.write("%s %s %s %s %s %s %s %s %s %s\n" % 
                              (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
    file_object.close()

# stats_subs_simflowday old 100
stats_subs_simflowday_old_100_file_name = 'stats_subs_simflowday_old_100.txt'
stats_subs_simflowday_old_100_sql = stats_subs_simflowday_old_sql + '100'

# stats_subs_simflowday old 200
stats_subs_simflowday_old_200_file_name = 'stats_subs_simflowday_old_200.txt'
stats_subs_simflowday_old_200_sql = stats_subs_simflowday_old_sql + '200'

# stats_subs_simflowday old 591
stats_subs_simflowday_old_591_file_name = 'stats_subs_simflowday_old_591.txt'
stats_subs_simflowday_old_591_sql = stats_subs_simflowday_old_sql + '591'

# stats_subs_simflowday old 371
stats_subs_simflowday_old_371_file_name = 'stats_subs_simflowday_old_371.txt'
stats_subs_simflowday_old_371_sql = stats_subs_simflowday_old_sql + '371'

getResult(cursor, stats_subs_simflowday_old_591_file_name, stats_subs_simflowday_old_591_sql)
