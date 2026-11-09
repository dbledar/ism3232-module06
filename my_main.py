# my_main.py
# Author: Darian Peters

from my_assistant import AssignmentBot
from my_tool import AssignmentTool
from ollama_model import OllamaModel

ASSIGNMENTS = {
    "HW11": "11-13-2026",
    "LAB02": "11-13-2026",
    "EXAM01": "12-03-2026",
}
INSTRUCTIONS = """You are Delilah, a frank and polite assistant for students.
You will answer questions about assignments and their due dates.
If you do not know the answer, say you do not know and offer to pass the student to their advisor.
Only state facts that appear in these instructions."""


assignment_tool = AssignmentTool(ASSIGNMENTS)
model = OllamaModel()
bot = AssignmentBot("Delilah", INSTRUCTIONS, assignment_tool, model)

user_name = input(f"{bot.name}: Hello, what is your name?\nYou: ")
print(
    f"{bot.name}: Hello, {user_name}! I am {bot.name}. Type a message, or type quit to stop."
)
user_message = input(f"{user_name}: ")
while user_message.lower() != "quit":
    print(f"{bot.name}: {bot.respond(user_message)}")
    user_message = input(f"{user_name}: ")

print(f"Messages in this conversation: {len(bot.history) + 2}")
