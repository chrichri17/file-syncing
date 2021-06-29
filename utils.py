import hashlib
import zlib

BLOCK_SIZE = 4096 # 2**12

def md5_chunk(chunk):
    m = hashlib.md5()
    m.update(chunk.encode('utf-8'))
    return m.hexdigest()


def adler32_chunk(chunk):
    return zlib.adler32(chunk.encode('utf-8'))