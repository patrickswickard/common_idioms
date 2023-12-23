"""Simple requests demo"""
import requests

request_url = 'https://www.instagram.com/api/v1/users/web_profile_info/?username=vintage_bmore_graffiti'

result = requests.get(request_url).text

print(result)
