## Fill-a-pix-desktop

#### Uruchomienie aplikacji (Windows - Git Bash)

Instalacja potrzebnych bibliotek i pakietów:
```
pip install -r requirements.txt
```

Uruchomienie programu:
```
python main.py
```

Aplikacja dostępna jest pod adresem: http://localhost:5000/. Jej interfejs prezentuje się następująco:

screen

Po wypełnieniu pól z nickiem, rozmiarem planszy, typem planszy i kliknięciu przycisku "Zatwierdź" następuje przejście
do strony:

screen

Wypełniając pola "Wiersz" oraz "Kolumna" odpowiednie pola będą się zakolorowywać:

screen

Końcowy efekt po rozwiązaniu całej łamigłówki:

screen

Przycisk na stronie startowej "Załaduj z pamięci" pozwala ładować stan rozpoczętej gry w danej sesji. Natomiast przycisk 
"Załaduj z pliku" pozwala załadować stan gry z pliku ```nick_gracza.txt```.