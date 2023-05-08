import asyncio
import logging


class ChatServer:

    def __init__(self, host, port):
        self._connections = set()
        self._host = host
        self._port = port
        self.handler = ClientHandler

    async def handle_client(self, reader, writer):
        handler = self.handler(reader, writer, self._connections)
        await handler.handle()

    async def run(self):
        server = await asyncio.start_server(
            self.handle_client,
            self._host,
            self._port
        )
        logging.info(f'Start server on {self._host}:{self._port}')
        async with server:
            await server.serve_forever()


class ClientHandler:
    def __init__(self, reader, writer, connections):
        self._reader = reader
        self._writer = writer
        self._connections = connections

    @property
    def address(self):
        return self._writer.get_extra_info('peername')

    async def handle(self):
        conn = (self._reader, self._writer)
        self._writer.write(b'welcome to chat!')
        self._connections.add(conn)
        await self._broadcast_data(b'New connection')
        logging.info(f'{self.address} connected')
        try:
            while True:
                data = await self._reader.read(1024)
                logging.debug(f'{self.address} send {data}')
                if not data:
                    break
                await self._broadcast_data(data)
        finally:
            self._writer.close()
            self._connections.remove(conn)

    async def _broadcast_data(self, data):
        for _, c_writer in self._connections:
            if c_writer != self._writer:
                c_writer.write(data)
                await c_writer.drain()
