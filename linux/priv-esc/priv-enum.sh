echo "----------SUID----------"

echo "----------SGID----------"

echo "----------Cron Jobs----------"

echo "----------Users----------"
cat /etc/passwd | cut -d ":" -f 1
