from ssh import connect_ssh,disconnect_ssh


async def fetch_cpu():
    ssh = await connect_ssh()

    cpu = """LANG=C lscpu | awk -F: '$1=="Model name" {print $2}'; awk '/processor/{core++} END{print core}' /proc/cpuinfo; uptime | sed 's/,/ /g' | awk '{for(i=NF-2;i<=NF;i++)print $i }' | xargs; vmstat 1 1 | awk 'NR==3{print $11}'; vmstat 1 1 | awk 'NR==3{print $12}'; vmstat 1 2 | awk 'NR==4{print $15}'"""
    _, stdout, _ = ssh.exec_command(cpu)
    output = stdout.read().decode('utf-8').strip()
    lines = output.split('\n')
    info = lines[0]
    cores = lines[1]
    interrupt = lines[2]
    load = lines[3]
    usage = lines[4]

    await disconnect_ssh()

    return {
        "info": info,
        "cores": cores,
        "interrupt": interrupt,
        "load": load,
        "usage": usage
    }