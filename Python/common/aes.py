import array
import base64

from Crypto.Cipher import AES
from dotenv import dotenv_values

env_values = dotenv_values()

BLOCK_SIZE = 16


def get_common_key():
    key = env_values['SECRET']
    return key


def get_iv():
    iv_str = env_values['IV']
    iv_int_items = list(map(lambda x: int(x), iv_str.split(",")))
    iv = array.array('B', iv_int_items)
    return iv


def pad(the_str, block_size):
    """Padding plain text.

    :param str the_str: The string to pad.
    :param block_size: Block size.
    :return: Padded string.
    """
    left_count = block_size - len(the_str) % block_size
    padding = bytes([left_count] * left_count)
    return the_str.encode() + padding


def unpad(padded_data, block_size):
    """Unpad the padded data.

    :param padded_data: The padded data.
    :param block_size: Block size.
    :return: Unpadded data.
    """
    padding_length = padded_data[-1]
    if padding_length <= 0 or padding_length > block_size:
        # Invalid padding length
        return padded_data

    expected_padding = bytes([padding_length] * padding_length)
    if padded_data[-padding_length:] != expected_padding:
        # Invalid padding bytes
        return padded_data

    return padded_data[:-padding_length]


def encrypt(plain_text):
    """Encrypt the plain text.

    :param plain_text: Plain text to be encrypted.
    :return: Cipher text as a string.
    """
    key = get_common_key()
    if key:
        aes = AES.new(key.encode(), AES.MODE_CBC, bytes(get_iv()))
        encrypted_data = aes.encrypt(pad(plain_text, BLOCK_SIZE))
        return base64.b64encode(encrypted_data).decode()
    else:
        return ''


def decrypt(cipher_text):
    """Decrypt the cipher text.

    :param cipher_text: Cipher text to be decrypted.
    :return: Decrypted plain text as a string.
    """
    key = get_common_key()
    if key:
        aes = AES.new(key.encode(), AES.MODE_CBC, bytes(get_iv()))
        decrypted_data = aes.decrypt(base64.b64decode(cipher_text))
        return unpad(decrypted_data, BLOCK_SIZE).decode()
    else:
        return ''
