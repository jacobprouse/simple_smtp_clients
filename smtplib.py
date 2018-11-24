import smtplib

#credentials
gmail_username = "########@gmail.com"
gmail_password = "########"

#sent from #######
mail_from = gmail_username

#sending to same email for convinience
rept = gmail_username
#subject of email
subject = 'How much easier is this?'
#contents
body = 'Wow a ton!!!'

#easy setup for email content
email_text = """\  
From: %s  
To: %s  
Subject: %s

%s
""" % (mail_from, ", ".join(rept), subject, body)

#try sending the email, if not print error
try:
    #connect to gmail via ssl
    mail_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    #send ehlo cmd
    mail_server.ehlo()
    #underneath wrapper this is sending the AUTH LOGIN cmd
    mail_server.login(gmail_username, gmail_password)
    #send the email, this does RCPT TO and MAIL FROM
    mail_server.sendmail(mail_from, rept, email_text)
    #closes the socket and quits
    mail_server.close()
    
    print('Sucess!')
except:
    print('whoops, something went wrong!')