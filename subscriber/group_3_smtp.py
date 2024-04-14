'''
Final Project - Group 3

Course and Section: COMP216-003 (2024-Winter)
Professor: Rissan Devaraja
Deadline: 2024-04-16

Amanda Yuri Monteiro Ike
Oluwatobiloba Abel
Rithin Peter
Vinicio Jacome Gomez
Yeshi Ngawang
'''


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = 'smtp.gmail.com'
PORT = 587
EMAIL_ACC = '2024comp216group3@gmail.com'
password_file = open('password.txt', 'r')
PASSWORD = password_file.read()

def send_email(recipient_email, topic, data_quality_info, invalid_data):
    html_msg = f'''<html><body>
    <h3>Hello</h3>
    <p>It was identified an <u>invalid</u> data on the Topic "{topic}".</p> 
    <h4>Data: </h4>
    <p>{invalid_data}</p>
    <br />
    <p>Details:</p>
    <p>{data_quality_info}</p>
    <p>Please, check the data and take the necessary actions.</p>
    <br />
    <p>Please, do not reply to this email.</p>
    <p>Thank you.</p>
    <p><b>COMP216 - Group 3<b></p>
    </body></html>'''

    message = MIMEMultipart('alternative')
    message['From'] = EMAIL_ACC
    message['To'] = recipient_email
    message['Subject'] = '[Data Quality Report] Invalid Data Detected'

    email_content = MIMEText(html_msg, 'html') 
    message.attach(email_content)

    try:
        with smtplib.SMTP(SMTP_SERVER, PORT) as smtp_server:
            smtp_server.starttls()
            smtp_server.login(EMAIL_ACC, PASSWORD)
            smtp_server.sendmail(EMAIL_ACC, recipient_email, message.as_string())
    except Exception as e:
        print(f'Error on send email: {e}')
    else:
        print('Email is sent.')
