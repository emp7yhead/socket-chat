def decode_request(request: bytes) -> str:
    decoded_request = request.decode()
    return decoded_request.rstrip('\n')
