from services.basics_info import fetch_basics
from services.cpu_info import fetch_cpu
from services.gpu_info import fetch_gpu
from services.mem_info import fetch_mem
from services.disk_info import fetch_disk
from services.net_info import fetch_net
from services.procs_info import fetch_procs

async def fetch_all():
        return {
            "basics": await fetch_basics(),
            "cpu": await fetch_cpu(),
            "gpu": await fetch_gpu(),
            "memory": await fetch_mem(),
            "disk": await fetch_disk(),
            "network": await fetch_net(),
            "processes": await fetch_procs()
        }