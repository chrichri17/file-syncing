import utils
from checksum import file_checksums

# Get the BLOCK_SIZE cunks in file_b that are in file_a
# -----------------------------------------------------

# The algorithm.
# -------------------------------------------------------------------------+
#     1. create rolling checksums for file_b                               |
#     2. for each chunk in file_a, determine if chunk is already in file_b |
#         a. If so:                                                        |
#             i. return the index of that chunk                            |
#             ii. move the read head by the size of a chunk                |
#         b. If not:                                                       |
#             i. return the next byte                                      |
#             ii. move the read head by 1 byte                             |
#     3. start over at 2 until you're out of file to read                  |
# -------------------------------------------------------------------------+
def _get_block_list(file_a, file_b):
    checksums = file_checksums(file_b)
    blocks = []
    offset = 0
    with open(file_a) as file:
        while True:
            chunk = file.read(utils.BLOCK_SIZE)
            if not chunk:
                break

            chunk_number = checksums.get_chunk(chunk)
            if chunk_number:
                offset += utils.BLOCK_SIZE
                blocks.append(chunk_number)
            else:
                offset += 1
                blocks.append(chunk[0])
                file.seek(offset)
    return blocks

# Compute the rsync algorithm
# ---------------------------
def rsync(file_a, file_b):
    output_str = []
    with open(file_b) as file:
        for block in _get_block_list(file_a, file_b):
            if isinstance(block, int):
                file.seek(block * utils.BLOCK_SIZE)
                output_str.append(file.read(utils.BLOCK_SIZE))
            else:
                output_str.append(block)
    return ''.join(output_str)

