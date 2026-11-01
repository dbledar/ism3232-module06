# my_main.py
# Author: Darian Peters

from my_assistant import AssignmentBot
from my_tool import AssignmentTool

ASSIGNMENTS = {
    "HW11": "11-13-2026",
    "LAB02": "11-13-2026",
    "EXAM01": "12-03-2026",
}

assignment_tool = AssignmentTool(ASSIGNMENTS)
bot = AssignmentBot("Delilah", "You are frank and polite.", assignment_tool)

user_name = input(f"{bot.name}: Hello, what is your name?\nYou: ")
print(
    f"{bot.name}: Hello, {user_name}! I am {bot.name}. Type a message, or type quit to stop."
)
user_message = input(f"{user_name}: ")
while user_message.lower() != "quit":
    print(f"{bot.name}: {bot.respond(user_message)}")
    user_message = input(f"{user_name}: ")

print(f"Messages in this conversation: {len(bot.history) + 2}")
