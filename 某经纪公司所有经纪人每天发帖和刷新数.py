# coding: gbk
import os,MySQLdb,time
conn=MySQLdb.connect(host="192.168.116.20",user="lixueshi",passwd="i14p4Dkyd",port=3320,db="house_premier",charset="GBK")

date1 = ['house_source_rent_premier','house_source_share_premier','house_source_sell_premier','house_source_loupan_premier']
date2 = ['house_source_storerent_premier','house_source_storetrade_premier','house_source_officerent_premier','house_source_officetrade_premier']
date3 = ['house_source_plant_premier']
sql = 'SELECT AccountId,accountName,BussinessScope FROM gcrm.customer JOIN gcrm.customer_account USING(CustomerId) WHERE CompanyName = "�Ϻ���ԭ���ز��������޹�˾"'
cursor = conn.cursor()
cursor.execute(sql)
dicAccount = {}
for row in cursor.fetchall():
    AccountId = row[0]
    accountName = row[1]
    BussinessScope = row[2]
    dicAccount[AccountId] = accountName + '\t' + str(BussinessScope)
'''
dic = {}
for accountId in dicAccount.keys():
    accountName,BussinessScope = dicAccount[accountId].split('\t')
    for d in range(1,7):
        dic['2012-12-02'] = 1
        dic['post'] = {}
        dic['ˢ��'] = {}
        dic['post'][accountId] = {}
        dic['ˢ��'][accountId] = {}
        dic['post'][accountId][d] = 0
        dic['ˢ��'][accountId][d] = 0
'''
for AccountId in dicAccount.keys():
    accountName,BussinessScope = dicAccount[AccountId].split('\t')
    cursor.execute('SET NAMES GBK;')
    if BussinessScope == '1':
        #print accountName
        for field in date1:
            sql = 'SELECT SUBSTR(FROM_UNIXTIME(post_at),9,2) ����,COUNT(1) FROM '+field+' WHERE account_id='+str(AccountId)+' AND post_at>=UNIX_TIMESTAMP("2012-12-14") and image_count>=4 GROUP BY ����'
            #print sql
            cursor.execute(sql)
            for row in cursor.fetchall():
                print('����'+'\t'+accountName+'\t'+str(row[0])+'\t'+str(row[1]))
                #pass
    elif BussinessScope == '2':
        for field in date2:
            sql = 'SELECT SUBSTR(FROM_UNIXTIME(post_at),9,2) ����,COUNT(1) FROM '+field+' WHERE account_id='+str(AccountId)+' AND post_at>=UNIX_TIMESTAMP("2012-12-14") and image_count>=4 GROUP BY ����'
            cursor.execute(sql)
            for row in cursor.fetchall():
                print('����'+'\t'+accountName+'\t'+str(row[0])+'\t'+str(row[1]))
                #pass
    elif BussinessScope == '3':
        for field in date2:
            sql = 'SELECT SUBSTR(FROM_UNIXTIME(post_at),9,2) ����,COUNT(1) FROM '+field+' WHERE account_id='+str(AccountId)+' AND post_at>=UNIX_TIMESTAMP("2012-12-14") and image_count>=4 GROUP BY ����'
            cursor.execute(sql)
            for row in cursor.fetchall():
                print('����'+'\t'+accountName+'\t'+str(row[0])+'\t'+str(row[1]))
                #pass
'''
sql = 'SELECT SUBSTR(FROM_UNIXTIME(RefreshAt),9,2) ����,accountId,COUNT(1) FROM house_premier.house_premier_refresh WHERE accountId in (SELECT AccountId FROM gcrm.customer JOIN gcrm.customer_account USING(CustomerId) WHERE CompanyName = "�Ϻ���ԭ���ز��������޹�˾") AND RefreshAt>=UNIX_TIMESTAMP("2012-12-14") GROUP BY ����,accountId'
cursor.execute(sql)
for row in cursor.fetchall():
    print('ˢ��'+'\t'+str(row[0])+'\t'+str(row[1])+'\t'+str(row[2]))
'''