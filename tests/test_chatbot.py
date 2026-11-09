from chatbot import SupportChatbot
from echo_model import EchoModel
from mock_model import MockModel
from order_tool import OrderLookup
from stock_tool import StockLookup


class SilentModel:
    """A model that never has an answer. It stands in for Ollama being switched off."""

    def reply(self, instructions, history):
        return None


def make_bot() -> SupportChatbot:
    """Build a fresh chatbot with its own tool for each test."""
    orders = {"A100": "shipped", "A101": "processing"}
    stock = {"rain jacket": 12, "day pack": 0}
    return SupportChatbot(
        "Sunny", "Be friendly.", OrderLookup(orders), StockLookup(stock), MockModel()
    )


def make_bot_with_silent_mode() -> SupportChatbot:
    """Build a chatbot whose model never answers."""
    orders = {"A100": "shipped", "A101": "processing"}
    stock = {"rain jacket": 12, "day pack": 0}
    return SupportChatbot(
        "Sunny", "Be friendly.", OrderLookup(orders), StockLookup(stock), SilentModel()
    )


def test_tool_finds_known_status() -> None:
    tool = OrderLookup({"A100": "shipped"})
    assert tool.find_status("A100") == "shipped"


def test_tool_returns_none_for_unknown_order() -> None:
    tool = OrderLookup({"A100": "shipped"})
    assert tool.find_status("A999") is None


def test_respond_records_both_messages() -> None:
    bot = make_bot()
    bot.respond("hello")
    assert len(bot.history) == 2
    assert bot.history[0]["role"] == "user"
    assert bot.history[1]["role"] == "assistant"


def test_order_question_uses_the_tool() -> None:
    bot = make_bot()
    assert bot.respond("Where is order A100?") == "Order A100 is shipped."


def test_order_question_without_an_id_asks_for_one() -> None:
    bot = make_bot()
    assert "order ID" in bot.respond("Where is my order?")


def test_stock_question_uses_the_tool() -> None:
    bot = make_bot()
    assert "12" in bot.respond("Is this rain jacket in stock?")


def test_stock_question_without_a_name_asks_for_one() -> None:
    bot = make_bot()
    assert "product" in bot.respond("Is this in stock?")


def test_address_change_goes_to_a_human() -> None:
    bot = make_bot()
    assert "human" in bot.respond("Please change my shipping address")


def test_unknown_request_gets_a_safe_reply() -> None:
    bot = make_bot()
    assert "not sure" in bot.respond("What is the weather today?")


def test_two_chatbots_keep_separate_histories() -> None:
    first = make_bot()
    second = make_bot()
    first.respond("hello")
    assert len(first.history) == 2
    assert len(second.history) == 0


def test_count_user_messages() -> None:
    bot = make_bot()
    bot.respond("hello")
    assert bot.count_user_messages() == 1
    bot.respond("weather")
    bot.respond("order")
    assert bot.count_user_messages() == 3


def test_other_messages_go_to_the_model() -> None:
    bot = make_bot()
    assert bot.respond("Hello") == "Hello! How can I help you today?"


def test_safe_reply_when_the_model_has_no_answer() -> None:
    bot = make_bot_with_silent_mode()
    assert "try again" in bot.respond("Hello")


def test_order_rules_does_not_need_the_model() -> None:
    bot = make_bot_with_silent_mode()
    assert "shipped" in bot.respond("Where is order A100?")


def test_handoff_rule_does_not_need_the_model() -> None:
    bot = make_bot_with_silent_mode()
    assert "human" in bot.respond("Please change my shipping address")


def test_chatbot_works_with_any_model_that_has_a_reply_method() -> None:
    order_tool = OrderLookup({"A100": "shipped"})
    stock_tool = StockLookup({"rain jacket": 12})
    bot = SupportChatbot("Sunny", "Be friendly.", order_tool, stock_tool, EchoModel())
    assert bot.respond("good morning") == "You said: good morning"
