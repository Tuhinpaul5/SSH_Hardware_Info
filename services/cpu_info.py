from ssh import connect_ssh,disconnect_ssh


async def fetch_cpu():
    ssh = await connect_ssh()

    cpu = """LANG=C lscpu | awk -F: '$1=="Model name" {print $2}'; awk '/processor/{core++} END{print core}' /proc/cpuinfo; vmstat 1 1 | awk 'NR==3{print $12}'; vmstat 1 2 | awk 'NR==4{print $15}'; cat /sys/class/thermal/thermal_zone*/temp | awk '{sum+=$1} END{print sum/NR/1000}'"""
    _, stdout, _ = ssh.exec_command(cpu)
    output = stdout.read().decode('utf-8').strip()
    lines = output.split('\n')
    info = lines[0]
    cores = lines[1]
    load = lines[2]
    usage = (100-int(lines[3]))
    temp = round(float(lines[4]), 1)
    
    await disconnect_ssh()

    return {
        "info": info,
        "cores": cores,
        "load": load,
        "usage": usage,
        "temp": temp
    }