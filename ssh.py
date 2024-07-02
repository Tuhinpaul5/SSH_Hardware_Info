import paramiko    

host = '192.168.0.103' # Ip of the server
port = 22
username = 'ubuntu'   # Username
password = '00'       # Password

async def connect_ssh():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port=22, username='ubuntu', password='00')
    return ssh

async def disconnect_ssh():
    ssh = paramiko.SSHClient()
    ssh.close()