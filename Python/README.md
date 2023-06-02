# CAMPUS LAUNDRY

## Backend Python Flask

### Setup

 - Python 3 Latest Version
 - Set Python Interpreter
 - Install all the `requirements.txt` dependencies
    ```commandline 
    pip install -r requirements.txt
    ```
 - set .env file to the Interpreter so that database username and password can be access through it
 - Allow Pycharm to run on public networks for accessing to act as server within the network
 - Run the `main.py` with python so the application bootup on [localhost:8090](http://localhost:8090)
   - if allowed on public networks then a new url `http://{your_ip_address}/`
 - The URL home page will display the `home.html` in `templates`
 - Application API's can be tested using [Swagger UI](http://localhost:8090/campus-laundary/ui/)

### API Implementation

 - Create respective class with `get/post` in the `api` folder 
 - Add respective API validation in `specs` folder