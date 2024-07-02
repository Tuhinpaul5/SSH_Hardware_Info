### 1. Install all the required imports

```
pip install -r .\requirements.txt
```
### 2. edit ssh.py file

```
host = '192.168.0.103' # Ip of the server machine
port = 22
username = 'ubuntu'   # Username
password = '00'       # Your password
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