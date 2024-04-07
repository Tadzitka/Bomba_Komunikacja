def odpowiedz_na_slowo(slowo):
    grupy_slow = {
        'grupa 1': ['kolarz'],
        'grupa 2': ['but', 'okej', 'kod'],
        'grupa 3': ['nic', 'mieć', 'jak?'],
        'grupa 4': ['pusty', 'może', 'morze', 'buk', 'kolaż', 'jak'],
        'grupa 5': ['lud', 'lód', 'romb'],
        'grupa 6': ['wyświetlacz', 'nie', 'miedź', 'lut', 'bóg', 'rąb', 'ja', 'kot']
    }

    odpowiedz_1 = None

    for grupa, slowa in grupy_slow.items():
        if slowo in slowa:
            if grupa == 'grupa 1':
                odpowiedz_1 = "LEWY GÓRA"
            elif grupa == 'grupa 2':
                odpowiedz_1 = "PRAWY GÓRA"
            elif grupa == 'grupa 3':
                odpowiedz_1 = "LEWY ŚRODEK"
            elif grupa == 'grupa 4':
                odpowiedz_1 = "PRAWY ŚRODEK"
            elif grupa == 'grupa 5':
                odpowiedz_1 = "LEWY DÓŁ"
            elif grupa == 'grupa 6':
                odpowiedz_1 = "PRAWY DÓŁ"

    if odpowiedz_1:
        print("Pierwsza odpowiedź: ", odpowiedz_1)

    if slowo in dane.values():
        for klucz, wartosc in dane.items():
            if slowo in wartosc.split(', '):
                print("Druga odpowiedź: ", klucz)
                return
    else:
        wejscie = input("Wprowadź wartość w cudzysłowie: ")
        if wejscie in dane:
            print("Druga odpowiedź: ", dane[wejscie])
        else:
            print("Nie ma takiej wartości w słowniku.")


if __name__ == "__main__":
    dane = {
        "gotów": "TAK, OKEJ, HAH, ŚRODEK, LEWY, NADUŚ, PRAWY, PUSTY, GOTÓW, NIE, PIERWSZY, ŹLE, NIC, CZEKAJ",
        "pierwszy": "LEWY, OKEJ, TAK, ŚRODEK, NIE, PRAWY, NIC, ŹLE, CZEKAJ, GOTÓW, PUSTY, HAH, NADUŚ, PIERWSZY",
        "nie": "PUSTY, ŹLE, CZEKAJ, PIERWSZY, HAH, GOTÓW, PRAWY, TAK, NIC, LEWY, NADUŚ, OKEJ, NIE, ŚRODEK",
        "pusty": "CZEKAJ, PRAWY, OKEJ, ŚRODEK, PUSTY, NADUŚ, GOTÓW, NIC, NIE, HAH, LEWY, ŹLE, TAK, PIERWSZY",
        "nic": "ŹLE, PRAWY, OKEJ, ŚRODEK, TAK, PUSTY, NIE, NADUŚ, LEWY, HAH, CZEKAJ, PIERWSZY, NIC, GOTÓW",
        "tak": "OKEJ, PRAWY, ŹLE, ŚRODEK, PIERWSZY, HAH, NADUŚ, GOTÓW, NIC, TAK, LEWY, PUSTY, NIE, CZEKAJ",
        "hah": "ŹLE, HAH, LEWY, NIC, GOTÓW, PUSTY, ŚRODEK, NIE, OKEJ, PIERWSZY, CZEKAJ, TAK, NADUŚ, PRAWY",
        "źle": "GOTÓW, NIC, LEWY, HAH, OKEJ, TAK, PRAWY, NIE, NADUŚ, PUSTY, ŹLE, ŚRODEK, CZEKAJ, PIERWSZY",
        "lewy": "PRAWY, LEWY, PIERWSZY, NIE, ŚRODEK, TAK, PUSTY, HAH, ŹLE, CZEKAJ, NADUŚ, GOTÓW, OKEJ, NIC",
        "prawy": "TAK, NIC, GOTÓW, NADUŚ, NIE, CZEKAJ, HAH, PRAWY, ŚRODEK, LEWY, ŹLE, PUSTY, OKEJ, PIERWSZY",
        "środek": "PUSTY, GOTÓW, OKEJ, HAH, NIC, NADUŚ, NIE, CZEKAJ, LEWY, ŚRODEK, PRAWY, PIERWSZY, ŹLE, TAK",
        "okej": "ŚRODEK, NIE, PIERWSZY, TAK, ŹLE, NIC, CZEKAJ, OKEJ, LEWY, GOTÓW, PUSTY, NADUŚ, HAH, PRAWY",
        "czekaj": "ŹLE, NIE, PUSTY, OKEJ, TAK, LEWY, PIERWSZY, NADUŚ, HAH, CZEKAJ, NIC, GOTÓW, PRAWY, ŚRODEK",
        "naduś": "PRAWY, ŚRODEK, TAK, GOTÓW, NADUŚ, OKEJ, NIC, ŹLE, PUSTY, LEWY, PIERWSZY, HAH, NIE, CZEKAJ",
        "buk": "DALEJ, BÓG, BUG, BUT, NASTĘPNY, LUT, LÓD, TRZYMAJ, CO?, BUK, HAHA, KTÓRY?, DOBRZE, LUD",
        "bóg": "BUG, NASTĘPNY, KTÓRY?, LUT, CO?, DOBRZE, HAHA, TRZYMAJ, BUK, LUD, BUT, DALEJ, LÓD, BÓG",
        "bug": "HAHA, BÓG, LUT, BUG, NASTĘPNY, LÓD, DALEJ, LUD, BUT, BUK, CO?, TRZYMAJ, KTÓRY?, DOBRZE",
        "but": "BUK, BUT, LÓD, NASTĘPNY, HAHA, BÓG, LUD, BUG, CO?, LUT, DALEJ, DOBRZE, KTÓRY?, TRZYMAJ",
        "lód": "DOBRZE, LUD, LÓD, LUT, CO?, DALEJ, BUG, TRZYMAJ, BUT, KTÓRY?, NASTĘPNY, HAHA, BÓG, BUK",
        "lud": "LUT, DALEJ, NASTĘPNY, CO?, BUT, LÓD, HAHA, DOBRZE, LUD, BUK, KTÓRY?, TRZYMAJ, BÓG, BUG",
        "lut": "LUT, BUG, BÓG, BUK, DOBRZE, TRZYMAJ, HAHA, NASTĘPNY, DALEJ, KTÓRY?, BUT, LÓD, LUD, CO?",
        "haha": "LÓD, LUD, BÓG, BUT, NASTĘPNY, HAHA, DOBRZE, BUK, LUT, KTÓRY?, BUG, DALEJ, TRZYMAJ, CO?",
        "co?": "BUK, TRZYMAJ, BUT, BUG, LUD, DOBRZE, HAHA, KTÓRY?, BÓG, LUT, LÓD, NASTĘPNY, CO?, DALEJ",
        "dobrze": "DALEJ, LUT, NASTĘPNY, CO?, BUG, LÓD, BUT, TRZYMAJ, KTÓRY?, BUK, LUD, BÓG, HAHA, DOBRZE",
        "następny": "CO?, LUT, HAHA, BUG, TRZYMAJ, DALEJ, NASTĘPNY, KTÓRY?, DOBRZE, BÓG, LÓD, BUT, LUD, BUK",
        "trzymaj": "BÓG, LUD, DOBRZE, HAHA, BUK, LÓD, DALEJ, CO?, BUT, NASTĘPNY, TRZYMAJ, LUT, BUG, KTÓRY?",
        "dalej": "BÓG, DOBRZE, KTÓRY?, BUT, BUK, TRZYMAJ, LUT, LÓD, DALEJ, LUD, CO?, NASTĘPNY, BUG, HAHA",
        "który?": "BUT, NASTĘPNY, LUD, LÓD, TRZYMAJ, DOBRZE, HAHA, CO?, LUT, BUK, KTÓRY?, DALEJ, BÓG, BUG"
    }

    slowo = input("Wpisz jedno ze słów z bazy danych: ").strip().lower()
    odpowiedz_na_slowo(slowo)

