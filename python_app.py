"""
> Go over our email and set up the 2 factor Authentication
> Generate App password
> Create the function to send the email
"""
from email.message import EmailMessage
from emailpassword import Password
import ssl
import smtplib

email_sender = 'john7ouma@gmail.com'
email_password = Password

email_receiver = 'beladhiambo@gmail.com'
subject = "Love of my life."

body = """
The love of my life is you and am very lucky to have you. i thank God everyday
that he gave me you!
"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
