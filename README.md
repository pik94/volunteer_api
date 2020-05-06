#### Description
This educational project is the forth task of an online [course](https://academy.stepik.org/flask). 
It's a simple API for searching a volunteer in a town Visotsk. 

#### Install
1. Create virtualenv and activate it:
    ```shell script
    python3.7 -m venv venv && source ./venv/bin/activate
    ```
2. Install required packages:
   ```shell script
    pip install -r requirements.txt
   ```

#### Running
1.  Export necessary environment variables:
    ```shell script
    export DB_USER=user_1 DB_PASSWORD=super_secret_pass ADMIN_LOGIN=admin@admin.com ADMIN_PASSWORD=12345
    ```
    A list of variables:
    | Variable | Require | Default | Description|
    | ------ | ------ | ------ | ----------|
    | DB_TYPE | no | sqlite | Database type. Now SQLite and PostgreSQL are supported. |
    | DB_HOST | no | localhost | A database host. |
    | DB_PORT | no | 5432 | A database port. |
    | DB_USER | yes (no for SQLite) | user | A database user. Required to be set if it's used no SQLite database. |
    | DB_PASSWORD | yes (no for SQLite) | password | A database user. Required to be set if it's used no SQLite database. |
    | DB_NAME | no  | volunteers.db | A database name. If you use SQLite use an absolute or relative path to the database. |
    | SERVER_NAME | no | localhost | An address where the server will be deployed. |
    | SERVER_PORT | no | 5000 | A port that the server will listen. |

2. Create tables
    ```shell script
    flask db upgrade
    ```
   
3. Fill tables
    ```shell script
    python init_data.py -i /path/to/a/json/file
    ```

4.  For running on a production server:
    ```shell script
    python app.py
    ```

    Running in a debug mode:
    ```shell script
    python app.py -d
    ```

    To see all keys for running, type:
    ```shell script
    python app.py -h
    ```

#### Usage
API methods:
| URI | Method | Response Format | Description |
| ------ | ------ | ------ | ------ |
| /districts | GET | JSON | A list of all available districts. |
| /districts/<int:district_id> | GET | JSON | Information about a selected district. |
| /streets | GET | JSON | A list of streets. |
| /streets/<int:street_id> | GET | JSON | Information about a selected street. |
| /streets&district=<int:id> | GET | JSON | A list of streets for a selected district. |
| /volunteers/ | GET | JSON | A list of all available volunteers. |
| /volunteers/<int:volunteer_id> | GET | JSON | Information about a selected volunteer. |
| /volunteers&streets=<int:id> | GET | JSON | A list of volunteers for a selected street. |
| /requests | POST | JSON | This method is for creating a request. Example of data for requesting <br/> { <br/> "district": 2, <br/> "street": 41, <br/> "volunteer": 5, <br/> "address": "Lesnaya street", <br/> "name": "Ivan", <br/> "surname": "Ivanov", <br/> "phone": "+72224234422", <br/> "text": "Help me" <br/> }|