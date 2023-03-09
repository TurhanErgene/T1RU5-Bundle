import random
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta
import time

# Receiver list
receiver_list = ['example1@example.com', 'example2@example.com', 'example3@example.com']

while True:
    # Random names and unique email addresses
    names = ['John', 'Jane', 'Bob', 'Samantha']
    email_addresses = []
    for name in names:
        email = name.lower() + str(random.randint(100, 999)) + '@example.com'
        email_addresses.append(email)
    print(f'{len(email_addresses)} new email addresses generated')
    # Create draft email
    msg = MIMEText('This is a test email.')
    msg['Subject'] = 'Test Email'
    msg['From'] = 'example@example.com'
    msg['To'] = ', '.join(receiver_list)

    for email in email_addresses:
        msg['From'] = email 
        # Send email
        try:
            smtp_server = smtplib.SMTP_SSL('smtp.example.com',465)
            smtp_server.login(email,'123456789')
            smtp_server.sendmail(email, receiver_list, msg.as_string())
            print(f'Email sent successfully from {email}')
        except smtplib.SMTPException as e:
            print("Error: Unable to send email. ",e)
        finally:
            smtp_server.quit()
    
    # Wait for an hour before sending the next email
    time.sleep(3600)