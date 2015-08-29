# coding: gbk
import os,MySQLdb,time

def getSql(category,datetime,type):
    if type == 'jjr':
        if category == 'fang1':
            sql = 'SELECT street_id,street_name,xiaoqu_id,xiaoqu,huxing_shi,AVG(price),COUNT(1) ��Դ�� FROM house_source_rent WHERE agent=1 and source_type = 0 and listing_status >=5 and show_time>=unix_timestamp("'+datetime+'")group by street_name,xiaoqu,huxing_shi HAVING ��Դ��>=1;'
        elif category == 'fang3':
            sql = 'SELECT street_id,street_name,xiaoqu_id,xiaoqu,AVG(price),COUNT(1) ��Դ�� FROM house_source_share WHERE agent=1 and source_type = 0  and listing_status >=5 and  show_time>=unix_timestamp("'+datetime+'")group by street_name,xiaoqu HAVING ��Դ��>=1;'
        elif category == 'fang5':
            sql = 'SELECT street_id,street_name,xiaoqu_id,xiaoqu,huxing_shi,AVG(price),COUNT(1) ��Դ�� FROM house_source_sell WHERE agent=1 and source_type = 0  and listing_status >=5 and  show_time>=unix_timestamp("'+datetime+'")group by street_name,xiaoqu,huxing_shi HAVING ��Դ��>=1;'
        else:
            return '������'
    elif type == 'geren':
        if category == 'fang1':
            sql = 'SELECT street_id,street_name,xiaoqu_id,xiaoqu,huxing_shi,AVG(price),COUNT(1) ��Դ�� FROM house_source_rent WHERE listing_status >=5 and show_time>=unix_timestamp("'+datetime+'") and source_type = 0 group by street_name,xiaoqu,huxing_shi HAVING ��Դ��>=1;'
        elif category == 'fang3':
            sql = 'SELECT street_id,street_name,xiaoqu_id,xiaoqu,AVG(price),COUNT(1) ��Դ�� FROM house_source_share WHERE listing_status >=5 and  show_time>=unix_timestamp("'+datetime+'") and source_type = 0 group by street_name,xiaoqu HAVING ��Դ��>=1;'
        elif category == 'fang5':
            sql = 'SELECT street_id,street_name,xiaoqu_id,xiaoqu,huxing_shi,AVG(price),COUNT(1) ��Դ�� FROM house_source_sell WHERE listing_status >=5 and  show_time>=unix_timestamp("'+datetime+'") and source_type = 0 group by street_name,xiaoqu,huxing_shi HAVING ��Դ��>=1;'
        else:
            return '������'
    else:
        return "����������󣡴��룺������ڣ���������ݣ�jjr����geren"
    return sql

#���ж�Ӧ��ϵ��ͳ��
categorys=['fang1','fang3','fang5']
'''
citys={}

conn=MySQLdb.connect(host="192.168.116.20",user="yangyu",passwd="c1b78739d",port=3311,db="management",charset="gbk")
cursor = conn.cursor()
cursor.execute('SELECT pinyin,city_name FROM city;')
for row in cursor.fetchall():
    #print row[1],row[0]
    citys[row[1]]=row[0]
cursor.close()
citys['������'] = 'beijing'
citys['others']='others'
'''
cityNames = ['beijing','shanghai','shenzhen','wuhan','chengdou','xian','chongqing','guangzhou']

#�����������ֵ�ͳ��
for city in cityNames:
    print city
    #city = citys[city_name]
    conn=MySQLdb.connect(host="192.168.116.20",user="yangyu",passwd="c1b78739d",port=3310,db=city,charset="gbk")
    cursor=conn.cursor()
    for category in categorys:
        mianfei = open(city + '_' + category + '_mianfei.txt','w')
        sqlGeren = getSql(category,'2012-01-01',"geren")
        cursor.execute(sqlGeren)
        if category != 'fang3':
            for rows in cursor.fetchall():
                #resultClickGeren.write(houseId+'\t'+houseIdClick[houseId])
                mianfei.write(str(rows[0])+'\t'+str(rows[1])+'\t'+str(rows[2])+'\t'+str(rows[3])+'\t'+str(rows[4])+'\t'+str(rows[5])+'\t'+str(rows[6])+'\n')
                #resultClickGeren.write('\n')
        else:
            for rows in cursor.fetchall():
                #resultClickGeren.write(houseId+'\t'+houseIdClick[houseId])
                mianfei.write(str(rows[0])+'\t'+str(rows[1])+'\t'+str(rows[2])+'\t'+str(rows[3])+'\t'+str(rows[4])+'\t'+str(rows[5])+'\n')
                #resultClickGeren.write('\n')