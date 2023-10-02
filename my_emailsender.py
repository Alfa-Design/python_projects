from email.message import EmailMessage
from emailpassword import Password 
import ssl
import smtplib

sender_email = 'john7ouma@gmail.com'
password_of_email = Password

receiver_of_email = 'beladhiambo@gmail.com'
subject = input('subject: ')

body = input('body: ')

em = EmailMessage() 
em['From'] = sender_email
em['To'] = receiver_of_email
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(sender_email, password_of_email)
    smtp.sendmail(sender_email, receiver_of_email, em.as_string())