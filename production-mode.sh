set -e
cd ~
#Go to file path
cd frappe-bench
#Find username
me=$(whoami)
#Froduction setup
sudo bench setup production ${me} --yes
#Update the the production mode
sudo apt update
#This file to run every 10 minutes. but, it requires only one time so this file removed
sudo rm -rf /home/production-mode.sh





step1: 
$ export LC_ALL=C.UTF-8
$ export LANG=C.UTF-8

step2:
bench --site {site-name} enable-scheduler

step3:
bench setup nginx
bench setup supervisor

step4:
bench --site {site-name} set-maintenance-mode off

step5:
sudo bench setup production {username}
optional
sudo bench setup production {username} --yes

step6:
bench stop
and
bench start

step6:
sudo systemctl reload nginx

finally:
sudo supervisorctl status

should be run all supervisor services.



When you are facing any errors while setup production mode.
$ sudo -A systemctl restart supervisor
$ chmod -R o+rx /home/erpnext/
