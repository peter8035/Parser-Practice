from bs4 import BeautifulSoup
from bs4 import NavigableString
import csv
import urllib3
import certifi

http = urllib3.PoolManager(
    cert_reqs = 'CERT_REQUIRED',
    ca_certs = certifi.where()
)
source = 'http://www.goodreads.com/quotes'
resp = http.request('GET',source)

#print(resp.status)
#print(resp.data.decode('utf-8'))

soup = BeautifulSoup(resp.data,features="lxml")
#print(soup.prettify())

# identifying tags
# for tag in soup.find_all(True):
#     print(tag.name)

# i can get names and quotes, but for quotes with <span id= and <script type=, i also get useless stuff
# for div in soup.find_all('div', class_='quoteText'):
#     print(div.text)
