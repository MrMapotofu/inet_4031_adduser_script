#!/usr/bin/python
import os
import re
import sys

def main():
	for line in sys.stdin:

		Add  a line of code here. Use re.match and create a regular expression to 
check for the presence of a # at the start of a line.We want to skip any 
lines in the file that starts with a hashtag: #
		
		Create your regex (I suggest re.match) and save the result in a variable 
named “match”

match = <your code goes here> 

		fields = line.strip().split(':') #strip any whitespace and split into 
                                                #into an array

		if match or len(fields) != 5: #explain what this is checking for and why
			continue  #the continue here is for the FOR loop. So if the line
				   #starts with a # or does NOT have five fields, we skip it
		
username = fields[0]
		password = fields[1]

		gecos    = "%s %s,,," % (fields[3],fields[2])

		groups   = fields[4].split(',') #add comment - what does this do and why?

		print "==> Creating account for %s..." % (username))
		cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
		#print cmd
		os.system(cmd)  #what does this line do?
		print "==> Setting the password for %s..." % (username)
		cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
		#print cmd
		os.system(cmd)
		for group in groups: #add comment - what is this FOR loop doing and why?
			if group != '-':
			    print "==> Assigning %s to the %s group..." % (username,group)
			    cmd = "/usr/sbin/adduser %s %s" % (username,group)
			    #print cmd
			    os.system(cmd)


if __name__ == '__main__':
	main()

