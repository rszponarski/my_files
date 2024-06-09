import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_mWIG40_companies():
    url = "https://www.money.pl/gielda/indeksy_gpw/mwig40/"
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Uruchamia przeglądarkę w trybie bezgłowym (bez interfejsu GUI)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)

    # Czekaj, aż wszystkie elementy będą załadowane
    time.sleep(5)

    companies = []
    for i in range(1, 41):
        try:
            xpath = f'//*[@id="app"]/div/div[11]/div/div[2]/div/main/div/section[2]/div[2]/div[1]/div/div/div[1]/div[2]/div[{i}]/div/div[1]/a/div'
            company_element = driver.find_element(By.XPATH, xpath)
            company_name = company_element.text.strip()
            companies.append(company_name)
        except Exception as e:
            print(f"Nie udało się pobrać danych dla indeksu {i}: {e}")
            break

    driver.quit()
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
