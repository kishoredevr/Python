import smtplib
import random
server=smtplib.SMTP("smtp.gmail.com",587)
server.ehlo()
server.starttls()
server.login("kishoredev37@gmail.com","999482222567dev")
msg=''
for d in range(4):
    e=random.randint(0,9)
    msg+=str(e)

server.sendmail("kishoredev37@gmail.com",input("mail id "),msg)
print("sent successfully")
