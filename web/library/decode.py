import base64


def decode_password(string):
    base64_bytes = string.encode('ascii')
    string_bytes = base64.b64decode(base64_bytes)
    string = string_bytes.decode('ascii')
    return string
