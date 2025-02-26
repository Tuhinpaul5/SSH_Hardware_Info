### 0. Clone the repository.
First clne the repository then follow the steps below to test the functionality.

### 1. Install all the required imports

```
pip install -r .\requirements.txt
```
### 2. edit ssh.py file

```
host = 'XXX.XXX.XXX.XXX' # Ip of the server machine
port = XX
username = 'xxxxx'   # Username
password = 'xxxxx'       # Your password
```

### 3. Run the app

```
python.\main.py
``` 

### 4. Test the API endpoints

```
http://localhost:8000/get/basics
http://localhost:8000/get/cpu
http://localhost:8000/get/memory
http://localhost:8000/get/disk
http://localhost:8000/get/network
http://localhost:8000/get/procs
```
