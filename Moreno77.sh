clear
echo "\n\n\n\033[1;32m      +---------[Spamer by Moreno77]----------+"
python .py
sleep 1
echo "\033[1;32m 1. Spam Grab\n 2. Spam Tokopedia\n 3. Spam OYO\n 4. Spam TRI"
echo "\033[1;32m 5. Spam Email BPJS
echo " 00. Update Script"
read -p " [?] Input => " pil;
case $pil in
1) cd data
python SMS.py
exit
;;
2) cd data
php Call.php
exit
;;
3) cd data
python OYO.py
exit
;;
4) cd data
python TRI.py
exit
;;
00) echo "[!] Proses Update Script......"
sleep 2 
cd $HOME
rm -rf Spam77
git clone https://github.com/DarkCurut08/Spam77
cd Spam77
sh Moreno77.sh
exit
;;
esac
done
done

