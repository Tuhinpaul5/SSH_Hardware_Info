from ssh import connect_ssh,disconnect_ssh

async def fetch_gpu():

    ssh = await connect_ssh()

    nvidia_smi_cmd = "nvidia-smi --query-gpu=uuid,name,temperature.gpu,power.draw,memory.total,memory.used,memory.free,utilization.gpu,utilization.memory --format=csv,noheader,nounits | "
    _, stdout, _ = ssh.exec_command(nvidia_smi_cmd)
    output = stdout.read().decode('utf-8').strip()
    lines = output.split('\n')
    parts = lines[0].split(',')
    id = parts[0]
    name = parts[1]
    temperature = parts[2]
    power = parts[3]
    memory_total = parts[4]
    memory_used = parts[5]
    memory_free = parts[6]
    gpu_utilization = parts[7]
    memory_utilization = parts[8]

    await disconnect_ssh()

    return {
            "id": id,
            "name": name,
            "temperature": float(temperature),
            "power": float(power),
            "memory_total": int(memory_total),
            "memory_used": int(memory_used),
            "memory_free": int(memory_free),
            "gpu_utilization": float(gpu_utilization),
            "memory_utilization": float(memory_utilization)
        }