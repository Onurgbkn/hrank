import smtplib

from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("onur@gmail.com", "123456")




msg = MIMEMultipart()

msg['From'] = ''
msg['To'] = ''
msg['Subject'] = ''


message = 'This message send with python'

msg.attach(MIMEText(message, 'plain'))


filename = 't.png'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attacment; filename={filename}')
msg.attach(p)

text = msg.as_string()

server.sendmail("from@gm", "to@gm", text)

server.quit()