# SchoolifyAPI
A student management API using either Flask- RESTX or Flask-Smorest framework in Python. The purpose of this project is to help you develop your skills in creating RESTful APIs using these frameworks


## Starting and Using the Project
### Requirements
You must have the following tools ready to run this project
- Python3
- Virtual Environment

### Backend

Before you get started, set up your virtual environment

```
python -m virtualenv myenv
myenv/Scripts/activate
```
Once your virtual environment is setup and running, install the required dependencies by running:

```bash
pip install -r requirements.txt
```

##### Run the Server
From within the `schoolify-api` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```
set FLASK_APP=api/
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.


This will the start the server at http://localhost:5000

## API Reference

### Getting Started
- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:5000/`


### Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```
The API will return three error types when requests fail:
- 400: Bad Request
- 404: Resource Not Found
- 422: Not Processable 
- 405: Method Not Allowed
- 500: Internal Server Error 

### Endpoints 
#### POST /auth/signup
- General:

    - Signs up an Admin User

- `curl http://127.0.0.1:5000/auth/signup`

``` {
    "Sign Up": 
        {
            "name": "string",
            "email": "string",
            "username": "string",
            "password": "string"
        },
    "success": true,
}

```
### GET /login
- General:

    - Logs in Admin User

-`curl http://127.0.0.1:5000/auth/login`

```{
    "Login":
        {
            "email": "string",
            "password": "string"
        },

        {
            "access_token": "string",
            "refresh_token":string"
        }
}
