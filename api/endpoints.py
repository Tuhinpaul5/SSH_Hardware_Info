from fastapi import APIRouter
from services.cpu_info import fetch_cpu
from services.gpu_info import fetch_gpu
from services.basics_info import fetch_basics
from services.mem_info import fetch_mem
from services.disk_info import fetch_disk
from services.net_info import fetch_net
from services.procs_info import fetch_procs

router = APIRouter()

@router.get("/cpu")
async def cpu():
    return {"cpu": await fetch_cpu()}

@router.get("/gpu")
async def gpu():
    return {"gpu": await fetch_gpu()}

@router.get("/basics")
async def basics():
    return {"basics": await fetch_basics()}

@router.get("/mem")
async def mem():
    return {"memory": await fetch_mem()}

@router.get("/disk")
async def disk():
    return {"disk": await fetch_disk()}

@router.get("/net")
async def net():
    return {"net": await fetch_net()}

@router.get("/procs")
async def procs():
    return {"procs": await fetch_procs()}