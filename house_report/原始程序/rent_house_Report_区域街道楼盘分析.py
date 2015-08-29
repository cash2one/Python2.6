# coding: gbk
import os,MySQLdb,time
t= time.time()
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

distReport = open(dateNow+'distReport.txt','w')
stReport = open(dateNow+'stReport.txt','w')
lpReport = open(dateNow+'lpReport.txt','w')
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
companys = ['�д���','����','�Ұ��Ҽ�','��ԭ','����','����']
#companys = ['�����д������ز��������޹�˾','�������ҷ��ز��������޹�˾','�����Ұ��Ҽҷ��ز��������޹�˾','������ԭ���ز��������޹�˾','�������﷿���������޹�˾','�������żκͷ��ز������������ι�˾']
#companys = ['�����д������ز��������޹�˾','�������ҷ��ز��������޹�˾','�����Ұ��Ҽҷ��ز��������޹�˾','������ԭ���ز��������޹�˾','�������﷿���������޹�˾','�������żκͷ��ز������������ι�˾','����������']
#companys = ['�д���','����','�Ұ��Ҽ�','��ԭ','����','����','����������']
lps = open('lp.txt').readlines()
lps = [l[:-1] for l in lps]
'''

arrTime = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
dicDist = {}

#######################################����Ϊɸѡ��Ȧ��Ϣ#########################################

for st in districts:
    dicDist[st] = {}
for st in districts:
    dicDist[st][st] = {}
    dicDist[st][st]['post'] = 0
    dicDist[st][st]['clicks'] = 0
    for company in companys:
        dicDist[st][company] = 0
for d in data:
    houseId,companyName,district,street,lp,clicks,datetime = d.split('\t')
    for st in districts:
        if district == st:
            dicDist[st][st]['post'] = dicDist[st][st]['post'] + 1
            dicDist[st][st]['clicks'] = dicDist[st][st]['clicks'] + int(clicks)
            for company in companys:
                if companyName == company:
                    dicDist[st][company] = dicDist[st][company] + 1
                    break
            break
for l in districts:
    tmp = dicDist[l][l]['post']
    distReport.write(l+'\t'+str(dicDist[l][l]['post'])+'\t'+str(dicDist[l][l]['clicks']))
    for company in companys:
        distReport.write('\t'+str(float(dicDist[l][company])/tmp*100)[:5]+'%')
    distReport.write('\n')

dicDist = {}

#####################################������ɸѡ�ֵ���Ϣ###########################################
for st in streets:
    dicDist[st] = {}
for st in streets:
    dicDist[st][st] = {}
    dicDist[st][st]['post'] = 0
    dicDist[st][st]['clicks'] = 0
    for company in companys:
        dicDist[st][company] = 0
for d in data:
    houseId,companyName,district,street,lp,clicks,datetime = d.split('\t')
    if street == '':
        street = district
    for st in streets:
        if street == st:
            dicDist[st][st]['post'] = dicDist[st][st]['post'] + 1
            dicDist[st][st]['clicks'] = dicDist[st][st]['clicks'] + int(clicks)
            for company in companys:
                if companyName == company:
                    dicDist[st][company] = dicDist[st][company] + 1
                    break
            break

for l in streets:
    tmp = dicDist[l][l]['post']
    stReport.write(l+'\t'+str(dicDist[l][l]['post'])+'\t'+str(dicDist[l][l]['clicks']))
    for company in companys:
        stReport.write('\t'+str(float(dicDist[l][company])/tmp*100)[:5]+'%')
    stReport.write('\n')
###################################������ɸѡ¥��С����Ϣ##############################################

dicDist = {}

for l in lps:
    dicDist[l] = {}
for l in lps:
    dicDist[l][l] = {}
    dicDist[l][l]['post'] = 0
    dicDist[l][l]['clicks'] = 0
    for company in companys:
        dicDist[l][company] = 0
for d in data:
    houseId,companyName,district,street,lp,clicks,datetime = d.split('\t')
    for l in lps:
        if lp == l:
            dicDist[l][l]['post'] = dicDist[l][l]['post'] + 1
            dicDist[l][l]['clicks'] = dicDist[l][l]['clicks'] + int(clicks)
            for company in companys:
                if companyName == company:
                    dicDist[l][company] = dicDist[l][company] + 1
                    break
            break

for l in lps:
    tmp = dicDist[l][l]['post']
    lpReport.write(l+'\t'+str(dicDist[l][l]['post'])+'\t'+str(dicDist[l][l]['clicks']))
    for company in companys:
        lpReport.write('\t'+str(float(dicDist[l][company])/tmp*100)[:5]+'%')
    lpReport.write('\n')

print time.time()-t
#os.system('pause')