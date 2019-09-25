import requests
url = 'https://raw.githubusercontent.com/dtadikam/Test/master/sample.txt'
req = requests.get(url)
print(req.text)
