import subprocess
from tqdm import tqdm
import time 
import os


project_details="""

####################---Project Details---###################
 _____________________________________________________________________________
|                                                                             |
| # Project Path: /home/username/frappe-framework                             |
|                                                                             |
| # Site Path:  /home/username/frappe-framework/sites/                        |
|                                                                             |
| # MySQL root user Password:  Frappe@123                                        |
|                                                                             |
| # Application URL: http://localhost:8000                                    |
|                                                                             |
| # Application Username:  Administrator                                      |
|                                                                             |
| # Any Query mailto: ranjithks@am.amrita.edu                                 |
|_____________________________________________________________________________|

"""
class colors:
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'

    class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'
        white = '\033[38;5;231m'

    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'
        white = '\033[38;5;231m'


bg_color = colors.bg
font_color = colors.fg

def config():
    os.system("sudo npm install -g yarn")
    os.system("sudo -H pip3 install frappe-bench")
    os.system("sudo service mysql restart")
    print("-",  font_color.green,"Got a Frappe Files!", colors.reset)


def install_v14():
    os.system("sudo rm -rf /etc/apt/sources.list.d/nodesource.list")
    os.system("sudo curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -")
    os.system("sudo apt-get install -y nodejs")
    config()

def local_setup():
    os.system("sudo timedatectl set-timezone 'Asia/Kolkata'")
    os.system("sudo apt-get -y update")


def dependency():
    print(bg_color.green,colors.bold, font_color.black, "+",colors.bold, font_color.white, "Installing Dependencies...!", colors.reset)
    os.system("sudo apt-get install -y git python3-dev python3.10-venv python3-setuptools xvfb libfontconfig wkhtmltopdf python3-pip virtualenv software-properties-common redis-server curl")
    time.sleep(2)
    print("-",  font_color.green,"Dependencies Installed!", colors.reset)


def db_setup():
    print("-",  font_color.yellow,"Database Configuration!\n", colors.reset)
    def only_setup():
        os.system("sudo chmod 777 /etc/mysql/my.cnf")
        for i in tqdm (range (100),desc="Configuring...!", ncols=75):
            time.sleep(0.02)
        mysql_content = """
[mysqld]
character-set-client-handshake = FALSE
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci
[mysql]
default-character-set = utf8mb4
"""
        mysql_config_file= open("/etc/mysql/my.cnf","a")
        mysql_config_file.write(mysql_content)
        os.system("sudo chmod 644 /etc/mysql/my.cnf")

    def db_install():
        os.system("sudo apt-get install -y mariadb-server")
        time.sleep(0.5)
        print("\nHIT [ENTER]\n")
        set_dbpass = """
sudo mysql -uroot -p << EOF
flush privileges;
alter user root@localhost identified by 'Frappe@123';
flush privileges;
EOF
""" 
        os.system(set_dbpass)
        only_setup()

    db_menu = {
        1: "Install and Setup",    
        2: "Only Setup Database"
    }
    for key in db_menu.keys():
        print (key, '--', db_menu[key] )
    
    option = ''
    while(True): 
        try:
            option = int(input('Enter Setup choice: '))
        except (NameError, ValueError) as error:
            print("\nPlease enter valid key!\n")
        except KeyboardInterrupt:
            print("\nUser Exited..!\n")
            exit()
        #Check what choice was entered and act accordingly
        if option == 1:
            db_install()
            for i in tqdm (range (100),desc="Setting Password...!", ncols=75):
                time.sleep(0.02)
            print("Database Password: Frappe@123")
            print("-",  font_color.green,"Database Setup Completed!", colors.reset)
        if option == 2:
            only_setup()
        break


def get_frappe():
    print(bg_color.green,colors.bold, font_color.black, "+",colors.bold, font_color.white, "Getting Frappe...!", colors.reset)
    get_version= subprocess.getoutput("node --version")

    node = get_version[1:3]
    node = get_version[1:3]
    try:
        node_version = int(node)
        if node_version <= "14":
            install_v14()
        else:
            config()
    except:
        install_v14()

def install_frappe():

    print(bg_color.green,colors.bold, font_color.black, "+",colors.bold, font_color.white, "Frappe Installing...!", colors.reset)
    users = subprocess.getoutput("who")
    username = users.split()
    os.chdir(f'/home/{username[0]}/')
    os.system("bench init frappe-framework --frappe-branch version-14")
    os.chdir(f"/home/{username[0]}/frappe-framework")
    os.system("bench new-site frappe-site.com")
    os.system("bench use frappe-site.com")
    with open(f"/home/{username[0]}/frappe-details.txt","w") as final_report:
        final_report.close()
        pass
    with open(f"/home/{username[0]}/frappe-details.txt","w") as final_reports:
        final_reports.write(project_details)
        final_reports.close()

    print("+++",  font_color.green,"Project file detail: /home/frappe-details.txt", colors.reset)
    print("-",  font_color.green,"Frappe Installed!\n", colors.reset)
    print("Enter the path [$ cd ~]  && HIT [$ bench start]")
    for i in tqdm (range (100),desc="Finalizing...!", ncols=75):
        time.sleep(0.5)
    





def complete_install():
    print(bg_color.green,colors.bold, font_color.black, "+",colors.bold, font_color.white, "Initiating Complete Installation...!", colors.reset)
    local_setup()
    dependency()
    db_setup()
    get_frappe()
    install_frappe()

def collecting():
    for i in tqdm (range (100),desc=desc, ncols=75):
        time.sleep(0.5)

def introduction():
    print("""
    ███████╗  ██████╗░  ░█████╗░  ██████╗░  ██████╗░  ███████╗
    ██╔════╝  ██╔══██╗  ██╔══██╗  ██╔══██╗  ██╔══██╗  ██╔════╝
    █████╗░░  ██████╔╝  ███████║  ██████╔╝  ██████╔╝  █████╗░░
    ██╔══╝░░  ██╔══██╗  ██╔══██║  ██╔═══╝░  ██╔═══╝░  ██╔══╝░░
    ██║░░░░░  ██║░░██║  ██║░░██║  ██║░░░░░  ██║░░░░░  ███████╗
    ╚═╝░░░░░  ╚═╝░░╚═╝  ╚═╝░░╚═╝  ╚═╝░░░░░  ╚═╝░░░░░  ╚══════╝
    """)

    print(colors.bold,"""
            █ █▄░█ █▀ ▀█▀ ▄▀█ █░░ █░░ ▄▀█ ▀█▀ █ █▀█ █▄░█
            █ █░▀█ ▄█ ░█░ █▀█ █▄▄ █▄▄ █▀█ ░█░ █ █▄█ █░▀█
    """, colors.reset)

    print(colors.bold,font_color.green,f"""

    ╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╭╮╱╱╭╮ CREATED BY,
    ┃╭━╮┃╱╱╱╱╱╱╱╱╱╭╮╱╱╭╯╰╮┃┃╱╱┃┃ 
    ┃╰━╯┃╭━━╮╭━╮╱╱╰╯╭╮╰╮╭╯┃╰━╮┃┃╭╮╭╮╭╮╭╮╭╮╭━━╮╭━╮
    ┃╭╮╭╯┃╭╮┃┃╭╮╮╱╭╮┣┫╱┃┃╱┃╭╮┃┃╰╯╯┃┃┃┃┃╰╯┃┃╭╮┃┃╭╯
    ┃┃┃╰╮┃╭╮┃┃┃┃┃╱┃┃┃┃╱┃╰╮┃┃┃┃┃╭╮╮┃╰╯┃┃┃┃┃┃╭╮┃┃┃
    ╰╯╰━╯╰╯╰╯╰╯╰╯╱┃┃╰╯╱╰━╯╰╯╰╯╰╯╰╯╰━━╯╰┻┻╯╰╯╰╯╰╯
    ╱╱╱╱╱╱╱╱╱╱╱╱╱╭╯┃   {font_color.red}      SUPPORT: {colors.reset} {font_color.green}
    ╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯ {colors.reset}{font_color.red} ranjithks@am.amrita.edu {colors.reset}
    """,colors.reset)
    print("\n")

try:
    menu_options = {
        0: "Complete Installation",    
        1: "local_setup",
        2: "Dependency Installation",
        3: "Database setup",
        4: "Get Frappe",
        5: "Install Frappe",
        6: "Exit"
    }
    def print_menu():
        for key in menu_options.keys():
            print (key, '--', menu_options[key] )

    username = subprocess.getoutput("whoami")

    if (username != 'root'):
        introduction()
        desc = "Collecting Menu's...!"
        collecting()
        print_menu() 
    else:
        print(F"""{colors.bold}{font_color.red}PLEASE RUN THIS SCRIPT AS A {colors.reset}
        {font_color.purple}        
        █▀ █░█ █▀▄ █▀█   █░█ █▀ █▀▀ █▀█
        ▄█ █▄█ █▄▀ █▄█   █▄█ ▄█ ██▄ █▀▄
        {colors.reset}""")
        exit()

    if __name__=='__main__':
        option = ''
        while(True): 
            try:
                option = int(input('Enter your choice: '))
            except (NameError, ValueError) as error:
                print("\nPlease enter valid key!\n")
            except KeyboardInterrupt:
                print("\nUser Exited..!\n")
                exit()
            #Check what choice was entered and act accordingly
            if option == 0:
                complete_install()
            if option == 1:
                local_setup()
            elif option == 2:
                dependency()
            elif option == 3:
                db_setup()
            elif option == 4:
                get_frappe()
            elif option == 5:
                install_frappe()
            elif option == 6:
                print('Thanks message before exiting')
                exit()


except KeyboardInterrupt:
    print("\nUser Exited..!\n")
    exit()
