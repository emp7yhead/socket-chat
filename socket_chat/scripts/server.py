import socket
import logging

from socket_chat.server import decode_request

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

ADDRESS = ('localhost', 5000)


def run() -> None:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(ADDRESS)
    server_socket.listen()
    logger.info('init server socket')

    while True:
        client_socket, addr = server_socket.accept()
        logger.info(f'Get connection from {addr}')
        while True:
            request = client_socket.recv(4096)
            logger.info(request)
            if not request:
                break
            msg = decode_request(request)
            client_socket.send(f'{addr[0]} send message: {msg}\n'.encode())
        client_socket.close()


if __name__ == '__main__':
    run()
