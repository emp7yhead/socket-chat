#! /usr/bin/env python
import asyncio
import logging
import sys

from socket_chat.server import ChatServer

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

HOST: str = 'localhost'
PORT: int = 5000


def main() -> None:
    chat = ChatServer(HOST, PORT)
    try:
        asyncio.run(chat.run())
    except KeyboardInterrupt:
        sys.exit(1)


if __name__ == '__main__':
    main()
