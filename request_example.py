import requests

request_url = 'http://www.google.com'

result = requests.get(request_url).text

print(result)
