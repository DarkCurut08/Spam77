clear
echo "\n\n\n\033[1;32m      +---------[Spamer by Moreno77]----------+"
python .py
sleep 1
echo "033[1;32m 1. Spam SMS\n 2. Spam Call"
echo " 3. Update Script"
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
3) echo "[!] Proses Update Script......"
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

