# my_assistant.py
# Author: Darian Peters

HANDOFFS = ["major", "registration", "schedule"]
MONTHS = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December",
}


class AssignmentBot:
    """Mock chatbot that helps with deadlines."""

    def __init__(self, name: str, instructions: str, assignment_tool) -> None:
        self.name = name
        self.instructions = instructions
        self.assignment_tool = assignment_tool
        self.history = []

    def respond(self, user_message: str) -> str:
        """Records the user's message, choose a reply, record it, and then send it."""
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, text: str) -> str:
        """Chooses the reply to give based on specific keywords"""
        if self.needs_advisor(text):
            return "Sorry, I cannot help you with that. I am handing you off to your advisor."
        if "deadline" in text.lower() or "due" in text.lower():
            return self.reply_deadline(text)
        if "hello" in text.lower():
            return f"Hello! I'm {self.name}. I can check your deadlines for you."
        return "I'm not sure I can help with that. Try asking me about a deadline!"

    def needs_advisor(self, text: str) -> bool:
        """Returns True if the request requires an advisor."""
        for word in HANDOFFS:
            if word in text.lower():
                return True
        return False

    def reply_deadline(self, text: str) -> str:
        """Use the assignment tool to return the deadline."""
        assignment = self.assignment_tool.find_assignment(text)
        if assignment is None:
            return "Which assignment? Use assignment IDs like HW01, EXAM02, or LAB03."
        deadline = self.assignment_tool.find_deadline(assignment)
        if deadline is None:
            return f"{assignment} hasn't been assigned a deadline yet."
        deadline_parts = deadline.split("-")
        month = MONTHS[deadline_parts[0]]
        if "1" in deadline_parts[1][1] and deadline_parts[1][0] != "1":
            day = "1st"
        elif "2" in deadline_parts[1][1] and "1" not in deadline_parts[1]:
            day = "2nd"
        elif "3" in deadline_parts[1][1] and "1" not in deadline_parts[1]:
            day = "3rd"
        else:
            day = deadline_parts[1] + "th"
        year = deadline_parts[2]
        deadline_parts = []
        return f"{assignment} is due on {month} {day}, {year}."
