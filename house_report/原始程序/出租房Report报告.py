# coding: gbk
import os,MySQLdb,time
t= time.time()
dateNow = time.strftime('%Y-%m-%d',time.localtime(time.time()))
data = open('C:\\Users\\suchao\\Desktop\\rent.txt').readlines()

sqresult = open(dateNow+'sqresult.txt','w')
stresult = open(dateNow+'stresult.txt','w')
lpresult = open(dateNow+'lpresult.txt','w')
cmyresult = open(dateNow+'cmyresult.txt','w')
tresult = open(dateNow+'tresult.txt','w')

arrTime = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']

#-----------------------------------------------------------����Ϊ��ȡ�����Ϣ------------------------#

#######################################����Ϊɸѡ��Ȧ��Ϣ#########################################
dic = {}
for d in data:
    houseId,companyName,district,street,lp,clicks,datetime = d.split('\t')
    if dic.has_key(district):
        dic[district] = dic[district] + 1
    else:
        dic[district] = 1
for i in sorted(dic.items(),key=lambda e:e[1],reverse=True):sqresult.write(i[0]+'\t'+str(i[1])+'\n')
sqresult.close()

#######################################����Ϊɸѡ�ֵ���Ϣ#########################################
dic = {}
for d in data:
    houseId,companyName,district,street,lp,clicks,datetime = d.split('\t')
    if dic.has_key(street):
        dic[street] = dic[street] + 1
    else:
        dic[street] = 1
for i in sorted(dic.items(),key=lambda e:e[1],reverse=True):stresult.write(i[0]+'\t'+str(i[1])+'\n')
stresult.close()

#######################################����Ϊɸѡ¥��С����Ϣ#########################################
dic = {}
for d in data:
    houseId,companyName,district,street,lp,clicks,datetime = d.split('\t')
    if dic.has_key(lp):
        dic[lp] = dic[lp] + 1
    else:
        dic[lp] = 1
for i in sorted(dic.items(),key=lambda e:e[1],reverse=True):lpresult.write(i[0]+'\t'+str(i[1])+'\n')
lpresult.close()

#######################################����Ϊɸѡ���͹�˾��Ϣ#########################################
dic = {}
for d in data:
    houseId,companyName,district,street,lp,clicks,datetime = d.split('\t')
    if dic.has_key(companyName):
        dic[companyName] = dic[companyName] + 1
    else:
        dic[companyName] = 1
for i in sorted(dic.items(),key=lambda e:e[1],reverse=True):cmyresult.write(i[0]+'\t'+str(i[1])+'\n')
cmyresult.close()

#######################################����Ϊɸѡ����ʱ����Ϣ#########################################
dic = {}
for time in arrTime:
    dic[time] = 0
for d in data:
    houseId,companyName,district,street,lp,clicks,datetime = d.split('\t')
    if companyName.find('�д���') != -1:
        t = datetime[11:13]
        dic[t] = dic[t] + 1
for time in arrTime:
    tresult.write(time+'\t'+str(dic[time])+'\n')
tresult.close()

#---------------------------------------------------------------����Ϊ��ȡ��Ӧ��ϵ------------------------#

#�򿪲�������Ȧ���ֵ���¥�̵���Ϣ
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

#--------------------------------------------------����Ϊ�������򡢽ֵ���С��ͳ����Ϣ------------------------#

#���ļ���׼��д��������

distReport = open(dateNow+'distReport.txt','w')
stReport = open(dateNow+'stReport.txt','w')
lpReport = open(dateNow+'lpReport.txt','w')

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
distReport.close()
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
stReport.close()
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
lpReport.close()

#--------------------------------------------------����Ϊ�������͡��۸����ͳ����Ϣ------------------------#

print time.time()-t
#os.system('pause')