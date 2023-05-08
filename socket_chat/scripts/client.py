#! /usr/bin/env python
import asyncio
import sys
import logging
from socket_chat.client import ChatClient

HOST: str = 'localhost'
PORT: int = 5000

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def main() -> None:
    client = ChatClient(HOST, PORT)
    try:
        asyncio.run(client.start())
    except KeyboardInterrupt:
        sys.exit(1)


if __name__ == '__main__':
    main()
