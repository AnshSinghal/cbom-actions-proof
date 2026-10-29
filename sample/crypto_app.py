"""Synthetic CI sample. Not a secret and not production code."""
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

key = b"0123456789abcdef"
cipher = Cipher(algorithms.AES(key), modes.ECB())
