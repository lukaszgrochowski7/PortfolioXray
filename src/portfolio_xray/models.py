from dataclasses import dataclass

@dataclass
class Holding:
    ticker : str
    quantity : float
    buy_price : float
    buy_date : str
    id: int | None = None




