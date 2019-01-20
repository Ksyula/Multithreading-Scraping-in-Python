import sqlite3 as lite

con = lite.connect('Coins.db')
def db_cleaner():
    with con:
        cur = con.cursor()
        cur.execute("DELETE FROM Prices;")
    con.commit()

db_cleaner()