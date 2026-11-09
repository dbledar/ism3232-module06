from my_assistant import AssignmentBot
from my_mock_model import MockModel
from my_tool import AssignmentTool


def make_bot() -> AssignmentBot:
    """Build a fresh chatbot for testing."""
    assignments = {"HW01": "01-01-2000", "LAB02": "02-02-2001", "EXAM03": "03-12-2002"}
    model = MockModel()
    return AssignmentBot("George", "Be succinct", AssignmentTool(assignments), model)


def test_tool_finds_deadline() -> None:
    tool = AssignmentTool({"HW01": "01-01-2000"})
    assert tool.find_deadline("HW01") == "01-01-2000"


def test_tool_returns_none_for_no_deadline() -> None:
    tool = AssignmentTool({"HW01": "01-01-2000"})
    assert tool.find_deadline("HW02") == None


def test_tool_finds_assignment() -> None:
    tool = AssignmentTool({"HW01": "01-01-2000"})
    assert tool.find_assignment("hw01") == "HW01"


def test_tool_returns_none_for_no_assignment() -> None:
    tool = AssignmentTool({"HW01": "01-01-2000"})
    assert tool.find_assignment("hw02") == None


def test_bot_returns_both_messages() -> None:
    bot = make_bot()
    bot.respond("hello")
    assert len(bot.history) == 2
    assert bot.history[0]["role"] == "user"
    assert bot.history[1]["role"] == "assistant"


def test_bot_returns_deadline() -> None:
    bot = make_bot()
    assert "January 1st, 2000" in bot.respond("HW01 due")


def test_bot_returns_advisor() -> None:
    bot = make_bot()
    assert "advisor" in bot.respond("major")
    assert "advisor" in bot.respond("schedule")
    assert "advisor" in bot.respond("registration")


def test_bot_safe_response() -> None:
    bot = make_bot()
    assert "not sure" in bot.respond("skibidi")
