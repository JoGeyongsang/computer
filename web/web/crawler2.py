import requests

url = 'http://info.cern.ch'

response = requests.get(url)
print( response.text )