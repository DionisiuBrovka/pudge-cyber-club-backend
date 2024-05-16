# pudge-cyber-club-backend <br> <sub><sup>0.0.0.а</sup><sub>

## About ( О приложении )

**Pudge Cyber Club** - Cистема из набора клиент-серверных приложений для администрирования и брони мест в компьютерных клубов _PUDGE_. 

**Pudge Cyber Club Backend** - DRF приложения обеспечивающие restfull api для клиентов


## Roadmap ( Технологическая + карта )

### 🟢 0.0.0.a

_Базовая версия бэка для приложения. Реализованы следующие функции:_

1. Базовые модели данных, а так же  rest интерфейс для crud операций с ними:
    - Модель "**Клуб**"
    - Модель "**Компьютер**"
    - Модель "**Тип компьютера**"
    - Модель "**Пользователь приложения**"
2. Реализован базовый функционал авторизации и аутентификация пользователя с помощью токена
3. Раздача статических файлов через nginx
4. Настроены прикольные стили для админки

### 🔴 0.1.0.a

_Версия отточенная для работы над dev версией клиента. Включает следующие пункты:_

1. Настройка правил CORS для media файлов
2. Добавление енд поинтов для специальных средств:
   - Добавление группы компьютеров для клуба
   - и другие **TODO НАПИСАТЬ ЕЩЕ**
3. Подготовка базового пакета данных (заполнения базы данных)
4. Развертывание на удаленном сервере (скорее всего домашнем) 

### 🔴 промежуточные версии ... 

_Дополнить при надобности_

### 🔴 1.0.0

_Финальная версия продукта_

**TODO НАПИСАТЬ ЕЩЕ**

## How to Build (Сборка)

Для сборки приложения нужно сделать следующие:

1. Добавить файл переменной среды: ```app/.env```
    ```.env
    export DEBUG = // отладочная версия или нет
    export DB_NAME = // название базы данных
    export DB_USER = // имя пользователя базы данных
    export DB_USER_PASSWORD = // пароль от пользователя базы данных
    export DB_HOST = // хост адрес
    export DB_DB_PORT = // хост порт
    ```
2. Добавить пароль от базы данных в файл: ```db/password.txt```
3. Собрать стек контейнеров: ```docker compose up -d```
4. Выполнить миграции для бд: ```python manage.py migrate``` 
5. Собрать статические файлы приложения: ```python manage.py collectstatic``` 


## Made by (Автор)

[![Link](https://img.shields.io/badge/email-dev.dionisiu.brovka%40gmail.com-green?style=for-the-badge)](mailto:dev.dionisiu.brovka@gmail.com) 
[![Link](https://img.shields.io/badge/telegram-goppi-blue?style=for-the-badge&color=%2300b2ff)](mailto:dev.dionisiu.brovka@gmail.com) 
[![Link](https://img.shields.io/badge/github-DIONISIU_BROVKA-blue?style=for-the-badge&color=%234925bb)](mailto:dev.dionisiu.brovka@gmail.com)

## License (Лицензия)

    Pudge Cuber Club System - software for managing a network of computer clubs
    Copyright (C) 2024  Dionisiu Brovka

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.