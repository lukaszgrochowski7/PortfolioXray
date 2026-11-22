import sqlite3



def connect(path):
    return sqlite3.connect(path)

def init_db(conn):
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS holdings (
                    id INTEGER PRIMARY KEY,
                    ticker TEXT NOT NULL,
                    quantity REAL NOT NULL,
                    buy_price REAL NOT NULL,
                    buy_date TEXT NOT NULL
                    )
    """)
    conn.commit()

def add_holding(conn, holding):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO holdings VALUES(?, ?, ?, ?)",
                   (holding.ticker, holding.quantity, holding.buy_price, holding.buy_date)
    )


    conn.commit()