def create_dictionary_from_file(file_path):
    dictionary = {}
    with open(file_path, "r") as file:
        for line in file:
            # podziel linię na klucz i wartość na podstawie nawiasów okrągłych
            parts = line.strip().split("(")
            if len(parts) >= 2:
                key = parts[0].strip()
                value = parts[1].split(")")[0].strip()
                dictionary[key] = value
    return dictionary

def save_dictionary_to_file(dictionary, file_path):
    with open(file_path, "w") as file:
        file.write("mWIG40 = {\n")
        for key, value in dictionary.items():
            file.write(f"    '{key}': '{value}',\n")
        file.write("}")

def main():
    file_path = "google_searched.txt"  # Ścieżka do pliku tekstowego
    result_dict = create_dictionary_from_file(file_path)
    save_dictionary_to_file(result_dict, "dictionary_mWIG40.py")

if __name__ == "__main__":
    main()
