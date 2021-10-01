import datetime
import re
import smtplib
import json
import os

from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


def mailer(*args):
	with open(m_record.txt, 'a') as mr:
		for line in mr:
			if path == line.strip('/n'):
				break
			else:
				mail_data(path)


def mail_data(*args):
	
	with open('address.json') as a:
		conv_json = json.load(a)

	address = 'defaultemailidgoeshere' #default 
	url = path
	for (key, email) in conv_json.items():
		if key in url:
			address = email
			subject = path.strip('.pdf')
			from = 'vesit-tracker-account'
			mail_sender(address,subject,from,path)
			break

def mail_sender(*args):
	msg = MIMEMultipart()
	msg['From'] = from
	msg['To'] = address
	msg['subject'] = subject

	body = """

			This mail contains some test results or test time table announcements
			Either way good luck

			"""

	msg.attach(MIMEText(body,'plain'))

	filename = path
	attachment = open(path,"rb")

	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment"; filename %s" % filename)

	msg.attach(part)

	server = smtplib.SMTP('smtp.gmail.com',587)
	server.starttls()
	server.login(from,"pass")
	text = msg.as_string()
	server.sendmail(from,address, text)
	server.quit()



	







