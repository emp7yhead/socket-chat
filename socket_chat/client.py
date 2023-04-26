import logging

logger = logging.getLogger(__name__)


def is_server(addr, socket):
    try:
        socket.connect(addr)
        logger.info('Connection established')
    except OSError:
        logger.info('Server not available')
        return False
    return True
