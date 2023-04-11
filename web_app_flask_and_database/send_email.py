import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(email, height):
    from_email = 'bgtscerebrate@gmail.com'
    from_password = 'password'
    to_email = email
    
    subject = 'Height data'
    message = 'Hey there, your height is <strong>%s</strong>.' % height
    
    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email
    
    try:
        # Connect to Gmail's SMTP server
        gmail = smtplib.SMTP('smtp.gmail.com', 587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login(from_email, from_password)
        
         # Send the email
        gmail.send_message(msg)
        gmail.close()
        print('Email sent successfully.')
    except Exception as e:
        print('Failed to send email.Error', str(e))