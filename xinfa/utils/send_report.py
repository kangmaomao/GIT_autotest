import os
import json
import requests
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

#获取最新报告的文件名
def new_reportname(report):
    # 将测试报告文件夹下的所有文件名作为一个列表返回
    report='D:\\Python\\xinfa\\report\\'
    lists = os.listdir(report)
    # 对所有测试报告按照生成时间进行排序
    lists.sort(key=lambda filename: os.path.getmtime(report + filename))
    # 获取最新的测试报告
    new_report= lists[-1]
    return new_report

#使用钉钉发送测试报告

webhook = '你的webhook地址'

def send_dingding(filename):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    data = {
        "msgtype": "text",
        "text": {
            "content": "测试报告："+ "http://localhost:63342/login_test/report/"+filename
        },
        "at": {
            "atMobiles": [
                ''
            ],
            "isAtAll": False
        }
    }
    r = requests.post(url=webhook, headers=headers, data=json.dumps(data))
    return r



#报告路径
result_dir = 'D:\\Python\\xinfa\\report\\'

def format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

## 将最新测试报告放附件发送邮件，以qq邮箱为例
def send_email(file_new):
    smtpserver = 'smtp.qq.com'
    user = '你的邮箱'
    #password填写授权码（授权码如何获取大家可以百度一下）
    password = ''
    sender = '发送人'
    receivers = ['收件人']

    file = open(file_new,encoding='utf-8').read()

    #邮件正文
    # 三个参数：第一个为文本内容，第二个设置文本格式，第三个 utf-8 设置编码
    text = MIMEText('本次自动化测试结果见附件，请您下载查看~', 'plain', 'utf-8')
    #邮件附件
    att = MIMEText(file, 'html', 'utf-8')
    att["Content-Type"] = "application/octet-stream"
    subject = new_reportname(result_dir)
    att.add_header('ContenT-Disposition','attachment',filename =subject)
    # 将邮件正文和邮件附件都加入到多媒体报告
    msgRoot = MIMEMultipart()
    msgRoot['Subject'] = subject
    msgRoot['From'] = format_addr(u'某公司测试组 <%s>' % sender)
    msgRoot['To'] = format_addr(u'项目组所有人 <%s>' % receivers)
    msgRoot.attach(att)  # 将附件加载msg里
    msgRoot.attach(text)  # 将邮件正文加载msg里

    try:
        smt = smtplib.SMTP(smtpserver)
        smt.ehlo()
        smt.starttls()
        smt.login(user, password)
        smt.sendmail(sender, receivers, msgRoot.as_string())
        smt.quit()
        print('发送成功')
    except Exception as e:
        print('发送失败', e)