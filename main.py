# main.py
# Author: Darian Peters

from chatbot import SupportChatbot
from ollama_model import OllamaModel
from order_tool import OrderLookup
from stock_tool import StockLookup

MODEL_NAME = "granite4.1:3b"
INSTRUCTIONS = """You are Sunny, a friendly support assistant for Bayside Outfitters. 
Answer in one short sentence.
Store hours are 10 am to 7 pm every day.
Returns are accepted within 30 days with a reciept.
Only state facts that appear in these instructions.
If you do not know, say you do not know and offer to pass the customer to a human agent."""

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
model = OllamaModel(MODEL_NAME)
bot = SupportChatbot("Sunny", INSTRUCTIONS, order_tool, stock_tool, model)

user_name = input("Hello, what is your name?\nYou: ")
print(f"Hello, {user_name}! Type a message, or type quit to stop.")
user_message = input(f"{user_name}: ")
while user_message != "quit":
    print(f"{bot.name}: {bot.respond(user_message)}")
    user_message = input(f"{user_name}: ")

print(f"Messages in this conversation: {len(bot.history) + 2}")
