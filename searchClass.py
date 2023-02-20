import requests


class Saerch1(object):
    url_iv_p = "https://omnieq.com/underlyings/S&P/SPX.IN"

    def __init__(self, day, range_percent):
        self.day = day
        self.range_percent = range_percent

    """The function get_iv gets the iv (implied volatility) percent of the stock.In this case SPX."""

    def get_iv(self):
        r = requests.get(Saerch1.url_iv_p, stream=True)
        for line in r.iter_lines():
            line = str(line)
            if '<th scope="row">IV</th>' in line:
                return float(line[line.find("IV") + 11:line.find("%")]) / 100

    """The function get_price accepts the current price of the stock. In this case SPX."""

    def get_price(self):
        r = requests.get(Saerch1.url_iv_p, stream=True)
        for line in r.iter_lines():
            line = str(line)
            if '<th scope="row">Price</th>' in line:
                return float(line[line.find("Price") + 15:line.find("Previous") - 30])
