#!/usr/bin/python

import subprocess
import paramiko
import time
import datetime as dt
import os



def getCurrentTime():
	return dt.datetime.now().strftime("%d_%m_%Y_%H.%M.%S")

def getFileName(name):
	return name + '_' + getCurrentTime()
		
def ExecutionTermination():
	while 1:
		d = raw_input('enter e to exit :  ')
		if d is not 'e':
			continue
		else:
			os._exit(0)

def RunRGTestScripts(intial_wait, script_list, logDirectory, repeat_count=1 ):

	print 'waiting about {} seconds before start running test scripts'.format(intial_wait)
	time.sleep(intial_wait)

	count = repeat_count
	loop = 1
	while loop <= count :

		os.chdir(logDirectory)
		for test_detail in script_list:
			for feature_name, script_path in test_detail.items():
				name_prefix = getFileName(feature_name)
				file_path_with_time_stamp = '{0}{1}'.format(logDirectory, name_prefix)
				#pybot_options = 'pybot -l {0}{1}.html -r {0}{1}_report.html -o {0}{1}_output.xml -L TRACE '.format(logDirectory, name_prefix)
				pybot_options = 'pybot -l {0}.html -r {0}_report.html -o {0}_output.xml -L TRACE '.format(file_path_with_time_stamp)
				cmd = pybot_options + script_path
				print cmd
				data = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
				print data.stdout.read()
				rmcmd1 = 'del {0}_report.html'.format(file_path_with_time_stamp)
				rmcmd2 = 'del {0}_output.xml'.format(file_path_with_time_stamp)
				data = subprocess.Popen(rmcmd1, shell=True, stdout=subprocess.PIPE)
				data = subprocess.Popen(rmcmd2, shell=True, stdout=subprocess.PIPE)
				time.sleep(1*60)
				
		loop = loop + 1
