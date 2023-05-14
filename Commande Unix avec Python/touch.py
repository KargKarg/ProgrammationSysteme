import os
import sys

if sys.argv[1] in os.listdir():
    os.utime(sys.argv[1])
else:
    os.close(os.open(sys.argv[1], os.O_CREAT))
