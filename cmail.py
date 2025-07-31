import smtplib 
from email.message import EmailMessage
def send_mail(to,subject,body):
    server = smtplib.SMTP_SSL('smtp.gmail.com',465) #creating obj for gmail
    server.login('pnsalekhyaists@gmail.com','wuig aiqh fexs nlna')
    msg=EmailMessage() #creating obj for EmailMessage to form email form
    msg['FROM']='pnsalekhyaists@gmail.com'
    msg['TO']=to
    msg['SUBJECT']=subject
    msg.set_content(body)
    server.send_message(msg)
    server.close()