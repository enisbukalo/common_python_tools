import sys
import asyncio
import subprocess
import time

from pathlib import Path

this_file_location = Path(__file__).parent.absolute()
launch_file = this_file_location.joinpath("launch_socket_server.py")
sys.path.append(this_file_location.as_posix())

# process = subprocess.Popen(["python", launch_file.as_posix()])
# time.sleep(2)

loop = asyncio.get_event_loop()


class SocketClient:
    def __init__(self) -> None:
        self._last_message = None
        self._last_response = None

    @property
    def last_message(self):
        return self._last_message

    @property
    def last_response(self):
        return self._last_response

    async def send(self, message: str) -> None:
        print(f"Client = Sending Data: {message}")
        self.writer.write(message.encode())
        self._last_response = message
        response = await self.reader.read(1024)
        print(f"Client = Received Response: {response.decode()}")
        self._last_message = response.decode()

    async def start_client(self) -> None:
        self.reader, self.writer = await asyncio.open_connection("localhost", 6000)


# def test_socket_server():
client = SocketClient()
loop.run_until_complete(client.start_client())
loop.run_until_complete(client.send("Foo"))

print(client.last_message)
print(client.last_response)

# process.terminate()
