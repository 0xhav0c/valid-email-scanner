#!/usr/bin/env python3
from verify_email import verify_email
import time
import datetime
import os
from colorama import Fore

########### COLOR ############
fr = Fore.RED
fc = Fore.CYAN
fw = Fore.WHITE
fg = Fore.GREEN
##############################
now = datetime.datetime.now().isoformat(sep=" ", timespec="seconds")

print(r"""
    █████                █████                               █████            
  ███░░░███             ░░███                              ███░░░███          
 ███   ░░███ █████ █████ ░███████    ██████   █████ █████ ███   ░░███  ██████ 
░███    ░███░░███ ░░███  ░███░░███  ░░░░░███ ░░███ ░░███ ░███    ░███ ███░░███
░███    ░███ ░░░█████░   ░███ ░███   ███████  ░███  ░███ ░███    ░███░███ ░░░ 
░░███   ███   ███░░░███  ░███ ░███  ███░░███  ░░███ ███  ░░███   ███ ░███  ███
 ░░░█████░   █████ █████ ████ █████░░████████  ░░█████    ░░░█████░  ░░██████ 
   ░░░░░░   ░░░░░ ░░░░░ ░░░░ ░░░░░  ░░░░░░░░    ░░░░░       ░░░░░░    ░░░░░░  
 """)
print(fc + "Valid Email Address Scanner v1 @Powered ßy 0xhav0c" + fw)
print(fw + "[" + fg + "*" + fw + "] STARTED AT: " + fg + str(now) + fw)
print("----------------------------------")

file_path = input('Enter mail address list (TXT) path: ')
print(file_path)

if os.path.exists(file_path):
    print(fc + 'The file exists'+ fw)
    print("----------------------------------")

    with open(file_path, 'r') as f:
        emails = f.readlines()
else:
    print(fr + 'The specified file does NOT exist' + fw)
    print('----------------------------------')


def time_it(func, *args, **kwargs):
    start = time.time()
    func(*args, **kwargs)
    print('----------------------------------')
    print(fc +'Scanning Take:', time.strftime("%H:%M:%S", time.gmtime(time.time() - start)), 'seconds' + fw)

def checkmail():
    for email in emails:
        if verify_email(email.rstrip()):
            print(
                fc + "[" + fc + "✓" + fc + "] " + fg + email.rstrip() + fw + " .... " + fg + " Valid Address " + fw + "")
        else:
            print(
                fc + "[" + fc + "x" + fc + "] " + fr + email.rstrip() + fw + " .... " + fr + " Not Valid " + fw + "" + fw)


print(fc + 'Scanning Mail Address' + fw)
print('----------------------------------')
time_it(checkmail)