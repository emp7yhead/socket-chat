import asyncio
import logging


class ChatServer:

    def __init__(self, host, port):
        self._connections = set()
        self._host = host
        self._port = port

    async def handle_client(self, reader, writer):
        conn = (reader, writer)
        writer.write(b'welcome to chat!')
        self._connections.add(conn)
        await self._broadcast_data(b'New connection', writer)
        logging.info(f'{conn} connected')
        try:
            while True:
                data = await reader.read(1024)
                if not data:
                    break
                await self._broadcast_data(data, writer)
        finally:
            writer.close()
            self._connections.remove(conn)

    async def _broadcast_data(self, data, sender_writer):
        for _, c_writer in self._connections:
            if c_writer != sender_writer:
                c_writer.write(data)
                await c_writer.drain()

    async def run(self):
        server = await asyncio.start_server(
            self.handle_client,
            self._host,
            self._port
        )
        logging.info(f'Start server on {self._host}:{self._port}')
        async with server:
            await server.serve_forever()
