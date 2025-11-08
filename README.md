# Investing Portfolio Backend


## Table of contents

1. [📌 About the project](#about)
   - [🎯 Goals of the project](#goals)
   - [🛠️ Stack and tools](#stack-and-tools)
2. [🚀 Getting Started](#start)
   - [📦 Poetry](#poetry)
   - [🔄 Pre-commit](#pre-commit)
   - [🪟 Installation on Windows](#installation-on-Windows)

## 📌 About the project <a name="about"></a> 

**Investing Portfolio Backend** — The backend part of the "Investment Portfolio" is an application for displaying the investment portfolio of clients, which allows:
- 📊 
- 🔍 
- 💡 
- 📈 
### 🎯 Goals of the project <a name="goals"></a> 
Goals:
- 📊 
- 🔍 
- 💡 
- 📈
  
### 🛠️ Stack and tools <a name="stack-and-tools"></a> 
Stack and tools:
- 🛠️ Python 3.12.
- 🛠️ 
- 🛠️ 
- 🛠️ Taskiq + TaskiqAioPika

to run taskiq broker enter the backend container terminal:
```
docker exec -it dev-backend-1 bash
```
and start the worker(-s) with the command:
```
taskiq worker app.adapters.taskiq.broker:broker --worker 1 --no-configure-logging --fs-discover --tasks-pattern "**/tasks"
```

## 🚀 Getting Started <a name="start"></a> 

### 📦 Poetry <a name="poetry"></a> 

Poetry is a tool for managing Python dependencies and virtual environments. It is a **required** tool for the Poetry project.

<details>
<summary><strong>🔽 Installing Poetry</strong></summary>

#### Installing Poetry

Follow the [official instructions](https://python-poetry.org/docs/#installation) or use one of the following methods:

</details>


Create .env.deploy and .env.app files in the sources root


Backend service for managing an investment portfolio.



To run the project locally:

Make sure that db ports are open in 'docker-compose.yaml':
```
  pg:
    ports:
      - "5432:5432"
```
Run the database in a Docker container:
```
docker compose up -d --build pg
```

Make sure that in the file 'fastapi_app/.env.app' the line with the database connection settings looks like this:
```
APP_CONFIG__DB__URL=postgresql+asyncpg://some_usr:some_pwd@localhost:5432/some_db
```
and run the command in terminal:
```
python fastapi_app/main.py
```

To run the whole project locally in docker-network:
Make sure that in the file 'fastapi_app/.env.app' the line with the database connection settings looks like this:
```
APP_CONFIG__DB__URL=postgresql+asyncpg://some_usr:some_pwd@pg:5432/some_db
```
and then run the command in terminal:
```
docker compose up -d --build
```

Testing:



Links:
- https://docs.sqlalchemy.org/en/20/core/engines.html#sqlalchemy.create_engine
- https://taskiq-python.github.io/


TODO:
Check whether stock exists (by ticker and provider). 
If stock doesn't exist, that create stock.
Create stock registry
Update information about stock from API-response
Refactor stock-transaction POST: ticker and provider must be in nested object asset like:
{
   "asset_type": "stock",
   “asset”: {
      "provider": "string",
      "asset_ticker": "string"
   },
   "initial_price": 0,
   "transaction_commission": 0,
   "transaction_currency": "USD",
   "transaction_date": "2025-11-05",
   "transaction_quantity": 0,
   "transaction_type": "buy",
   "notes": "string"
}
