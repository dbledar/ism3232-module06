# echo_model.py
# Author: Darian Peters


class EchoModel:
    """A model that echos the last thing the user sent."""

    def reply(self, instructions, history) -> str:
        """Return the last message with a few words in front of it."""
        last_message = history[-1]["content"]
        return f"You said: {last_message}"
