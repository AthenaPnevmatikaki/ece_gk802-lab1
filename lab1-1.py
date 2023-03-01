import requests  # εισαγωγή της βιβλιοθήκης

url = 'http://python.org/'

with requests.get(url) as response:  # το αντικείμενο response
    headers = response.headers
    for k, v in headers.items():
        print(k +": "+ v)
    print("Λογισμικό web server:", headers["Server"])

    if response.cookies:
        print("Η σελίδα χρησιμοποιεί cookies.")
    else:
        print("Η σελδίδα δεν χρησιμοποιεί cookies.")
