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
st_sqReport = open(dateNow+'st-sq��Ӧ��ϵ.txt','w')
lp_sq_stReport = open(dateNow+'lp_sq_st��Ӧ��ϵ.txt','w')
dicDist = {}

for st in streets:
    for d in data:
        houseId,companyName,district,street,lp,clicks,datetime = d.split('\t')
        if st == street:
            dicDist[st] = district
            break
for st in streets:
    st_sqReport.write(st+'\t'+dicDist[st]+'\n')
st_sqReport.close()


dicDist = {}

for l in lps:
    for d in data:
        houseId,companyName,district,street,lp,clicks,datetime = d.split('\t')
        if l == lp:
            dicDist[l] = district+'\t'+street
            break
for l in lps:
    lp_sq_stReport.write(l+'\t'+dicDist[l]+'\n')
lp_sq_stReport.close()