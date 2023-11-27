from src import scraper


def test_formatPrice():
    prices = [
        "     Now\n                         \n\n            199 \n\n\n 00 \n\n\n /month",
        "$\n                         \n\n              228 \n\n\n 02 \n\n\n",
        " Now\n                         \n\n 112 \n\n\n 32 \n\n\n /month",
        "299\n\n\n58",
        "     Now\n                         \n\n            499 \n\n\n \n\n\n 00"
    ]

    ans = [199.00, 228.02, 112.32, 299.58, 499]
    formattedPrices = []

    for ele in prices:
        formattedPrices.append(scraper.formatPrice(ele))

    assert (ans == formattedPrices)
