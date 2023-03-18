asdf123
Erp@123



SELECT table_schema AS "_a84d87efcf56aea8", SUM(data_length + index_length) / 1024 / 1024 AS "Size (MB)" FROM information_schema.TABLES GROUP BY table_schema



bench migrate
sudo service supervisor start
sudo service nginx start

# after production mode still updating
bench --site erp_next.com set-maintenance-mode off


#  Redis is now ready to exit, bye bye...

# Address already in use:
sudo supervisorctl stop all



# backup files from production:
Config  : ./erp_next.com/private/backups/erp_next_com-site_config_backup.json 94.0B
Database: ./erp_next.com/private/backups/erp_next_com-database.sql.gz         1.0MiB

# after production CSS not working
$ bench clear-website-cache



#error: <class ‘PermissionError’>, [Errno 13] Permission denied: file: /usr/lib/python3/dist-packages/supervisor/xmlrpc.py line: 560
$ sudo service supervisor stop
$ sudo service nginx stop
$ bench start


# regenerate production config files
bench setup socketio
bench setup supervisor
bench setup nginx
bench setup redis
sudo service nginx reload
sudo supervisorctl reload



# redis ready to exis bye...
sudo supervisorctl restart all

# 127.0.0.1:11000: bind: Address already in use
sudo supervisorctl stop all 

# Still showing Updating issue
bench set-config maintenance_mode 0


# ERROR: Failed building wheel for tesserocr facing this issue while installing erpnext_ocr
sudo apt-get install tesseract-ocr libtesseract-dev libleptonica-dev pkg-config
