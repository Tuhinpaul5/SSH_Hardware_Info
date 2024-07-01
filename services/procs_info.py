from ssh import connect_ssh, disconnect_ssh 

async def fetch_procs():
    ssh = await connect_ssh()

    procs_cmd = """ps --no-headers -eo pid,%cpu,%mem,cmd --sort=-%cpu | head -n 10"""
    awk_cmd = """awk '{print $1, $2, $3, $4}'"""
    command = f"{procs_cmd} | {awk_cmd}"
    
    _, stdout, _ = ssh.exec_command(command)
    output = stdout.read().decode('utf-8').strip()
    lines = output.split('\n')

    process_list = []
    for line in lines:
        parts = line.split()
        if len(parts) < 4:
            continue

        try:
            pid = int(parts[0])
            cpu_percent = float(parts[1])
            mem_percent = float(parts[2])
            command = ' '.join(parts[3:])
            
            process_info = {
                "pid": pid,
                "name": command.split()[0],
                "cpu_percent": cpu_percent,
                "memory_percent": mem_percent
            }
            process_list.append(process_info)
        except ValueError:
            continue

    await disconnect_ssh()

    return {"processlist": process_list}