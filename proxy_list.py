from bs4 import BeautifulSoup
import requests

# Scrape to extract a set of available elite proxies from free-proxy-list.net
def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    proxies = set()
    for i in soup.tbody.find_all('tr')[:30]:
        if (i.find_all('td')[6].text == "yes" and i.find_all('td')[4].text == "elite proxy"):
            #Grabbing IP and corresponding PORT
            proxy = i.find_all('td')[0].text + ":" + i.find_all('td')[1].text
            # list of 10 proxy addresses
            if (len(proxies) < 10):
                proxies.add(proxy)
    return proxies


