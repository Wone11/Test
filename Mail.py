import smtplib
# from dotenv import load_dotenv

'''sending an email'''
try:
    mail_server = smtplib.SMTP('smtp.gmail.com',587)
    mail_server.set_debuglevel(1)
    mail_server.starttls()
    login=mail_server.login('sonangl2020@gmail.com','ujfojfsyxqsnsrqq')
    send= mail_server.sendmail("sonangl2020@gmail.com","ggirma143@gmail.com","email send by sonangl..")
    print(login)
except Exception as e:
    print(e)
    
