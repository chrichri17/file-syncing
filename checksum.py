import collections
import utils

# Checksum objects
# ----------------

Signature = collections.namedtuple('Signature', 'md5 adler32')

class Chunk:
    """ Data structure that holds rolling checksums for a file B. """

    def __init__(self):
        self.chunks = []
        self.chunk_sigs = {}
    

    def append(self, sig):
        self.chunks.append(sig)
        self.chunk_sigs.setdefault(sig.adler32, {})
        self.chunk_sigs[sig.adler32][sig.md5] = len(self.chunks) - 1
    

    def get_chunk(self, chunk):
        adler32 = self.chunk_sigs.get(utils.adler32_chunk(chunk))
        if adler32:
            return adler32.get(utils.md5(chunk))
        return
    

    def __getitem__(self, key):
        return self.chunks[key]
    

    def __len__(self):
        return len(self.chunks)


# Build chunks from a file
# ------------------------
def file_checksums(filename):
    chunks = Chunk()
    with open(filename) as file:
        while True:
            chunk = file.read(utils.BLOCK_SIZE)
            if not chunk:
                break

            chunks.append(
                Signature(
                    md5=utils.md5_chunk(chunk),
                    adler32=utils.adler32_chunk(chunk)
                )
            )
    return chunks
