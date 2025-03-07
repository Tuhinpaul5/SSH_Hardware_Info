## INFO
This project is designed to provide FastAPI endpoints that fetch hardware information of SSH servers.

### 0. Clone the repository.
First, clone the repository then follow the steps below to test the functionality.

### 1. Install all the required imports
Run the following command to install all required dependencies:
```
pip install -r .\requirements.txt
```
### 2. edit ssh.py file
Modify the ssh.py file with your server details:
```
host = 'XXX.XXX.XXX.XXX' # Ip of the server machine
port = 22
username = 'xxxxx'   # Username of the server machine
password = 'xxxxx'   # password of the server machine
```

### 3. Run the app
Start the application by running:
```
python.\main.py
``` 

### 4. Test the API endpoints
Once the application is running, test the API by accessing the following endpoints in your browser or using a tool like curl or Postman:
```
http://localhost:8000/get/basics
http://localhost:8000/get/cpu
http://localhost:8000/get/memory
http://localhost:8000/get/disk
http://localhost:8000/get/network
http://localhost:8000/get/procs
```
