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

<img src="https://user-images.githubusercontent.com/49610728/195409755-ef65ac26-07b6-498d-ad04-fd48aeb287df.png" width="45%">
<br/> <br/>
Po wypełnieniu pól z nickiem, rozmiarem planszy, typem planszy i kliknięciu przycisku "Zatwierdź" następuje przejście
do strony:

<img src="https://user-images.githubusercontent.com/49610728/195409759-5ed9eeac-3b12-4b12-92aa-f589b8355daf.png" width="45%">
<br/> <br/>
Wypełniając pola "Wiersz" oraz "Kolumna" odpowiednie pola będą się zakolorowywać:

<img src="https://user-images.githubusercontent.com/49610728/195409763-b67f4584-d57c-4b1a-80bb-5f31c2ec7a25.png" width="45%">
<br/> <br/>
Końcowy efekt po rozwiązaniu całej łamigłówki:

<img src="https://user-images.githubusercontent.com/49610728/195409765-5951057e-2bb1-4d69-8e64-7759b96ad29d.png" width="45%">
<br/> <br/>
Przycisk na stronie startowej "Załaduj z pamięci" pozwala ładować stan rozpoczętej gry w danej sesji. Natomiast przycisk 
"Załaduj z pliku" pozwala załadować stan gry z pliku ```nick_gracza.txt```.
