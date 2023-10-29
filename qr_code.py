from pyzbar.pyzbar import decode
from PIL import Image
import qrcode

def make_code(data: str):
    code = qrcode.make(data)
    return code

def decode_code(path: str) -> str:
    result = decode(Image.open(path))
    return result[0][0].decode()