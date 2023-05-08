import asyncio
import aioconsole


class ChatClient:
    def __init__(self, host, port):
        self._host = host
        self._port = port

    async def _read_data(self, reader):
        while True:
            data = await reader.read(1024)
            if not data:
                break
            print(f'Recieved: {data.decode()}')

    async def _send_messages(self, writer):
        while True:
            message = await aioconsole.ainput()
            writer.write(message.encode())
            await writer.drain()

    async def start(self):
        reader, writer = await asyncio.open_connection(self._host, self._port)
        try:
            asyncio.create_task(self._read_data(reader))
            await self._send_messages(writer)
        finally:
            writer.close()
