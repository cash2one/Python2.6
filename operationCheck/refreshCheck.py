#coding:gbk
import sys,mySQLClass,time,json,os

os.system("color f0")

#print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
dateToday = time.strftime('%Y-%m-%d',time.localtime(time.time()))
dateYesterday = time.strftime('%Y-%m-%d',time.localtime(time.time()-86400))
cur = mySQLClass.MySQLClass('192.168.116.20',3320,'lixueshi','i14p4Dkyd')
cur.connectDB()
cur.selectDB('house_premier')

if len(sys.argv)>1:
    dateSerch = sys.argv[1]
    email = sys.argv[2]
else:
    dateSerch = raw_input('ˢ��ר�ã�ֻ�鵱�£������ѯ���ڣ���3~27��֮�䣩ʾ�� 14:\n')
    email = raw_input('Customer acount:')

if dateSerch == '':
    dateSerch = dateYesterday
elif len(dateSerch) == 2:
    dateSerch = dateToday[:-2] + dateSerch
elif len(dateSerch) == 1:
    dateSerch = dateToday[:-2] + '0' + dateSerch

day = [31, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30 ,31]

dateStart = dateSerch[:-2] + str (day[int(dateSerch[-2:]) - 3])

dateEnd = dateSerch[:-2] + str (day[int(dateSerch[-2:]) + 1])

#print dateStart,dateEnd

import html

params = {"UserName":"suchao","Domain":"@ganji.com","Password":"hFuT814155356134"}
url = "http://sso.ganji.com/Account/LogOn"

crm = html.Html()
crm.post(url,params,"")

if not email :
    sys.exit()

params = {'[Equal]Email':email,'accountListType':'2','page':'1','pagesize':'20','sortname':'CreatedTime','sortorder':'desc','unnamed':'none'}
url = "http://gcrm.ganji.com/HousingAccount/Items?listType=ForManagers"

creatorId = json.loads(crm.post(url,params,""))['Rows'][0]['Id']

crm.clear()

#operationTypeNum = raw_input('���Ҳ�������: 0->��Ʒˢ��     1->���ķ�ˢ��     2->����/ɾ������     3->�ƹ�/ȡ���ƹ�     4->�Զ���\n')

operationTypes = {"user-edit":"�༭��Դ","user-add-refresh":"������Ʒˢ��","user-del-refresh":"ȡ����Ʒˢ��", "user-add-refresh-assure":"�������ķ�ˢ��","user-del-refresh-assure":"ȡ�����ķ�ˢ��", "user-add":"������Դ","user-delete":"ɾ����Դ", "user-start-premier":"�����ƹ�","user-cancel-premier":"ȡ���ƹ�",'user-del-repeat-house':"ȡ��ѡ���ƹ������ظ�ˢ��",'user-add-repeat-house':"�����ƹ������ظ�ˢ��"}

cur.executeDB('set names "gbk";')

#if operationTypeNum != "4":
    #sql = 'select creatorName,operationType,createdTime from house_source_operation where creatorId= '+ creatorId +' and operationType in (' + operationTypes[operationTypeNum] + ') and (createdTime BETWEEN \"' + dateStart + '\" and \"' +dateEnd  + '\") and (message LIKE \"' + dateSerch + '%\" or createdTime = \"' + dateSerch + '\" )'
#sql = "SELECT SUBSTR(CreatedTime,1,10) ����,creatorname �ͻ�����,operationtype ��������,COUNT(1) ˢ�´��� FROM house_premier.house_source_operation WHERE creatorID=" + creatorId + " AND (createdTime BETWEEN \'" + dateStart + "\' and \'" +dateEnd  + "\') AND (message LIKE \'" + dateSerch + "%\' or createdTime LIKE \'" + dateSerch + "%\') GROUP BY SUBSTR(CreatedTime,1,10),OperationType ORDER BY createdtime DESC;"
sql = "SELECT SUBSTR(CreatedTime,1,10),creatorname,operationtype,COUNT(1) FROM house_premier.house_source_operation WHERE creatorID=" + creatorId + " AND (createdTime BETWEEN \'" + dateStart + "\' and \'" +dateEnd  + "\') AND (message LIKE \'" + dateSerch + "%\' or createdTime LIKE \'" + dateSerch + "%\') GROUP BY SUBSTR(CreatedTime,1,10),OperationType ORDER BY createdtime DESC;"
#sql = "SELECT SUBSTR(CreatedTime,1,10) ����,creatorname �ͻ�����,operationtype ��������,COUNT(1) �������� FROM house_premier.house_source_operation WHERE creatorID=184105 AND (createdTime BETWEEN '2013-08-1' AND '2013-09-1') AND (message LIKE '2013-08-%' OR createdTime LIKE '2013-08-%') GROUP BY SUBSTR(CreatedTime,1,10),OperationType ORDER BY createdtime DESC;"
#print sql

tmpFile = open("tmpFile.csv",'w')

print "\n\n����\t�ͻ�����\t��������\t��������"
tmpFile.write("����,�ͻ�����,��������,��������\n")
for r in cur.selectData(sql):
    try:
        print r[0] + '\t' + r[1] + '\t' + operationTypes[r[2]] + '\t' + str(r[3])
        tmpFile.write(r[0] + ',' + r[1] + ',' + operationTypes[r[2]] + ',' + str(r[3]) + '\n')
    except:
        print r[0] + '\t' + r[1] + '\t' + r[2] + '\t' + str(r[3])
        tmpFile.write(r[0] + ',' + r[1] + ',' + r[2] + ',' + str(r[3]) + '\n')
print "\n\n" + sql

tmpFile.close()
os.system('start tmpFile.csv')
os.system('refreshCheck.py')

cur.closeDB()