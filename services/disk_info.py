from ssh import connect_ssh, disconnect_ssh 

async def fetch_disk():
        ssh = await connect_ssh()
        sudo_password = "00"
        combined_command = (
        "vmstat -D | awk 'NR==1{print $1}'; "
        "vmstat -D | awk 'NR==2{print $1}'; "
        f"echo {sudo_password} | sudo -S iotop -o -b -n1 | grep '^Total' | awk '{{print $4 \"\\n\" $10}}'"
    )
        _, stdout, _ = ssh.exec_command(combined_command)
        output = stdout.read().decode('utf-8').strip()
        lines = output.split('\n')

        disk_num = lines[0]
        partition_num = lines[1]
        read_speed = lines[2]
        write_speed = lines[3]

        await disconnect_ssh()

        return {
            "disk_num": disk_num,
            "partition_num": partition_num,
            "read_speed": read_speed,
            "write_speed": write_speed
        }
    