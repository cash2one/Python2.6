# -*- coding: gbk -*-
'''
���ʹ������ʼ�
С���壺http://www.cnblogs.com/xiaowuyi
'''

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

#����һ����������ʵ��
msg = MIMEMultipart()

#���츽��1
att1 = MIMEText(open('d:\\123.rar', 'rb').read(), 'base64', 'gb2312')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="123.doc"'#�����filename��������д��дʲô���֣��ʼ�����ʾʲô����
msg.attach(att1)

#���츽��2
att2 = MIMEText(open('d:\\123.txt', 'rb').read(), 'base64', 'gb2312')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="123.txt"'
msg.attach(att2)

#���ʼ�ͷ
msg['to'] = 'suchao.bbs@163.com'
msg['from'] = 'hfutsuchao@163.com'
msg['subject'] = 'hello world'
#�����ʼ�
try:
    server = smtplib.SMTP()
    server.connect('smtp.163.com')
    server.login('hfutsuchao','814155356')#XXXΪ�û�����XXXXXΪ����
    server.sendmail(msg['from'], msg['to'],msg.as_string())
    server.quit()
    print '���ͳɹ�'
except Exception, e:  
    print str(e)