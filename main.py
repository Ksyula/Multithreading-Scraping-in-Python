import re
import requests
from bs4 import BeautifulSoup
from threading import Thread
from proxy_list import get_proxies
from parse_and_write import parse_and_write
from clean_db import db_cleaner
url = 'https://coinmarketcap.com/'

# query the website and return the html to the variable ‘page’
page = requests.get(url)
# parse the html content
soup = BeautifulSoup(page.content, "html.parser")

coins = []

# Extract the list of Top-100 coins through parsing page’s <a> tags. (Working with <a> tags here are for exercising purpose)
for link in soup.find_all('a'):
    # Extracting all meaningful site internal links URLs:
    if (link.get('href') != None and link.get('href') != '/' and link.get('href') != '#'):
        #Extract all coin names from internal links:
        if (re.match('^/currencies' , link.get('href'))):
            coin = re.search('/currencies/(.+?)/', link.get('href')).group(1)
            if(coin not in coins and coin != 'volume'):
                coins.append(coin)

#print("\n".join(coins))
proxies = get_proxies()
#print("\n".join(proxies))


threads = []
# Create new threads
t1 = Thread(target=parse_and_write, args=(coins[0:25], proxies))
t2 = Thread(target=parse_and_write, args=(coins[25:50], proxies))
t3 = Thread(target=parse_and_write, args=(coins[50:75], proxies))
t4 = Thread(target=parse_and_write, args=(coins[75:100], proxies))
# Start new Threads
t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

# Add threads to thread list
threads.append(t1)
threads.append(t2)
threads.append(t3)
threads.append(t4)

# Wait for all threads to complete
for t in threads:
    t.join()
print("Exiting Main Thread")
