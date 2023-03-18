# It requires python3.10

# upgrade v13 to v14
bench migrate
bench switch-to-branch version-14 --upgrade
update --reset
bench restart
