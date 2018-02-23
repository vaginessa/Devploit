#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
# author : zD4NI3L
# Tested on Kali Linux / lxle-linux
# Simple script for install Devploit

__author__ = "zD4NI3L"

import os
import pip

banner = '''
             
\033[92m 

██████╗ ███████╗██╗   ██╗██████╗ ██╗      ██████╗ ██╗████████╗
██╔══██╗██╔════╝██║   ██║██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝
██║  ██║█████╗  ██║   ██║██████╔╝██║     ██║   ██║██║   ██║   
██║  ██║██╔══╝  ╚██╗ ██╔╝██╔═══╝ ██║     ██║   ██║██║   ██║   
██████╔╝███████╗ ╚████╔╝ ██║     ███████╗╚██████╔╝██║   ██║   
╚═════╝ ╚══════╝  ╚═══╝  ╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝v2.3  
                Update Script for Devploit
           Created by zD4NI3L

'''
print banner

content = """
#!/bin/bash

cd /usr/share/Devploit
python Devploit "$@"
"""

def main():
	if os.name != "nt":
		if os.getuid() == 0:
			os.system("git clone http://github.com/zD4NI3L/Devploit /usr/share/Devploit")
			for i in ["requests", "bs4"]:
				pip.main(["install", i])
			
			file = open("/usr/bin/Devploit", "w")
			file.write(content)
			file.close()
			
			os.system("chmod +x /usr/bin/Devploit")

			print "\n\n[+] Update finished, Run \033[91m'Devploit'\033[92m In Terminal!"
		else:
			print "Run as root!"
	else:
		print "This script doesn't work on Windows!"

if __name__ == "__main__":
	main()
