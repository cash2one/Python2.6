# -*- coding: cp936-*-
import MySQLdb
import datetime
import urllib
import re
from datetime import datetime,timedelta


# ����һ������
Con = MySQLdb.connect(host="192.168.116.20", port=3380,   user= "lixueshi", passwd= "i14p4Dkyd", db= "house_report")
# ����һ��cursor, ����ִ��sql���
Cursor = Con.cursor( )

def init():
    # ����һ������
    global Cursor,companylist,hzyfdic
    
    #ÿ����� ��ʱ�ļ���
    sql = 'DELETE FROM koubeitemp'
    #print sql
    Cursor.execute(sql)
    
    #ÿ������յ���Ŀڱ�,Ȼ��������¼���¿ڱ�
    sql = 'DELETE FROM koubei where date="'+str(datetime.today())[:10]+'"'
    Cursor.execute(sql)
    
    
    #��wrapper�ŵ��б���
    sql = 'SELECT DISTINCT(company) FROM wrapperCompany'
    #print sql
    Cursor.execute(sql)
    Results = Cursor.fetchall( )
    
    for r in Results:
        m = r[0].decode('utf-8').encode('cp936')
        companylist.append(m)
        
    #��wrapper�ŵ��б���
    sql = 'SELECT * FROM koubei_hzyf'
    #INSERT INTO koubei_hzyf (company,months) VALUES ('��̩����',13)
    #sql = 'insert into koubei_hzyf (company,months) VALUES ("��̩����",12)'
    #print sql
    Cursor.execute(sql)
    Results = Cursor.fetchall( )

    for r in Results:
        m = r[0].decode('utf-8').encode('cp936')
        #print m,r[1]
        hzyfdic[m] = r[1]



    

                                    
def main():
    global Cursor
    
    sql = "SELECT * FROM house_company_report_2012_07 LIMIT 10;"
    Cursor.execute(sql)

    # Fetch all results from the cursor into a sequence and close the connection
    # ȡ�÷��ص�ֵ���ر�����
    Results = Cursor.fetchall( )
    
    for r in Results:
        print r
    

if __name__ == '__main__':
    main()
    

