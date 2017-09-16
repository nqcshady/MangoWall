#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, time
os.system('clear')

default_files = "/var/www/html"
username = "admin"
passer = "toor"

def main():
	print "Requires: Apache2, tcpdump, php\n Tested on: Debian,Ubuntu"
	user = raw_input('[user: ' + username + ']: ') or username
	password = raw_input('[pass: ' + passer + ']: ') or passer
	mkdir_files = raw_input('[install: ' + default_files + ']: ') or default_files
	os.system('mkdir %s' % (mkdir_files))
	os.system('mkdir %s/logs' % (mkdir_files))

	login_file = """<!DOCTYPE html>
<title>MangoWall - Login</title>

<?php defined('DS') OR die('No direct access allowed.');

$users = array(
 "%s" => "%s"
);

if(isset($_GET['logout'])) {
    $_SESSION['username'] = '';
    header('Location:  ' . $_SERVER['PHP_SELF']);
}

if(isset($_POST['username'])) {
    if($users[$_POST['username']] !== NULL && $users[$_POST['username']] == $_POST['password']) {
  $_SESSION['username'] = $_POST['username'];
  header('Location:  ' . $_SERVER['PHP_SELF']);
    }else {
  echo "<p>error logging in</p>";
    }
}

	      echo '<form method="post" action="'.SELF.'">
              <p><label for="username">Username:</label> <input type="text" id="username" name="username" value="" /></p>
              <p><label for="password">Password:</label> <input type="password" id="password" name="password" value="" /></p>
              <p><input type="submit" name="submit" value="Login" class="button dark"/></p>
              </form>
              </div>
              </article>';
              exit; 
              ?>
  </body>
</html>

	""" % (user,password)
	login = open('login.php','w')
	login.write(login_file)
	login.close()
	console_file = """#!/bin/bash

if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root :("
    echo "Please try running this command again as root user"
    exit 1
fi


SYNCREC=`netstat -n -p | grep SYN_REC | sort -u`
NUMBERCONN=`netstat -ntu | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -n|wc -l`
ESTASH=`netstat -plan|grep :80|awk {'print $5'}|cut -d: -f 1|sort|uniq -c|sort -nk 1`

function printMessage() {
    echo -e "\e[1;37m# $1\033[0m"
}

function tcpdump() {
  timeout 10s tcpdump -n udp > """ + mkdir_files + """/udp.log
  timeout 10s tcpdump -n tcp |grep S > """ + mkdir_files + """/syn.log
  timeout 10s tcpdump -n icmp > """ + mkdir_files + """/icmp.log
}

function netstats() {
  netstat -n|grep :80|cut -c 45-|cut -f 1 -d ':'|sort|uniq -c|sort -nr|more > """ + mkdir_files + """/topip.log
  netstat -an | grep :80 | sort > """ + mkdir_files + """/active-connections.log
}

clear

echo ""
echo "---------------------------------------------------------------"
echo "Server started"
echo "All log files should be listed under """ + mkdir_files + """/logs"
echo "You can exit console if you want however logs will close!"
echo "reopen console: ./console"
echo "---------------------------------------------------------------"
echo ""

tcpdump
netstats
	"""
	console = open('console','w')
	console.write(console_file)
	console.close()
	os.system('cp -r * %s/' % (mkdir_files))
	os.system('service apache2 restart')


def banner():
	print """___  ___                        _    _       _ _ 
|  \/  |                       | |  | |     | | |
| .  . | __ _ _ __   __ _  ___ | |  | | __ _| | |
| |\/| |/ _` | '_ \ / _` |/ _ \| |/\| |/ _` | | |
| |  | | (_| | | | | (_| | (_) \  /\  / (_| | | |
\_|  |_/\__,_|_| |_|\__, |\___/ \/  \/ \__,_|_|_|
                     __/ |                       
                    |___/ """


def console():
	yesr = "yes"
	yen = raw_input('[start console?: ' + yesr + ']: ') or yesr
	if yen == "yes":
		os.system('chmod +x console; ./console')
	else:
		print "Finished, console was not executed however you can visit webpage: localhost:%s" % (port)

banner()
main()
console()
