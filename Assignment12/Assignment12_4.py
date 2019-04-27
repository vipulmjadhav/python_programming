import psutil
import os
import time
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from sys import *
from urllib.request import urlopen


def is_connected():
		
	try:
		urlopen('http://216.58.192.142',timeout = 5)
		return True
		
	except Exception:
		return False	
		
def mailsender(filename,time):
	fromaddr = 'jadhavipul933@gmail.com'
	toaddr = 'Marvellousinfosystem@gmail.com'
	
	name,addr = toaddr.split('@')
	
	msg = MIMEMultipart()
	msg['from'] = fromaddr
	msg['to'] = toaddr
	
	body = """Hello %s , \n Please find attached documents which contains the log of running process.
	Log file is created at %s
	
	Program generated Mail.
	
	Thanks And Regards
	Vipul jadhav
	"""%(name,time)
	
	Subject = """ Process Log generated at : %s """%(time)
	msg['subject'] = Subject
	
	msg.attach(MIMEText(body,'plain'))
	
	attachment = open(filename, "rb") 

	p = MIMEBase('application', 'octet-stream') 

	p.set_payload((attachment).read()) 

	encoders.encode_base64(p) 

	bool = os.path.isabs(filename)
	
	if(bool):
		path,filen = os.path.split(filename)
		
	
	p.add_header('Content-Disposition', "attachment; filename= %s" % filen) 

	msg.attach(p)
	 
	s = smtplib.SMTP('smtp.gmail.com', 587) 

	s.starttls() 

	s.login(fromaddr, "----------") 

	text = msg.as_string() 

	s.sendmail(fromaddr, toaddr, text) 

	s.quit() 


	
def createProcessLog(dir_name):
	
	bool = os.path.isabs(dir_name)
	
	if(bool == False):
		dir_name = os.path.abspath(dir_name)
	
		
	exists = os.path.isdir(dir_name)
	
	if(exists == False):
		try:
			os.mkdir(argv[1])
		except:
			pass

	seperator = "-"*80
	log_path = os.path.join(dir_name,"process%sLog"%(time.ctime()))
	fd = open(log_path,'w')
	fd.write(seperator+"\n")
	fd.write("Current Process Running log %sLog"%(time.ctime())+"\n")
	fd.write(seperator+"\n")
	
	listprocess = []
	
	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs = ['pid','name','username'])
			pinfo['vms'] = proc.memory_info().vms/(1024*1024)
			
			listprocess.append(pinfo)
		
		except Exception as E:
			pass
		
	for i in listprocess:
		fd.write("%s\n"%i)
		
	mailsender(log_path,time.ctime())

def main():
	if(len(argv) != 2):
		print("ERROR : Invalid no of arguments\n")
		print("enter -h as argv[1] for help\n")
		print("enter -u as argv[1] for usage\n")
		exit()
	
	if(argv[1]=='-h'):
		print("HELP : The script shows all the files of extension given in argv[1]")
		exit()
		
	if(argv[1]=='-u'):
		print("USAGE : Application_name.py dir_name")
		exit()
		
	if((len(argv)) <1 or len(argv)>3):
		print("ERROR : Invalid No of Arguments!!")

	try:
		connected = is_connected()
		
		if(connected):
			print('Connected')		
			createProcessLog(argv[1])
		
		else:
			print('Not Connected')
		
	except Exception as E:
		print("Exception found : ",E)
			
		
		
if __name__ == "__main__":
	main()
