# coding: gbk
import os,MySQLdb,time

dateNow = time.strftime('%Y-%m-%d',time.localtime(time.time()))

#�򿪲�������Ȧ���ֵ���¥�̵���Ϣ
data = open('C:\\Users\\suchao\\Desktop\\rent.txt').readlines()
districts = open(dateNow+'sqresult.txt').readlines()
streets = open(dateNow+'stresult.txt').readlines()
companys = open(dateNow+'cmyresult.txt').readlines()
lps = open(dateNow+'lpresult.txt').readlines()

districts = [i.split('\t')[0] for i in districts]
streets = [i.split('\t')[0] for i in streets]
companys = [i.split('\t')[0] for i in companys][:8]
lps = [i.split('\t')[0] for i in lps][:800]

#���ļ���׼��д��������
resultshi = open(dateNow+'shiresult.txt','w')
resultprice = open(dateNow+'priceresult.txt','w')

'''
districts = ['����','����','��̨','��ƽ','����','����','����','��ɽ','����','ʯ��ɽ']
streets = ['���','�ϵ�','�йش�','���˴�','����','�ļ���','��ҩ��','�����','������',
           '������','֪��·','��ֱ��','κ����','��ó','����','����·','������',
           '�㰲��','���Ӻ�','̫����','ѧԺ·','��������','˫����','������','������',
           '������','�Ƽ�԰��','���','������ѧ','³��','������','��Ȫ·','����',
           '��Ȼͤ','�Ұ���','����','��ʤ��','��԰��','����','���˴�СӪ','����·',
           '������','�����','������','������','�����','���ڽ�','������','CBD',
           '��̫ƽׯ','������','�˻�Ӫ','������','¬����','������','��ֽ��','��ȪӪ',
           '�½ֿ�','������¥','�����','����ׯ','�˽�','������','����ׯ','��ֱ����',
           'ţ��','����·','С����','��̳','������','��Ȫ��','�Ʒ���','������',
           '��ˮ̶','��ׯ','��չ','ľ�ص�','��¥���','������','��ʿ·','����ׯ',
           '�ʼҿ�','չ��·','������','��ɽ','�˱�ɽ','������','����վ','����',
           '����','С��','ʯ��ɽ','���԰','�ོ']
companys = ['�����д������ز��������޹�˾','�������ҷ��ز��������޹�˾','�����Ұ��Ҽҷ��ز��������޹�˾','������ԭ���ز��������޹�˾','�������﷿���������޹�˾','�������żκͷ��ز������������ι�˾']
#companys = ['�д���','����','�Ұ��Ҽ�','��ԭ','����','����','����������']
lps = open('lp.txt').readlines()
lps = [l[:-1] for l in lps]
'''

arrTime = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
dicDist = {}
dicPrice = {}

conn=MySQLdb.connect(host="192.168.116.20",user="lixueshi",passwd="i14p4Dkyd",port=3320,db="house_premier",charset="gbk")

#######################################����Ϊɸѡ��Ȧ��Ϣ#########################################

for d in data:
    houseId,companyName,district,street,lp,clicks,datetime = d.split('\t')
    cursor = conn.cursor()
    cursor.execute('select huxing_shi,price from house_source_rent_premier where house_id='+houseId+';')
    for row in cursor.fetchall():
        huxing_shi = row[0]
        price = str(row[1])
    cursor.close()
    if huxing_shi in dicDist:
        dicDist[huxing_shi][huxing_shi]['count'] = dicDist[huxing_shi][huxing_shi]['count'] + 1
        dicDist[huxing_shi][huxing_shi]['click'] = dicDist[huxing_shi][huxing_shi]['click'] + int(clicks)
        for company in companys:
            if company == companyName:
                dicDist[huxing_shi][company]['count'] = dicDist[huxing_shi][company]['count'] + 1
                dicDist[huxing_shi][company]['click'] = dicDist[huxing_shi][company]['click'] + int(clicks)
                break
    else:
        dicDist[huxing_shi] = {}
        dicDist[huxing_shi][huxing_shi] = {}
        dicDist[huxing_shi][huxing_shi]['count'] = 1
        dicDist[huxing_shi][huxing_shi]['click'] = int(clicks)
        for company in companys:
            dicDist[huxing_shi][company] = {}
            dicDist[huxing_shi][company]['count'] = 0
            dicDist[huxing_shi][company]['click'] = 0
    if price in dicPrice:
        dicPrice[price][price]['count'] = dicPrice[price][price]['count'] + 1
        dicPrice[price][price]['click'] = dicPrice[price][price]['click'] + int(clicks)
        for company in companys:
            if company == companyName:
                dicPrice[price][company]['count'] = dicPrice[price][company]['count'] + 1
                dicPrice[price][company]['click'] = dicPrice[price][company]['click'] + int(clicks)
                break
    else:
        dicPrice[price] = {}
        dicPrice[price][price] = {}
        dicPrice[price][price]['count'] = 1
        dicPrice[price][price]['click'] = int(clicks)
        for company in companys:
            dicPrice[price][company] = {}
            dicPrice[price][company]['count'] = 0
            dicPrice[price][company]['click'] = 0
for huxing_shi in dicDist:
    resultshi.write(str(huxing_shi)+'\t'+str(dicDist[huxing_shi][huxing_shi]['count'])+'-'+str(dicDist[huxing_shi][huxing_shi]['click']))
    for company in companys:
        resultshi.write('\t'+str(dicDist[huxing_shi][company]['count'])+'-'+str(dicDist[huxing_shi][company]['click']))
    resultshi.write('\n')
resultshi.close()

for price in dicPrice:
    resultprice.write(str(price)+'\t'+str(dicPrice[price][price]['count'])+'-'+str(dicPrice[price][price]['click']))
    for company in companys:
        resultprice.write('\t'+str(dicPrice[price][company]['count'])+'-'+str(dicPrice[price][company]['click']))
    resultprice.write('\n')
resultprice.close()

#os.system('pause')
