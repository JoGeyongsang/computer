import urllib.request

url = 'http://info.cern.ch'

request = urllib.request.Request(url)
response = urllib.request.urlopen( request )
print( response.read().decode() )