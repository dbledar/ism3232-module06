# stock_tool.py
# Author: Darian Peters


class StockLookup:
    """A tool that knows about stocks. Whether it knows about orders or chatting is pending investigation."""

    def __init__(self, stock: dict) -> None:
        self.stock = stock

    def find_product(self, text: str):
        """Returns the first known product name in text or None."""
        for product in self.stock:
            if product in text.lower():
                return product
        return None

    def count_for(self, product: str):
        """Returns the count of a product or None."""
        if product in self.stock:
            return self.stock[product]
        return None
