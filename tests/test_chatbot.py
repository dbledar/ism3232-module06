from chatbot import SupportChatbot
from order_tool import OrderLookup
from stock_tool import StockLookup


def make_bot() -> SupportChatbot:
    """Build a fresh chatbot with its own tool for each test."""
    orders = {"A100": "shipped", "A101": "processing"}
    stock = {"rain jacket": 12, "day pack": 0}
    return SupportChatbot(
        "Sunny", "Be friendly.", OrderLookup(orders), StockLookup(stock)
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
