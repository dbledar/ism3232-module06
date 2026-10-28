# two_bots.py
# Author: Darian Peters

from chatbot import SupportChatbot
from order_tool import OrderLookup
from stock_tool import StockLookup


ORDERS = {
    "A100": "shipped",
    "A101": "processing",
    "A102": "delivered",
}

STOCK = {
    "rain jacket": 12,
    "day pack": 0,
    "trail hat": 5,
}

order_tool = OrderLookup(ORDERS)
stock_tool = StockLookup(STOCK)
sunny = SupportChatbot(
    "Sunny",
    "You are cheerful and brief.",
    order_tool,
    stock_tool,
)
river = SupportChatbot(
    "River",
    "You are formal and detailed.",
    order_tool,
    stock_tool,
)

sunny.respond("hello")
sunny.respond("Where is order A100?")
river.respond("hello")

print(f"{sunny.name} {len(sunny.history)}")
print(f"{river.name} {len(river.history)}")
print(f"{sunny.respond('hello')}")
print(f"{river.respond('hello')}")
print(f"{sunny.instructions}")
print(f"{river.instructions}")
