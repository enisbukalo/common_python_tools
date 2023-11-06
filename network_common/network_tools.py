import subprocess
import re
import os


def ping_check(ip_to_check: str, ping_count: int = 1) -> bool:
    """Responsible determining if IP is reachable.

    Args:
        ip_to_check (str): IP Address we want to ping.
        ping_count (int, optional): Times we want to ping IP. Defaults to 1.

    Returns:
        bool: True if IP is reachable, otherwise False.
    """
    cmd = "-n" if os.name =="nt" else "-c"
    output = subprocess.Popen(f"ping {ip_to_check} {cmd} {ping_count}", stdout=subprocess.PIPE, encoding="utf-8")

    data = ""
    for line in output.stdout:
        data = data + line

    return False if len(re.findall("TTL", data)) == 0 else True
