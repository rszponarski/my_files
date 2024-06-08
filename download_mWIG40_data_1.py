import requests
from bs4 import BeautifulSoup

def get_mWIG40_tickers():
    url = "https://pl.investing.com/indices/wig-40-components"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    mWIG40 = {}

    # Znajdź tabelę zawierającą spółki mWIG40
    table = soup.find('table', {'id': 'cr1'})
    if not table:
        print("Nie znaleziono tabeli z komponentami mWIG40.")
        return mWIG40

    rows = table.find_all('tr')[1:]  # Pomijamy nagłówek tabeli

    for row in rows:
        cols = row.find_all('td')
        company_name = cols[1].text.strip()
        ticker = cols[1].find('a').get('href').split('/')[-1] + ".WA"
        mWIG40[company_name] = ticker

    return mWIG40

def save_to_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for company, ticker in data.items():
            file.write(f'{company}: {ticker}\n')

# Przykład użycia
if __name__ == "__main__":
    tickers = get_mWIG40_tickers()
    save_to_file(tickers, 'mWIG40_tickers.txt')
    print("Zapisano dane do pliku mWIG40_tickers.txt")

