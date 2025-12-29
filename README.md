# Investing Portfolio Backend

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
- 