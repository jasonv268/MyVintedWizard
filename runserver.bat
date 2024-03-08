@echo off

set "VENV_DIR=venv"
set "REQUIREMENTS_FILE=requirements.txt"

if exist "%VENV_DIR%" (
    echo Environnement virtuel Python déjà créé.
) else (
    echo Création de l'environnement virtuel Python...
    python -m venv "%VENV_DIR%"
    echo Environnement virtuel Python créé avec succès.
    echo Activation de l'environnement virtuel...
    call "%VENV_DIR%\Scripts\activate"

    echo Installation des dépendances depuis le fichier %REQUIREMENTS_FILE%...
    pip install -r "%REQUIREMENTS_FILE%"

    playwright install

    echo Installation terminée.
)
call "%VENV_DIR%\Scripts\activate"

if exist .config (
    echo Le fichier .config est présent.
) else (
    echo Le fichier .config est manquant. Arrêt du script.
    pause > nul
    exit /b 1
)

cd src

if exist db.sqlite3 (
    echo Le fichier db.sqlite3 est présent.
) else (
    echo Le fichier .config est manquant. Arrêt du script.
    pause > nul
    exit /b 1
)


start python manage.py runserver --noreload
ping localhost -n 2 > nul
start http://127.0.0.1:8000/
