import asyncio
from logging_common.logger import Logger


class SocketServer:
    def __init__(self, host: str = "localhost", port: int = 6000) -> None:
        self._host = host
        self._port = port
        self._max_read_bytes = 1024
        self._last_message = None
        self._last_response = None
        self.logger = Logger(log_to_file=False, logger_name="SocketServer")

    @property
    def last_message(self):
        return self._last_message

    @property
    def last_response(self):
        return self._last_response

    async def _server(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        while True:
            data = await reader.read(self._max_read_bytes)
            if not data:
                break
            self._last_message = data.decode()
            self.logger.info(f"Received Data: {self._last_message}")
            writer.write(data)
            await writer.drain()
            self._last_response = data.decode()
            self.logger.info(f"Responded With: {self._last_response}")
        writer.close()

    async def start_server(self):
        self.logger.info(f"Starting Socket Server With {self._host}:{self._port} ")
        server = await asyncio.start_server(self._server, self._host, self._port)
        await server.serve_forever()
        server.close()
