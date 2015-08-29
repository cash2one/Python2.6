# coding: gbk
import os,MySQLdb,time

citys = {'beijing':'����','shanghai':'�Ϻ�','shenzhen':'����','guangzhou':'����','xian':'����','shenyang':'����','jinan':'����','dalian':'����','hangzhou':'����','zhengzhou':'֣��','xiamen':'����','nanjing':'�Ͼ�','wuhan':'�人','suzhou':'����','kunming':'����','chongqing':'����','tianjin':'���','chengdou':'�ɶ�','qingdao':'�ൺ','hefei':'�Ϸ�','fuzhou':'����','shijiazhuang':'ʯ��ׯ'}

resultRent = open('rent.txt','w')
resultShare = open('share.txt','w')

#rent AVG_price
for city in citys.keys():
    conn=MySQLdb.connect(host="192.168.116.20",user="yangyu",passwd="c1b78739d",port=3310,db=city,charset="GBK")
    #sql = "SELECT district_name,street_name,huxing_shi,AVG(price),COUNT(1) hs FROM house_source_rent WHERE post_at>=UNIX_TIMESTAMP('2013-9-29') AND huxing_shi<=3 AND huxing_shi>=1 GROUP BY district_name,street_name,huxing_shi HAVING hs>=3"
    sql = "SELECT huxing_shi,AVG(price),COUNT(1) hs FROM house_source_rent WHERE post_at>=UNIX_TIMESTAMP('2013-11-1') AND huxing_shi<=3 AND huxing_shi>=1 GROUP BY huxing_shi HAVING hs>=3"
    cursor = conn.cursor()
    cursor.execute(sql)
    for rows in cursor.fetchall():
        try:
            #resultRent.write(citys[city] + '\t' + rows[0] + '\t' + rows[1] + '\t' + str(rows[2]) + '\t' + str(int(rows[3])) + '\t' + str(rows[4]) + '\n')
            resultRent.write(citys[city] + '\t' + str(rows[0]) + '\t' + str(rows[1]) + '\t' + str(rows[2]) + '\n')
        except Exception, e:
            print e, rows
    cursor.close()
    conn.close()

#share AVG_price
for city in citys.keys():
    conn=MySQLdb.connect(host="192.168.116.20",user="yangyu",passwd="c1b78739d",port=3310,db=city,charset="GBK")
    #sql = "SELECT district_name,street_name,AVG(price),count(1) hs FROM house_source_share WHERE post_at>=UNIX_TIMESTAMP('2013-9-29') GROUP BY district_name,street_name having hs>=3"
    sql = "SELECT AVG(price),count(1) hs FROM house_source_share WHERE post_at>=UNIX_TIMESTAMP('2013-11-1') having hs>=3"
    cursor = conn.cursor()
    cursor.execute(sql)
    for rows in cursor.fetchall():
        try:
            #resultShare.write(citys[city] + '\t' + rows[0] + '\t' + rows[1] + '\t' + str(int(rows[2])) + '\t' + str(rows[3]) + '\n')
            resultShare.write(citys[city] + '\t' + str(rows[0]) + '\t' + str(rows[1]) + '\n')
        except Exception, e:
            print e, rows
    cursor.close()
    conn.close()

citys = {'0':'����','100':'�Ϻ�','401':'����','400':'����','2300':'����','800':'����','1500':'����','801':'����','600':'����','1200':'֣��','1001':'����','900':'�Ͼ�','2500':'�人','901':'����','2800':'����','300':'����','200':'���','500':'�ɶ�','1501':'�ൺ','1600':'�Ϸ�','1000':'����','1100':'ʯ��ׯ'}

conn=MySQLdb.connect(host="192.168.116.20",user="suchao",passwd="CE7w7pTNB",port=3328,db="house_premier",charset="GBK")

resulttgRent = open('tg_rent.txt','w')
resulttgShare = open('tg_share.txt','w')

#rent AVG_price
for city in citys.keys():
    #sql = "SELECT district_name,street_name,huxing_shi,AVG(price),COUNT(1) hs FROM house_source_rent_premier WHERE city=" + city + " and post_at>=UNIX_TIMESTAMP('2013-9-29') AND huxing_shi<=3 AND huxing_shi>=1 GROUP BY district_name,street_name,huxing_shi HAVING hs>=3"
    sql = "SELECT huxing_shi,AVG(price),COUNT(1) hs FROM house_source_rent_premier WHERE city=" + city + " and post_at>=UNIX_TIMESTAMP('2013-11-1') AND huxing_shi<=3 AND huxing_shi>=1 GROUP BY huxing_shi HAVING hs>=3"
    #print sql
    cursor = conn.cursor()
    cursor.execute(sql)
    for rows in cursor.fetchall():
        try:
            #resulttgRent.write(citys[city] + '\t' + rows[0] + '\t' + rows[1] + '\t' + str(rows[2]) + '\t' + str(int(rows[3])) + '\t' + str(rows[4]) + '\n')
            resulttgRent.write(citys[city] + '\t' + str(rows[0]) + '\t' + str(rows[1]) + '\t' + str(rows[2]) + '\n')
        except Exception, e:
            print e, rows

#share AVG_price
for city in citys.keys():
    #sql = "SELECT district_name,street_name,AVG(price),count(1) hs FROM house_source_share_premier WHERE city=" + city + " and post_at>=UNIX_TIMESTAMP('2013-9-29') GROUP BY district_name,street_name having hs>=3"
    sql = "SELECT AVG(price),count(1) hs FROM house_source_share_premier WHERE city=" + city + " and post_at>=UNIX_TIMESTAMP('2013-11-1') having hs>=3"
    #print sql
    cursor = conn.cursor()
    cursor.execute(sql)
    for rows in cursor.fetchall():
        try:
            #resulttgShare.write(citys[city] + '\t' + rows[0] + '\t' + rows[1] + '\t' + str(int(rows[2])) + '\t' + str(rows[3]) + '\n')
            resulttgShare.write(citys[city] + '\t' + str(rows[0]) + '\t' + str(rows[1]) + '\n')
        except Exception, e:
            print e, rows
