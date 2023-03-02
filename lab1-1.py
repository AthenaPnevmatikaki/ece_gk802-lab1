import requests
from datetime import datetime

url = input("Enter url: ")

with requests.get(url) as response:
    headers = response.headers
    print("\nAll headers:")
    for k, v in headers.items():
        print(k +": "+ v)
    
    print("\nWeb server Software:", headers["Server"])

    if response.cookies:
        print("\nThis web page uses cookies:")
        for cookie in response.cookies:
            expires = cookie.expires
            if expires != None:
                valid = datetime.fromtimestamp(cookie.expires) - datetime.now()
                print("Cookie Name:", cookie.name, ", will be valid for:", valid)
            else:
                print("Cookie Name:", cookie.name, ", has no expiration date.")
    else:
        print("\nThis web page does not use cookies.")
    print("")
