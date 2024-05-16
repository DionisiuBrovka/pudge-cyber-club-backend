# pudge-cyber-club-backend

## About

> TODO -- write this

## How to Build

To build backend application follow next steps:

1. Add envirement file to: ```app/.env```
    ```.env
    export DEBUG = {}
    export DB_NAME = {}
    export DB_USER = {}
    export DB_USER_PASSWORD = {}
    export DB_HOST = {}
    export DB_DB_PORT = {}
    ```
2. Add password for db file to: ```db/password.txt```
3. Up docker compose stack: ```docker compose up -d```
4. Make migarations for db in django aplication container: ```python manage.py migrate``` 
5. Collect static filles: ```python manage.py collectstatic``` 

---

## Made by @**Dionisiu Brovka**



[![Link](https://img.shields.io/badge/email-dev.dionisiu.brovka%40gmail.com-green?style=for-the-badge)](mailto:dev.dionisiu.brovka@gmail.com) 
[![Link](https://img.shields.io/badge/telegram-goppi-blue?style=for-the-badge&color=%2300b2ff)](mailto:dev.dionisiu.brovka@gmail.com) 
[![Link](https://img.shields.io/badge/github-DIONISIU_BROVKA-blue?style=for-the-badge&color=%234925bb)](mailto:dev.dionisiu.brovka@gmail.com)

## License

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