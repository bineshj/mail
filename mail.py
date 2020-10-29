import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail_content = "This is a sample mail"
sender_address = ""
sender_pass = ""
receiver_address = ''
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Test mail subject'   
message.attach(MIMEText(mail_content, 'plain'))
session = smtplib.SMTP('smtp.gmail.com', 587) 
session.ehlo()
session.starttls()
session.ehlo()
session.login(sender_address, sender_pass)
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
