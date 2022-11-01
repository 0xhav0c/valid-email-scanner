# Valid Email Address Scanner
This tool checks an existing mailing address list to see if these mailing addresses exist.
# Installing from Source

```console
git clone https://github.com/0xhav0c/valid-email-scanner.git
cd valid-email-scanner
pip 3 install -r requirements.txt
```

# Tutorial
```console
root@kali:~/tools/valid-email-scanner# python3 mail-validation-scanner.py 

    █████                █████                               █████            
  ███░░░███             ░░███                              ███░░░███          
 ███   ░░███ █████ █████ ░███████    ██████   █████ █████ ███   ░░███  ██████ 
░███    ░███░░███ ░░███  ░███░░███  ░░░░░███ ░░███ ░░███ ░███    ░███ ███░░███
░███    ░███ ░░░█████░   ░███ ░███   ███████  ░███  ░███ ░███    ░███░███ ░░░ 
░░███   ███   ███░░░███  ░███ ░███  ███░░███  ░░███ ███  ░░███   ███ ░███  ███
 ░░░█████░   █████ █████ ████ █████░░████████  ░░█████    ░░░█████░  ░░██████ 
   ░░░░░░   ░░░░░ ░░░░░ ░░░░ ░░░░░  ░░░░░░░░    ░░░░░       ░░░░░░    ░░░░░░  
 
Valid Email Address Scanner v1 @Powered ßy 0xhav0c
[*] STARTED AT: 2022-11-01 17:10:50
----------------------------------
Enter mail address list (TXT) path: /root/tools/valid-email-scanner/list.txt
/root/tools/valid-email-scanner/list.txt
The file exists
----------------------------------
Scanning Mail Address
----------------------------------
[✓] press@tesla.com ....  Valid Address 
[x] for-example-non-exist@tesla.com ....  Not Valid 
[x] asilhan@tesla.com ....  Not Valid 
[x] 0xhav0c@tesla.com ....  Not Valid 
[x] etc-mail@tesla.com ....  Not Valid 
[✓] china-press@tesla.com ....  Valid Address 
[✓] ServiceHelpNA@tesla.com ....  Valid Address 
[✓] hongkong@tesla.com ....  Valid Address 
[✓] macau@tesla.com ....  Valid Address 
[✓] japan@tesla.com ....  Valid Address 
[✓] southkorea@tesla.com ....  Valid Address 
[✓] australia@tesla.com ....  Valid Address 
[✓] ServiceHelpAU@tesla.com ....  Valid Address 
[✓] taiwan@tesla.com ....  Valid Address 
[✓] Supercharger-EU@tesla.com ....  Valid Address 
[✓] legal@tesla.com ....  Valid Address 
[✓] vulnerability@tesla.com ....  Valid Address 
[✓] supercharger@tesla.com ....  Valid Address 
[✓] ChargingInstallation-EUR@tesla.com ....  Valid Address 
----------------------------------
Scanning Take: 00:00:18 seconds
```

# Thanks To
Thanks to [@kakshay21](https://github.com/kakshay21) for creating [this](https://pypi.org/project/verify-email/) library.