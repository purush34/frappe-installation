# backup existing project
$ bench --site {site-name} backup

# RESTORE:

# Method 1: Restore a site with files
$ bench --site {site} restore {path/to/database/file} --with-public-files {path/to/public/archive} --with-private-files {path/to/private/archive}

# Method 2: Bypass DBMS root interactive prompt by passing values in options
$ bench --site {site} restore {path/to/database/file} --db-root-username {db-user} --db-root-password {db-pass}

# Method 3: Specify new app to install after site restore
$ bench --site {site} restore {path/to/database/file} --install-app {app}

# Method 4: Specify custom database name for the restored site
$ bench --site {site} restore {path/to/database/file} --db-name {custom-db-name}

# Method 5: Reset the admin password for the restored site
$ bench --site {site} restore {path/to/database/file} --admin-password {admin-pass}



Example1:

Step1:
	Existing site inside run bench migrate command once.
	$ bench migrate
	
Step2:
	Take a backup inside the existing site.
	$ bench backup
	
Step3:
	Backup Database file and site-backup file both are copy to restore required machine.
	$ scp {db-file-path} remoteuser@remoteip:{destination-path}
	
Step4:
	Login to Restored required machine.
	$ ssh username@remoteip
	
Step5:
	Create new frappe site on restore required machine.
	$ bench new-site {site-name}

Step6:
	Get all required apps.
	$ bench get-app {appname}
	
Step7:
	Restore the copied database file.
	$ bench --site {new-site-name} restore {database/file-path}
	
Step8:
	Change encryption key backup file to new-site's "site-config.json" file.
	$ cat site-config.json
	{
		"encryption_key": "####################"
	}
	
Step9:
	Update database schemas
	$ bench migrate
	
Step10:
	Start bench
	$ bench start
	
