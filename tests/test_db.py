import pytest
from portfolio_xray.db import connect, init_db, add_holding, get_holdings, delete_holding
from portfolio_xray.models import Holding


@pytest.fixture
def conn():
    conn = connect(":memory:")
    init_db(conn)
    yield conn
    conn.close()


def test_add_holding(conn):
    holding = Holding("AAPL", 10, 150, "2024-01-05")

    add_holding(conn, holding)

    df = get_holdings(conn)
    assert len(df) == 1
    assert df["ticker"][0] == "AAPL"

def test_delete_holding(conn):
    add_holding(conn, Holding("AAPL", 10, 150, "2024-01-05"))

    df = get_holdings(conn)
    row = df.iloc[0]                 
    holding = Holding(row["ticker"], row["quantity"], row["buy_price"],
                      row["buy_date"], id=int(row["id"]))

    assert delete_holding(conn, holding) is True
    assert get_holdings(conn).empty