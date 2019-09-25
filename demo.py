import requests
url = 'https://raw.githubusercontent.com/dtadikam/Test/master/README.md'
req = requests.get(url)
print(req.text)
