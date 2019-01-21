import sqlite3 as lite
import requests
from bs4 import BeautifulSoup
from itertools import cycle

con = lite.connect('Coins.db')

def parse_and_write(coins, proxies):
    proxy_pool = cycle(proxies)
    con = lite.connect('Coins.db')
    for coin in coins:
        url = 'https://coinmarketcap.com/currencies/' + coin
        print(url)
        price = 0.0
        for i in range(0, len(proxies)):
            if(price == 0.0):
                proxy = next(proxy_pool)
                print("Request #%d" % i)
                try:
                    coin_page = requests.get(url, proxies={"http": proxy, "https": proxy})
                    soup = BeautifulSoup(coin_page.content, "html.parser")
                    price = float(soup.find(id="quote_price").span.text)
                except:
                    # Most free proxies will often get connection errors.
                    print("Skipping. Connnection error")
                    pass
            else:
                break
        with con:
            cur = con.cursor()
            cur.execute("INSERT INTO Prices (Coin, Price) VALUES ('" + str(coin) + "', '" + str(price) + "');")
        con.commit()
