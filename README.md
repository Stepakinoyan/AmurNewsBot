# AmurNewsBot

## Описание

Этот проект создан специально для хакатона «CODDY11100».

## Инструкция по запуску

1. Создайте файл `.env-non-dev` с следующим содержимым:

    ```plaintext
    MODE=PROD

    TOKEN=Свой тг токен

    DB_NAME=postgres
    DB_PASS=postgres
    DB_HOST=db
    DB_USER=postgres
    DB_PORT=5432

    POSTGRES_DB=postgres
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres

    TEST_DB_NAME=postgres
    TEST_DB_PASS=postgres
    TEST_DB_HOST=db
    TEST_DB_USER=postgres
    TEST_DB_PORT=5432

    SECRET_KEY=Свой ключ
    ```

2. Запустите проект с помощью команды:

    ```
    docker compose up
    ```

## Примечания

- **TOKEN**: Замените `Свой тг токен` на ваш действующий токен Telegram.
- **SECRET_KEY**: Замените `Свой ключ` на ваш секретный ключ.
