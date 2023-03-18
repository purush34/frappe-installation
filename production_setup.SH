##frappe production setup:

#Step 1: 
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

#Step 2:
bench --site {site-name} enable-scheduler

#Step 4:
bench --site {site-name} set-maintenance-mode off

#Step 2: 	
sudo bench setup production {username}

#Step 3: 
bench stop

#Step 4:
bench start


# when error  occurred!
$ sudo -A systemctl restart supervisor
$ chmod -R o+rx /home/erpnext/




#####################################################################################

bench --site site1.local enable-scheduler
bench --site site1.local add-to-hosts
bench --site site1.local set-maintenance-mode off
bench --site site1.local scheduler resume
sudo snap install --classic certbot
sudo bench setup production {username}

# supervisor setup
bench setup supervisor --skip-redis

# nginx setup:
bench setup nginx
sudo ln -s `pwd`/config/nginx.conf /etc/nginx/conf.d/frappe-bench.conf


bench set-nginx-port site1.local 9001


bench setup nginx
sudo systemctl reload nginx










sudo bench setup production erpnext