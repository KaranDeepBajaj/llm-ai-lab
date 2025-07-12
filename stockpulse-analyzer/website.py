import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}


class StockSummary:
    def __init__(self, symbol):
        """
        Create a StockSummary object for the given stock symbol using Yahoo Finance
        """
        self.symbol = symbol.upper()
        self.url = f"https://finance.yahoo.com/quote/{self.symbol}"

        response = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"

        # Extract current price
        price_span = soup.find("fin-streamer", {"data-field": "regularMarketPrice"})
        self.price = price_span.text if price_span else "N/A"

        # Extract price change
        change_span = soup.find("fin-streamer", {"data-field": "regularMarketChangePercent"})
        self.change_percent = change_span.text if change_span else "N/A"

        # Optional: summary text if available
        summary_div = soup.find("section", {"data-test": "qsp-statistics"})
        self.summary_text = summary_div.get_text(strip=True) if summary_div else "Summary not found"

    def display(self):
        print(f"Stock: {self.symbol}")
        print(f"Title: {self.title}")
        print(f"Price: {self.price}")
        print(f"Change %: {self.change_percent}")
        print(f"Summary: {self.summary_text}")


# Example usage
if __name__ == "__main__":
    stock = StockSummary("AAPL")
    stock.display()
