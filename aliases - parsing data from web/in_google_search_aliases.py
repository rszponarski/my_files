import requests
from bs4 import BeautifulSoup


def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.find("h3")  # znajdź pierwszy tytuł z wyników wyszukiwania
    return result.text if result else None


def main():
    with open("wig_40_cleanup.txt", "r") as file:
        lines = file.readlines()  # odczytaj wszystkie linie z pliku

    with open("google_searched.txt", "w") as output_file:
        for linijka in lines:
            linijka = linijka.strip()  # usuń białe znaki z końca i początku linii
            query = f"yahoo finance {linijka}"
            title = search_google(query)

            if title:
                output_file.write(title + "\n")
                print(f"Tytuł dla frazy '{linijka}': {title}")
            else:
                output_file.write("Brak wyników dla: " + linijka + "\n")
                print(f"Brak wyników dla frazy '{linijka}'.")


    print("Wyniki zapisano do pliku google_searched.txt")


if __name__ == "__main__":
    main()

