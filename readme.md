# The Notes App

Przykładowa aplikacja stworzona w ramach zajęć z Python'a, można jej używać jako szablonu do własnych projektów lub ćwiczenia dockeryzacji.

## Instalacja
Sklonuj repozytorium na swoje lokalne środowisko.
Zainstaluj wymagane pakiety używając pip do wirtualnego środowiska:

```bash
python -m venv venv # Tylko pierwszy raz

source venv/bin/activate # MacOS/Linux
./venv/Scripts/activate.bat # Windows CMD
pip install -r requirements.txt
```

## Struktura projektu
Główny plik aplikacji to main.py, który zawiera definicje modeli, widoków i konfiguracji aplikacji.

Modele `User` i `Note` są zdefiniowane za pomocą SQLAlchemy, ORM dla Pythona. `User` reprezentuje zarejestrowanego użytkownika, a `Note` reprezentuje notatkę stworzoną przez użytkownika.

Widoki są zdefiniowane jako funkcje Pythona zadekorowane za pomocą `@app.route`. Każdy widok odpowiada za obsługę określonego żądania HTTP do określonego URL-a.

Szablony HTML są przechowywane w katalogu templates. Używają one silnika szablonów Jinja2 do renderowania dynamicznych danych.

## Uruchomienie aplikacji
Aby uruchomić aplikację, użyj poniższego polecenia:


```bash
python main.py
```

Aplikacja będzie dostępna pod adresem `http://localhost:8000`.

## Rozszerzanie aplikacji
Możesz rozbudować tę aplikację, dodając nowe funkcje, takie jak edycja i usuwanie notatek, udostępnianie notatek innym użytkownikom, dodawanie tagów do notatek i wiele innych. Pamiętaj, aby zawsze przestrzegać dobrych praktyk programowania i zasad bezpieczeństwa aplikacji webowych. Powodzenia!