#coding: gbk
import os,MySQLdb,time
dianji = open('C:\\Users\\suchao\\Desktop\\dianji.log','r').readlines()
xianshi = open('C:\\Users\\suchao\\Desktop\\xianshi.log','r').readlines()

datetime = ['2012-11-08','2012-11-09','2012-11-10','2012-11-11','2012-11-12','2012-11-13']
'''
resultFang1Dianji = open('resultFang1Dianji.txt','w')
resultFang3Dianji = open('resultFang3Dianji.txt','w')
resultFang5Dianji = open('resultFang5Dianji.txt','w')

resultFang1Xianshi = open('resultFang1Xianshi.txt','w')
resultFang3Xianshi = open('resultFang3Xianshi.txt','w')
resultFang5Xianshi = open('resultFang5Xianshi.txt','w')
'''
resultCityClickDuankou = open('resultCityClickDuankou.txt','w')
resultCityClickMianfei = open('resultCityClickMianfei.txt','w')
resultCityXianshiDuankou = open('resultCityXianshiDuankou.txt','w')
resultCityXianshiMianfei = open('resultCityXianshiMianfei.txt','w')

fourCities = ['bj','sh','gz','sz']

def getSql(category,houseId,type='zhongjie'):
    #category = houseIdClick[houseId].split('\t')[0].split('_')[1]
    if type == 'zhongjie':
        if category == 'fang1':
            sql = 'SELECT c.CompanyName �ͻ���˾, district_name ����, street_name �ֵ�, title ����, image_count ͼƬ��, TYPE Ƶ������, bid_status �Ƿ񾺼�, price �۸�, xiaoqu С������,fang_xing ��������,AREA ���,chaoxiang ����,zhuangxiu װ�����,pay_type ���ʽ,huxing_shi ��,huxing_ting ��,huxing_wei ��,peizhi ��������  FROM house_premier.house_source_rent_premier rp INNER JOIN gcrm.customer_account cb INNER JOIN gcrm.customer c ON rp.account_id=cb.AccountId AND cb.CustomerId=c.CustomerId WHERE rp.house_id='+houseId+';'
        elif category == 'fang3':
            sql = 'SELECT c.CompanyName �ͻ���˾, district_name ����, street_name �ֵ�, title ����, image_count ͼƬ��, TYPE Ƶ������, bid_status �Ƿ񾺼�, price �۸�, xiaoqu С������,fang_xing ��������,AREA ���,chaoxiang ����,zhuangxiu װ�����,pay_type ���ʽ,house_type ����������,peizhi ��������  FROM house_premier.house_source_share_premier rp INNER JOIN gcrm.customer_account cb INNER JOIN gcrm.customer c ON rp.account_id=cb.AccountId AND cb.CustomerId=c.CustomerId WHERE rp.house_id='+houseId+';'
        elif category == 'fang5':
            sql = 'SELECT c.CompanyName �ͻ���˾, district_name ����, street_name �ֵ�, title ����, image_count ͼƬ��, TYPE Ƶ������, bid_status �Ƿ񾺼�, price �۸�, xiaoqu С������,fang_xing ��������,AREA ���,chaoxiang ����,zhuangxiu װ�����,huxing_shi ��,huxing_ting ��,huxing_wei ��  FROM house_premier.house_source_sell_premier rp INNER JOIN gcrm.customer_account cb INNER JOIN gcrm.customer c ON rp.account_id=cb.AccountId AND cb.CustomerId=c.CustomerId WHERE rp.house_id='+houseId+';'
        else:
            return '������'
    elif type == 'mianfei':
        if category == 'fang1':
            sql = 'SELECT district_name ����, street_name �ֵ�, title ����, image_count ͼƬ��, price �۸�, xiaoqu С������,fang_xing ��������,AREA ���,chaoxiang ����,zhuangxiu װ�����,pay_type ���ʽ,huxing_shi ��,huxing_ting ��,huxing_wei ��,peizhi �������� FROM house_source_rent WHERE puid='+houseId+';'
        elif category == 'fang3':
            sql = 'SELECT district_name ����, street_name �ֵ�, title ����, image_count ͼƬ��, price �۸�, xiaoqu С������,fang_xing ��������,AREA ���,chaoxiang ����,zhuangxiu װ�����,pay_type ���ʽ,house_type ���������� ,huxing_shi ��,huxing_ting ��,huxing_wei ��,peizhi �������� FROM house_source_share WHERE puid='+houseId+';'
        elif category == 'fang5':
            sql = 'SELECT district_name ����, street_name �ֵ�, title ����, image_count ͼƬ��, price �۸�, xiaoqu С������,fang_xing ��������,AREA ���,chaoxiang ����,zhuangxiu װ�����,huxing_shi ��,huxing_ting ��,huxing_wei �� FROM house_source_sell WHERE puid='+houseId+';'
        else:
            return '������'
    else:
        return "����������󣡴��룺��𣬷�Դ�ɣ�"
    return sql

citys = {}

cityChange={}

conn=MySQLdb.connect(host="192.168.116.20",user="yangyu",passwd="c1b78739d",port=3310,db="management",charset="gbk")
cursor = conn.cursor()
cursor.execute('SELECT domain,pinyin FROM city;')
for row in cursor.fetchall():
    cityChange[row[0]]=row[1]
cursor.close()


for d in dianji:
    date,agent,tuiguang,url,times = d.split('\t')
    #��ȡ���к������Լ���ԴID
    city = url[url.find('//')+2:url.find('.')]
    category = url[url.find('/fang')+1:url.find('/fang')+6]
    if url == '-':
        house_id = '0'
    elif url.find('tuiguang-') != -1:
        house_id = url.split('tuiguang-')[1]
        house_id = house_id[:house_id.find('.htm')]
    else:
        try:
            house_id = url.split('/fang')[1]
            if house_id.find('x.htm') != -1:
                house_id = house_id[2:house_id.find('x.htm')]
            else:
                house_id = 0
        except:
            house_id = 0
    if city in fourCities:
        if tuiguang == 'tuiguang=1':
            try:
                conn=MySQLdb.connect(host="192.168.116.20",user="lixueshi",passwd="i14p4Dkyd",port=3320,db="house_premier",charset="gbk")
                sql = getSql(category,house_id,'zhongjie')
            except:
                print 'sqlerror77',d
                continue
            cursor = conn.cursor()
            cursor.execute(sql)
        elif tuiguang == 'tuiguang=0':
            city = cityChange[city]
            try:
                conn=MySQLdb.connect(host="192.168.116.20",user="yangyu",passwd="c1b78739d",port=3310,db=city,charset="gbk")
                sql = getSql(category,house_id,'mianfei')
            except:
                try:
                    conn=MySQLdb.connect(host="192.168.116.20",user="yangyu",passwd="c1b78739d",port=3310,db="others",charset="gbk")
                    sql = getSql(category,house_id,'mianfei')
                except:
                    try:
                        conn=MySQLdb.connect(host="192.168.116.20",user="yangyu",passwd="c1b78739d",port=3310,db="others",charset="gbk")
                        sql = getSql(category,house_id,'mianfei')
                    except:
                        print 'sqlerror95',d
                        continue
            cursor = conn.cursor()
            cursor.execute(sql)
        for row in cursor.fetchall():
            if tuiguang == 'tuiguang=1':
                resultCityClickDuankou.write(date+'\t'+city+'\t'+category+'\t'+agent+'_'+tuiguang+'\t'+house_id+'\t'+times[:-1])
                for i in row:
                    resultCityClickDuankou.write('\t'+str(i))
                resultCityClickDuankou.write('\n')
            else:
                resultCityClickMianfei.write(date+'\t'+city+'\t'+category+'\t'+agent+'_'+tuiguang+'\t'+house_id+'\t'+times[:-1])
                for i in row:
                    resultCityClickMianfei.write('\t'+str(i))
                resultCityClickMianfei.write('\n')
resultCityClickMianfei.close()
resultCityClickDuankou.close()

'''
citys = {}

for x in xianshi:
    date,agent,tuiguang,url,times = x.split('\t')
    city = url[url.find('//')+2:url.find('.')]
    category = url[url.find('/fang')+1:url.find('/fang')+6]
    if url == '-':
        house_id = '0'
    elif url.find('tuiguang-') != -1:
        house_id = url.split('tuiguang-')[1]
        house_id = house_id[:house_id.find('.htm')]
    else:
        try:
            house_id = url.split('/fang')[1]
            if house_id.find('x.htm') != -1:
                house_id = house_id[2:house_id.find('x.htm')]
            else:
                house_id = 0
        except:
            house_id = 0
    if city in fourCities:
        if tuiguang == 'tuiguang=1':
            try:
                conn=MySQLdb.connect(host="192.168.116.20",user="lixueshi",passwd="i14p4Dkyd",port=3320,db="house_premier",charset="gbk")
                sql = getSql(category,house_id,'zhongjie')
            except:
                print 'sqlerror165',x
                continue
            cursor = conn.cursor()
            cursor.execute(sql)
        elif tuiguang == 'tuiguang=0':
            city = cityChange[city]
            try:
                conn=MySQLdb.connect(host="192.168.116.20",user="yangyu",passwd="c1b78739d",port=3310,db=city,charset="gbk")
                sql = getSql(category,house_id,'mianfei')
            except:
                try:
                    conn=MySQLdb.connect(host="192.168.116.20",user="yangyu",passwd="c1b78739d",port=3310,db="others",charset="gbk")
                    sql = getSql(category,house_id,'mianfei')
                except:
                    try:
                        conn=MySQLdb.connect(host="192.168.116.20",user="yangyu",passwd="c1b78739d",port=3310,db="others",charset="gbk")
                        sql = getSql(category,house_id,'mianfei')
                    except:
                        print 'sqlerror183',x
                        continue
            cursor = conn.cursor()
            cursor.execute(sql)
        for row in cursor.fetchall():
            if tuiguang == 'tuiguang=1':
                resultCityXianshiDuankou.write(date+'\t'+city+'\t'+category+'\t'+agent+'_'+tuiguang+'\t'+house_id+'\t'+times[:-1])
                for i in row:
                    resultCityXianshiDuankou.write('\t'+str(i))
                resultCityXianshiDuankou.write('\n')
            else:
                resultCityXianshiMianfei.write(date+'\t'+city+'\t'+category+'\t'+agent+'_'+tuiguang+'\t'+house_id+'\t'+times[:-1])
                for i in row:
                    resultCityXianshiMianfei.write('\t'+str(i))
                resultCityXianshiMianfei.write('\n')
resultCityXianshiDuankou.close()
resultCityXianshiMianfei.close()
'''