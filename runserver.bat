@echo off
call .env\Scripts\activate.bat
cd src
start python manage.py runserver --noreload
ping localhost -n 2 > nul
start http://127.0.0.1:8000/