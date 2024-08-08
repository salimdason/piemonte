__version__ = "1.0.0"

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import platform
import psutil
import getpass
import socket
import time


class SystemInformation:

    def __init__(self):
        pass

    @staticmethod
    def get_system_info():
        user = getpass.getuser()
        cpu = platform.processor()
        cores = psutil.cpu_count(logical=False)
        memory = psutil.virtual_memory().total / (1024 ** 3)  # Convert bytes to GB
        os_name = platform.system()

        if os_name == "Darwin":
            os_name = "macOS"

        os_info = f"{os_name} {platform.release()} ({platform.architecture()[0]})"
        hostname = socket.gethostname()
        uptime_seconds = time.time() - psutil.boot_time()
        uptime_hours = uptime_seconds / 3600
        ip_address = socket.gethostbyname(hostname)
        disk_usage = psutil.disk_usage('/')
        return user, cpu, cores, memory, os_info, hostname, uptime_hours, ip_address, disk_usage, __version__

    @staticmethod
    def display_info():
        user, cpu, cores, memory, os_info, hostname, uptime_hours, ip_address, disk_usage, script_version = SystemInformation.get_system_info()

        table = Table(show_header=True, header_style="bold magenta", box=None)
        table.add_column("Attribute", style="dim", width=25)
        table.add_column("Value", width=45, justify="right")

        table.add_row("User", user)
        table.add_row("CPU", cpu)
        table.add_row("Cores", str(cores))
        table.add_row("Memory (GB)", f"{memory:.2f}")
        table.add_row("OS", os_info)
        table.add_row("Hostname", hostname)
        table.add_row("Uptime (hours)", f"{uptime_hours:.2f}")
        table.add_row("IP Address", ip_address)
        table.add_row("Free Disk Space (GB)", f"{disk_usage.free / (1024 ** 3):.2f}")
        table.add_row("Script Version", script_version)

        console = Console()
        console.print(Panel.fit(table, title="System Information", subtitle=" @author: S. Dason"))


if __name__ == "__main__":
    SystemInformation.display_info()
