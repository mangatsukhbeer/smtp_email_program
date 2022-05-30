import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

receiver_email = "xyz@gmail.com" #test accounts used cannot be made public hence xyz.com
sender_email = "xyz@outlook.com" #test accounts used cannot be made public hence xyz.com

message = MIMEMultipart()

message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Test Completion Email"
body = MIMEText("This is Another Test email",'plain','utf-8')
message.attach(body)
file = "log.txt"
attachment = open(file,'rb')
obj = MIMEBase('application','octet-stream')
obj.set_payload((attachment).read())
encoders.encode_base64(obj)
obj.add_header('content-disposition','attachment',filename='log.txt')
message.attach(obj)

message = message.as_bytes()
try:
    smtpObj = smtplib.SMTP('smtp.outlook.com',587)
    smtpObj.starttls()
    smtpObj.login(sender_email,"TestPass")
    smtpObj.sendmail(sender_email,receiver_email,message)
    smtpObj.quit()
    print("Sent Successfully")
except smtplib.SMTPException:
    print("Error")
