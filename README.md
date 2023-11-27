#### FLASK CV-Generator app

### Terminal commands
Note: make sure you have `pyenv` installed

    Initial installation of python version: `make init-python`
    
    To init virtualenv: `make init-virtualenv`
    
    To enter virtualenv: `make shell`
    
    To start the app: `make run`
    
    To clean virtualenv: `make clean`

### Using postman ###

    Use the following url on Postman:
    http://127.0.0.1:8000/

### Endpoints ###

1. `/education`
2. `/personal`
3. `/experience`
4. `/recommendations`


### TO DO ###
1. Add swagger documentation
2. Use Pydantic for data validation
3. Add a global exception handler