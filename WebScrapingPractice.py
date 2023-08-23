import requests 
from bs4 import BeautifulSoup

req = requests.get("http://legislature.idaho.gov/senate/membership/")
print(req)