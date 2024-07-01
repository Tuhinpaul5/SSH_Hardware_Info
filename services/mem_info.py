from ssh import connect_ssh, disconnect_ssh

async def fetch_mem():
        ssh = await connect_ssh()
        mem = """free -m | awk 'NR==2{print $2,$3,$4,$6,$7}'"""
        _, stdout, _ = ssh.exec_command(mem)
        output = stdout.read().decode('utf-8').strip()
        if output:
            total, used, free, buff_cache, available = output.split()

            await disconnect_ssh()

            return {
                "total": total,
                "used": used,
                "free": free,
                "buff_cache": buff_cache,
                "available": available
            }