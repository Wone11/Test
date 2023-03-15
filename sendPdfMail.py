
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

# from dotenv import load_dotenv

'''sending an email'''
try:
    msg = MIMEMultipart()
    with open('./test.pdf', 'r') as f:
        file = f.read()
    msg.attach(MIMEText(file))
    mail_server = smtplib.SMTP('smtp.gmail.com',587)
    mail_server.starttls()
    login=mail_server.login('sonangl2020@gmail.com','ujfojfsyxqsnsrqq')
    send= mail_server.sendmail("sonangl2020@gmail.com","ggirma143@gmail.com",msg.as_string())
    print(login)
except Exception as e:
    print(e)
    
