# VENV
* Tworzymy wirtualne środowisko python -m venv env
* Instalujemy wszystkie potrzebne biblioteki pip install -r requirements.txt
* Aktywacja venv -  .\env\Scripts\activate   
* Deaktywacja venv - deactivate 

# DJANGO
* Utworzenie projektu - django-admin startproject project
* Przechodzimy do utworzonego projektu - cd project
* Utworzenie aplikacji na serwerze - Python manage.py startapp api
* Uruchomienie serwera Django - python GymProject\manage.py runserver 
* Wstępna migracja danych ( wrazie gdyby baza się wysypała) -  python GymProject\manage.py makemigrations app
* Migracja danych (weryfikacja) - python GymProject\manage.py makemigrations 
* Migracja danych (realizacja) - python GymProjectt\manage.py migrate
* Zbieramy pliki statyczne - python GymProject\manage.py collectstatic  
* Utworzenie super użytkownika (przechowujemy w bazie danych Firebase)  - python GymProject\manage.py createsuperuser

* Routing w naszej aplikaji umożliwia nawigowanie między komponentami 
aplikacji bez potrzeby przeładowywania jej.

* views - plik który odpowiada za renderowanie stron, a raczek określa
co dokładnie ma zostać wyrenderowane. 

## Tworzymy konto użytkownika dla naszej bazy danych
CREATE USER 'admin'@'localhost' IDENTIFIED BY '**********';
grant all on sitedb.* to 'admin'@'localhost';

## Objaśnienie poszczególnych plików w Django 
views.py - zwraca odpowiednie widoki
urls.py - odpowiada za mapowanie naszych stron 
models.py - w tym pliku definiujemy nasze pola i zachowania danych które przechowujemy 
admin.py - w tym pliku rejestrujemy nasze modele, aby  były widoczne w panelu administracyjnym 
static -  w tym folderze przechowujemy pliki CSS, JS zdjęcia itp. 
templates - tutaj przechowujemy pliki html, często zawiera się w nich csrf_token (zabezpieczenie przed niekontrolowanym wykonaniem operacji).
