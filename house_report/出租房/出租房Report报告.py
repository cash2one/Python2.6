# coding: gbk
import os,MySQLdb,time
t= time.time()
dateNow = time.strftime('%Y-%m-%d',time.localtime(time.time()))
data = open('C:\\Users\\suchao\\Desktop\\rent.txt').readlines()

resultsq = open(dateNow+'resultsq.txt','w')
resultst = open(dateNow+'resultst.txt','w')
resultlp = open(dateNow+'resultlp.txt','w')
resultcmy = open(dateNow+'resultcmy.txt','w')

arrTime = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']

#-----------------------------------------------------------下面为提取相关信息------------------------#

#######################################以下为筛选商圈信息#########################################
dic = {}
for d in data:
    houseId,companyName,district,street,lp,clicks,datetime = d.split('\t')
    if dic.has_key(district):
        dic[district] = dic[district] + 1
    else:
        dic[district] = 1
for i in sorted(dic.items(),key=lambda e:e[1],reverse=True):resultsq.write(i[0]+'\t'+str(i[1])+'\n')
resultsq.close()

#######################################以下为筛选街道信息#########################################
dic = {}
for d in data:
    houseId,companyName,district,street,lp,clicks,datetime = d.split('\t')
    if dic.has_key(street):
        dic[street] = dic[street] + 1
    else:
        dic[street] = 1
for i in sorted(dic.items(),key=lambda e:e[1],reverse=True):resultst.write(i[0]+'\t'+str(i[1])+'\n')
resultst.close()

#######################################以下为筛选楼盘小区信息#########################################
dic = {}
for d in data:
    houseId,companyName,district,street,lp,clicks,datetime = d.split('\t')
    if dic.has_key(lp):
        dic[lp] = dic[lp] + 1
    else:
        dic[lp] = 1
for i in sorted(dic.items(),key=lambda e:e[1],reverse=True):resultlp.write(i[0]+'\t'+str(i[1])+'\n')
resultlp.close()

#######################################以下为筛选经纪公司信息#########################################
dic = {}
for d in data:
    houseId,companyName,district,street,lp,clicks,datetime = d.split('\t')
    if dic.has_key(companyName):
        dic[companyName] = dic[companyName] + 1
    else:
        dic[companyName] = 1
for i in sorted(dic.items(),key=lambda e:e[1],reverse=True):resultcmy.write(i[0]+'\t'+str(i[1])+'\n')
resultcmy.close()

#---------------------------------------------------------------下面为提取对应关系------------------------#

#打开并处理商圈，街道，楼盘等信息
districts = open(dateNow+'resultsq.txt').readlines()
streets = open(dateNow+'resultst.txt').readlines()
#companys = open(dateNow+'resultcmy.txt').readlines()
companys = open('company.txt').readlines()
lps = open(dateNow+'resultlp.txt').readlines()

districts = [i.split('\t')[0] for i in districts]
streets = [i.split('\t')[0] for i in streets]
#companys = [i.split('\t')[0] for i in companys][:8]
companys = [i[:-1] for i in companys]
lps = [i.split('\t')[0] for i in lps][:800]

#打开文件，准备写入结果数据
st_sqReport = open(dateNow+'st-sq对应关系.txt','w')
lp_sq_stReport = open(dateNow+'lp_sq_st对应关系.txt','w')
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

#--------------------------------------------------下面为处理区域、街道及小区统计信息------------------------#

#打开文件，准备写入结果数据

Reportdist = open(dateNow+'Reportdist.txt','w')
Reportst = open(dateNow+'Reportst.txt','w')
Reportlp = open(dateNow+'Reportlp.txt','w')

dicDist = {}

#######################################以下为筛选商圈信息#########################################

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
    Reportdist.write(l+'\t'+str(dicDist[l][l]['post'])+'\t'+str(dicDist[l][l]['clicks']))
    for company in companys:
        Reportdist.write('\t'+str(float(dicDist[l][company])/tmp*100)[:5]+'%')
    Reportdist.write('\n')
Reportdist.close()
dicDist = {}

#####################################下面是筛选街道信息###########################################
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
    if tmp == 0:
        tmp = 1
        print l,dicDist[l][company],tmp
    Reportst.write(l+'\t'+str(dicDist[l][l]['post'])+'\t'+str(dicDist[l][l]['clicks']))
    for company in companys:
        Reportst.write('\t'+str(float(dicDist[l][company])/tmp*100)[:5]+'%')
    Reportst.write('\n')
Reportst.close()
###################################下面是筛选楼盘小区信息##############################################

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
    Reportlp.write(l+'\t'+str(dicDist[l][l]['post'])+'\t'+str(dicDist[l][l]['clicks']))
    for company in companys:
        Reportlp.write('\t'+str(float(dicDist[l][company])/tmp*100)[:5]+'%')
    Reportlp.write('\n')
Reportlp.close()

#######################################以下为筛选热门时段信息#########################################
dic = {}
for company in companys:
    resultt = open(dateNow+company+'resultt.txt','w')
    all = 0
    for hour in arrTime:
        dic[hour] = 0
    for d in data:
        houseId,companyName,district,street,lp,clicks,datetime = d.split('\t')
        if companyName.find(company) != -1:
            t = datetime[11:13]
            dic[t] = dic[t] + 1
    a = [int(i) for i in dic.values()]
    all = sum(a)
    for hour in arrTime:
        try:
            tmps = float(dic[hour])/all*100
        except:
            tmps = 0
            print company,hour
        resultt.write(str(tmps)[:5]+'%\n')
    resultt.close()

#--------------------------------------------------下面为处理室型、价格相关统计信息------------------------#

#打开文件，准备写入结果数据
#rentShiPrice = open(dateNow+'renttmpfile.txt','r').readlines()
resultshi = open(dateNow+'resultshi.txt','w')
resultprice = open(dateNow+'resultprice.txt','w')

#######################################以下为筛选价格和室型信息#########################################

conn=MySQLdb.connect(host="192.168.116.20",user="lixueshi",passwd="i14p4Dkyd",port=3328,db="house_premier",charset="gbk")

print conn

dicDist = {}
dicPrice = {}
dicArea = {}

for d in data:
    house_id,companyName,district,street,lp,clicks,datetime = d.split('\t')
    cursor = conn.cursor()
    try:
        cursor.execute('select huxing_shi,price from house_source_rent_premier where house_id='+house_id+';')
        for row in cursor.fetchall():
            if len(row) >0:
                huxing_shi = row[0]
                price = str(row[1])
    except:
        print '连接出错'
    try:
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
    except:
        print house_id+' 不存在'

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

#######################################以下为价格和室型信息的后续处理#########################################

resultshi = open(dateNow+'resultshi.txt').readlines()
resultprice = open(dateNow+'resultprice.txt').readlines()
Reportshi = open(dateNow+'ReportShi.txt','w')
Reportprice = open(dateNow+'ReportPrice.txt','w')
for shi in resultshi:
    s,allCount,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10 = shi.split('\t')
    Reportshi.write(s+'\t'+allCount.split('-')[0]+'\t'+allCount.split('-')[1]+'\t'+c1.split('-')[0]+'\t'+c2.split('-')[0]+'\t'+c3.split('-')[0]+'\t'+c4.split('-')[0]+'\t'+c5.split('-')[0]+'\t'+c6.split('-')[0]+'\t'+c7.split('-')[0]+'\t'+c8.split('-')[0]+'\t'+c9.split('-')[0]+'\t'+c10.split('-')[0]+'\n')
Reportshi.close()
for price in resultprice:
    p,allCount,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10 = price.split('\t')
    Reportprice.write(p+'\t'+allCount.split('-')[0]+'\t'+allCount.split('-')[1]+'\t'+c1.split('-')[0]+'\t'+c2.split('-')[0]+'\t'+c3.split('-')[0]+'\t'+c4.split('-')[0]+'\t'+c5.split('-')[0]+'\t'+c6.split('-')[0]+'\t'+c7.split('-')[0]+'\t'+c8.split('-')[0]+'\t'+c9.split('-')[0]+'\t'+c10.split('-')[0]+'\n')
Reportprice.close()
#print('总用时:\t'+str(int(time.time())-int(t))+'s\n')
os.system('shutdown -h')