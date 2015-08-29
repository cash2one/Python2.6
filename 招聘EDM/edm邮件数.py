# coding: gbk
import os,MySQLdb,time
t= time.time()
dateNow = time.strftime('%Y-%m-%d',time.localtime(time.time()))
#data = open('C:\\Users\\suchao\\Desktop\\phone_20121108\\fufei_zhongjie_short_20121108.log').readlines()
geren = open('geren.txt','w')
jjr = open('jjr.txt','w')

def getSql(category,type):
    if type == 'other':
        if category == 'zp':
            #sql = 'SELECT COUNT(1) FROM findjob_post WHERE listing_status >= 5 AND findjob_period > 1 AND show_time >=unix_timestamp("2013-04-01") AND email != "" AND show_before_audit_reason LIKE "%���ip%";'
            sql = 'SELECT COUNT(1) FROM findjob_post WHERE listing_status >= 5 AND findjob_period > 1 AND refresh_at >= UNIX_TIMESTAMP("2013-6-25") AND email != "" ;'
        else:
            return '������'
    elif type == 'yjs':
        if category == 'zp':
            #sql = 'SELECT COUNT(1) FROM findjob_post WHERE listing_status >= 5 AND findjob_period = 1 AND show_time >=unix_timestamp("2013-04-01") AND email != "";'
            sql = 'SELECT COUNT(1) FROM findjob_post WHERE listing_status >= 5 AND findjob_period = 1 AND refresh_at >= UNIX_TIMESTAMP("2013-6-25") AND email != "" ;'
        else:
            return '������'
    else:
        return "����������󣡴��룺������ڣ���������ݣ�yjs����other"
    return sql

#���ж�Ӧ��ϵ��ͳ��
categorys=['zp']

citys={}

conn=MySQLdb.connect(host="192.168.116.20",user="yangyu",passwd="c1b78739d",port=3311,db="management",charset="gbk")
cursor = conn.cursor()
cursor.execute('SELECT domain,pinyin FROM city;')
for row in cursor.fetchall():
    citys[row[0]]=row[1]
cursor.close()
citys['others']='others'

#�����������ֵ�ͳ��
t = 0
for domain in citys:
    city = citys[domain]
    try:
        conn=MySQLdb.connect(host="192.168.116.20",user="yangyu",passwd="c1b78739d",port=3310,db=city,charset="gbk")
    except:
        continue
    try:
        print city
        cursor=conn.cursor()
        for category in categorys:
            #print category
            sqlGeren = getSql(category,"yjs")
            sqlJjr = getSql(category,"other")
            #print sqlJjr
            #print sqlGeren
            cursor.execute(sqlGeren)
            for row in cursor.fetchall():
                #resultClickGeren.write(houseId+'\t'+houseIdClick[houseId])
                geren.write(category+'\t'+city+'\t'+'yjs'+'\t'+str(row[0])+'\n')
                #resultClickGeren.write('\n')
            cursor.execute(sqlJjr)
            for row in cursor.fetchall():
                #resultClickGeren.write(houseId+'\t'+houseIdClick[houseId])
                jjr.write(category+'\t'+city+'\t'+'other'+'\t'+str(row[0])+'\n')
                #resultClickGeren.write('\n')
    except:
        print city,'error'
