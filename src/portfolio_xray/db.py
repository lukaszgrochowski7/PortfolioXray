import sqlite3
from pathlib import Path
import pandas as pd


DB_PATH = Path(__file__).parent.parent / "portfolio.db"   # zawsze src/portfolio.db


def connect(path=DB_PATH):
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
    cursor.execute("INSERT INTO holdings (ticker, quantity, buy_price, buy_date) VALUES(?, ?, ?, ?)",
                   (holding.ticker, holding.quantity, holding.buy_price, holding.buy_date)
    )   
    
    conn.commit()  

    return holding.id

def get_holdings(conn):
    return pd.read_sql_query("SELECT * FROM holdings", conn)    

def delete_holding(conn, holding):

    cursor = conn.execute("DELETE FROM holdings WHERE id = ?", (holding.id,))
    conn.commit()
    return cursor.rowcount > 0



    