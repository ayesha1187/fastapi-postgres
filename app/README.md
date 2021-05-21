# This project demonstrates FastAPI-Postgres integration.

# pre-requisites
- Python 3.7
- Postgresql (https://www.postgresql.org/download/)

## Initial Setup
1. Create virtual env with python 3.7 and activate the same.
2. Install python dependencies required for the app to run locally:
    `pip install -r requirements.txt`
3. Create postgres database locally. (Refer .env file . Password is base64 encoded)
4. Create database schema and dummy records:
    `alembic -x env=.env upgrade heads`

## Run and configure API locally
- Add below config to launch.jso:
"configurations": [
        {
            "name": "Python: FastAPI",
            "type": "python",
            "request": "launch",
            "module": "uvicorn",
            "args": [
                "src.main:app", "--reload"
            ],
            "envFile": "${workspaceFolder}/app/.env",
			"cwd": "${workspaceFolder}/app",
			"jinja": true,
			"justMyCode": false
        }
    ]
- .env file contains database configuration details.

# Assumptions:
- Trade and TradeDetails are two tables having trade_id as primary and foreign key respectively.
- orm_models.py maps database tables to ORM. (sqlalchemy)
- models.py contains API response models.
- api_helper.py forwards api calls to database layer.
- db_helper.py makes db connections and returns data by executing queries back to api_helper.
- Below are the API endpoint details:
    1. /getalltrades --> Displays all trade details
    2. /gettradedetails/trade_id --> Displays trade details based on trade_id
    3. /searchtrade/?search=    --> It will search in counterparty, instrumentId, instrumentName, trader fields. It will return the result if searchtext matches with any of the listed fields.
    4. /filtercriteria?assetClass=&tradeType=&maxPrice=&minPrice=&start=&end=  --> It will display data meeting all the mentioned criteria of query params. start and end are date fields in (YYYY-DD-MM) format.
- Pagination has been handled at db level by setting limit(10).
- Ascending order_by sort is applied on trader column of trade table.