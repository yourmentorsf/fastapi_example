# Код к вебинару "FastAPI" для студентов Skillfactory направления backend web development


## Содержание

[0. Подготовка](readme.md#Подготовка)

[1. Запуск](readme.md#Запуск)

[2. Дальнейшие действия](readme.md#Дальнейшие-действия)

## Подготовка

Рекомендуемое ПО:
[VSCode](https://code.visualstudio.com/), [Python](https://www.python.org/downloads/), [Git BASH](https://gitforwindows.org/)

Для запуска проекта необходимо выполнить следующие действия:

1. Скачать и распаковать архив, либо клонировать репозиторий командой

```bash
git clone git@github.com:yourmentorsf/fastapi_example.git
```

2. Перейти в папку с кодом и открыть в ней редактор кода. Команда для запуска VSCode в текущей папке из терминала:

```bash
code .
```

3. Создать и активировать виртуальное оркужение:

```bash
python -m venv venv

source venv/bin/activate - Linux/MacOS

venv\Scrips\activate - Windows

pip install -r requirements.txt
```


## Запуск

1. В терминале выполнить команду для запуска веб-сервера: 

```bash
uvicorn main:app --reload 
```


2. В браузере перейти по адресу 

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

или

[http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)


2. Для запуска тестов в терминале выполнить команду: 

```bash
pytest
```

## Дальнейшие действия

Изучить код, научиться писать веб-приложения с использованием FastAPI.  

**Удачи!**