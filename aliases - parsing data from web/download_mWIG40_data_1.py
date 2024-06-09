import requests
from bs4 import BeautifulSoup
from lxml import etree


def get_mWIG40_companies():
    url = "https://www.money.pl/gielda/indeksy_gpw/mwig40/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Konwertujemy zawartość na obiekt lxml
    dom = etree.HTML(str(soup))

    companies = []

    # XPath dla nazw spółek
    company_tags = dom.xpath('//*[@id="app"]/div/div[11]/div/div[2]/div/main/div/section[2]/div[2]/div[1]/div/div/div/div[2]/div/div/div/a/div')
    for tag in company_tags:
        company_name = tag.text.strip()
        companies.append(company_name)

    return companies

def save_to_text_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for company in data:
            file.write(f'{company}\n')

# Przykład użycia
if __name__ == "__main__":
    companies = get_mWIG40_companies()
    if companies:
        save_to_text_file(companies, 'mWIG40_companies.txt')
        print("Zapisano dane do pliku mWIG40_companies.txt")
    else:
        print("Nie udało się pobrać danych.")
