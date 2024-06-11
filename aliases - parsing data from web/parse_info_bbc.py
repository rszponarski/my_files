import requests
from bs4 import BeautifulSoup


def parse_bbc_news_headlines():
    url = "https://www.bbc.com/news"

    # Wysłanie żądania GET do strony
    response = requests.get(url)

    # Sprawdzenie, czy żądanie zostało wykonane poprawnie
    if response.status_code == 200:
        # Parsowanie zawartości strony przy użyciu BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Znalezienie wszystkich nagłówków artykułów
        headlines = soup.find_all("h3")

        # Wyświetlenie tytułów artykułów
        print("BBC News Headlines:")
        for headline in headlines:
            print(headline.text)
    else:
        print("Nie udało się pobrać zawartości strony.")


if __name__ == "__main__":
    parse_bbc_news_headlines()
