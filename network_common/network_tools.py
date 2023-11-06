import subprocess
import re
import os


def ping_check(ip_to_check: str, ping_count: int = 1) -> bool:
    """
    Ping a given IP address and check if the ping is successful.

    Args:
        ip_to_check (str): The IP address to ping.
        ping_count (int, optional): The number of pings to send. Defaults to 1.

    Returns:
        bool: True if the ping is successful, False otherwise.
    """
    cmd = "-n" if os.name =="nt" else "-c"
    output = subprocess.Popen(f"ping {ip_to_check} {cmd} {ping_count}", stdout=subprocess.PIPE, encoding="utf-8")

    data = ""
    for line in output.stdout:
        data = data + line

    return False if len(re.findall("TTL", data)) == 0 else True
