from ssh import connect_ssh,disconnect_ssh

async def fetch_basics():
        ssh = await connect_ssh()
        basics = """uname -r && hostname && uptime | awk -F ',' '{print $1}' | sed 's/^ //g'"""
        _, stdout, _ = ssh.exec_command(basics)
        output = stdout.read().decode('utf-8').strip()
        lines = output.split('\n')
        version = lines[0]
        hostname = lines[1]
        uptime = lines[2]

        await disconnect_ssh()

        return {
            "hostname": hostname,
            "version": version,
            "Uptime": uptime
        }