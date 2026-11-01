# main.py
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
bot = SupportChatbot(
    "Sunny",
    "You are a friendly support assistant for Bayside Outfitters.",
    order_tool,
    stock_tool,
)

user_name = input("Hello, what is your name?\nYou: ")
print(f"Hello, {user_name}! Type a message, or type quit to stop.")
user_message = input(f"{user_name}: ")
while user_message != "quit":
    print(f"{bot.name}: {bot.respond(user_message)}")
    user_message = input(f"{user_name}: ")

print(f"Messages in this conversation: {len(bot.history) + 2}")
