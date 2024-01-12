import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

smtp_server = ''
smtp_port = 587
sender_email = os.getenv('EMAIL_USER')
receiver_email = 'recipient@example.com'
password = os.getenv('EMAIL_PASSWORD')

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'Sample Email Subject'

body = 'This is a sample email message.'
message.attach(MIMEText(body, 'plain'))

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())