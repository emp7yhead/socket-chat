import pytest
from unittest.mock import AsyncMock, Mock, patch
from socket_chat.server import ClientHandler, ChatServer


@pytest.mark.asyncio
async def test_client_handler_sends_welcome_message():
    reader = AsyncMock()
    reader.read.side_effect = [b'some data', b'']
    writer = Mock()
    connections = set()
    client_handler = ClientHandler(reader, writer, connections)
    await client_handler.handle()
    writer.write.assert_called_once_with(b'welcome to chat!')


@pytest.mark.asyncio
async def test_chat_server_handle_client():
    with patch(
        'socket_chat.server.ClientHandler.handle',
        new_callable=AsyncMock,
    ) as mock_handler:
        chat_server = ChatServer('localhost', 1234)
        await chat_server.handle_client(Mock(), Mock())
        mock_handler.assert_called_once_with()


@pytest.mark.asyncio
async def test_chat_server_run():
    with patch('asyncio.start_server') as mock_start_server:
        chat_server = ChatServer('localhost', 1234)
        await chat_server.run()
        mock_start_server.assert_called_once_with(
            chat_server.handle_client,
            'localhost',
            1234
        )
