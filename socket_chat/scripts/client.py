import prompt
import socket
import logging

from socket_chat.client import is_server

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

ADDRESS = ('localhost', 5000)


def run() -> None:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if is_server(ADDRESS, client_socket):
        while True:
            request = prompt.string('> ')
            client_socket.sendall(request.encode())
