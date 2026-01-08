import psutil

def get_system_status():
    get_cpu_usage = psutil.cpu_percent(interval=1)
    get_mem_usage = psutil.virtual_memory().percent
    get_disk_usage = psutil.disk_usage("/").percent

    cpu_threshold =10

    status="High CPU" if get_cpu_usage > cpu_threshold else "Healthy"

    response = {
        "CPU_Usage":get_cpu_usage,
        "Memory_Usage": get_mem_usage,
        "Disk_Usage": get_disk_usage,
        "system_status": status
    }

    return response