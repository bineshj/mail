import smtplib, sys
import getopt
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

argv = sys.argv[1:]

try:
	opts, args = getopt.getopt(argv, 'f:u:p:')
	file = user = password = ''
	for k, v in opts:
		if k == '-f':
			file = v
		if k == '-u':
			user = v
		if k == '-p':
			password = v
	xls = pd.read_excel(file, )
	for each in xls.iterrows():
		message = MIMEMultipart()
		message['From'] = user
		mail_content = ''
		message['Subject'] = 'Progress report for subject ' + each[1]['subject']
		receiver_address = each[1]['email']
		mail_content = "Dear " + each[1]['name'] + "\n"
		mail_content = mail_content + "this is the progress report\n"
		mail_content = mail_content + 'Progress report for subject : ' + each[1]['subject'] + "\n"
		mail_content = mail_content + "Marks obtained : " + str(each[1]['marks']) \
					   + " out of " + str(each[1]['total'])
		message['To'] = each[1]['email']
		message.attach(MIMEText(mail_content, 'plain'))
		session = smtplib.SMTP('smtp.gmail.com', 587)
		session.ehlo()
		session.starttls()
		session.ehlo()
		session.login(user, password)
		text = message.as_string()
		session.sendmail(user, receiver_address, text)
		print ("Successfully report sent to " + each[1]['name'])
	print("Successfull sent mail to these email addresses..")
	print(xls['email'])
except Exception as e:
	print ("error...", e)
