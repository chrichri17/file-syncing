# This package is built using the official description of `rsync` at:
# https://www.andrew.cmu.edu/course/15-749/READINGS/required/cas/tridgell96.pdf
# and a poorly implementation in python at:
# https://tylercipriani.com/blog/2017/07/09/the-rsync-algorithm-in-python/

import rsync

if __name__ == '__main__':
    rsync.rsync("./ressources/bar.txt", "./ressources/foo.txt")
    rsync.rsync("./ressources/baz.txt", "./ressources/foo.txt")