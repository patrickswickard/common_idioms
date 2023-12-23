"""More complex requests demo"""
import requests

request_url = 'https://www.instagram.com/api/v1/users/web_profile_info/?username=vintage_bmore_graffiti'

#headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0'}
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0'}

response = requests.get(request_url, headers=headers)

print(response.text)
