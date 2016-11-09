#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Author: Adel Messaoudi
#
#
#
import getpass
import smtplib, os, sys
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders

# for hotmail change  smtp.gmail.com to smtp.live.com
def send_mail( send_from, pwd, send_to, subject, text, files=[], server="smtp.gmail.com", port=587, attach=True):
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime = True)
    msg['Subject'] = subject
    if attach:
    	msg.attach( MIMEText(text) )
    	for f in files:
        	part = MIMEBase('application', "octet-stream")
        	part.set_payload( open(f,"rb").read() )
        	encoders.encode_base64(part)
        	part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(os.path.basename(f)))
        	msg.attach(part)

    smtp = smtplib.SMTP(server, port)
    smtp.starttls()
    smtp.login(send_from, pwd)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()

if __name__ == '__main__':
	try:
		if len(sys.argv) != 3 and len(sys.argv) != 4:
			print "Usage:\n python "+sys.argv[0]+" Your_Email_Address txt_file_TO_send_email Attached_Filename"
			print "(P.S: this works only for gmail accounts with enabled option for less secure apps)"
			print "To activate it check this link: https://www.google.com/settings/security/lesssecureapps "
			exit(0)
		sender = sys.argv[1]
		pwd = getpass.getpass('enter your email Password:')


		# Edit the Subject and the text as you want:
		subject = "Hello, this is a test bulk email"

		text="""
		Hey,\n
		\tThis is just a test email , TO BE Modified .\n
		\n\t Best Regards,
		"""

		emails_list = [line.rstrip('\n') for line in open(sys.argv[2]) if line.rstrip('\n') ]

		if len(sys.argv)==3:
			print "no attached file ! (Ctrl + C) to quit"
			attach=False
		else:
			attach = True
			file = [sys.argv[3],]
	#       file = ['/home/adel/MSD_Adel-Last.pdf',]
	
		for email in emails_list:
			try:
				send_mail( send_from=sender, pwd=pwd, send_to=email, subject=subject, text=text, files=file, server="smtp.gmail.com", port=587, attach=attach)
				print 'email sent successfully to '+email
			except:
				print 'Sorry, we were not able to send email to '+email+', please check again your email and password'
	except KeyboardInterrupt:
		print "\nScript was stopped\nGood Bye" 
		sys.exit()
