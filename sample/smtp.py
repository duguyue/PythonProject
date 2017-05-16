import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender=''
receivers=['']

message=MIMEText('邮件测试','plain','utf-8')
message['From']=Header('Ivy','utf-8')
message['To']=Header('LinDL','utf-8')

subject='SMTP邮件测试'
message['Subject']=Header(subject,'utf-8')

try:
    smtpObj=smtplib.SMTP('localhost')
    smtpObj.sendmail(sender,receivers,message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
