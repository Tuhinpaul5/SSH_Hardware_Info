from ssh import connect_ssh, disconnect_ssh

async def fetch_net():
        ssh = await connect_ssh()
        net = """cat /proc/net/dev | tail -n +3 | awk '{print $1,$2,$10}'"""
        _, stdout, _ = ssh.exec_command(net)
        output = stdout.read().decode('utf-8').strip()
        lines = output.split('\n')

        network_data = {}
        for line in lines:
            parts = line.split()
            interface_name = parts[0].strip(':')
            receive_bytes = int(parts[1])
            transmit_bytes = int(parts[2])

            await disconnect_ssh()

            network_data[interface_name] = {
                "receive_bytes": receive_bytes,
                "transmit_bytes": transmit_bytes
            }

        return network_data
    