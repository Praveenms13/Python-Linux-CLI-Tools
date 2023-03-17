# This concept is inherited from c language so it might be difficult to understand for python developers. But it is very useful for python developers to share data between processes. It is very useful for multiprocessing.

from multiprocessing import shared_memory
from mediaInfo.lib.Arguement import Arguement
import sys

args = Arguement(sys.argv)

if not args.hasOptions(["--shm", "--pname"]):
    print(
        "Usage: {} python3 V_SharedMemory.py --shm=shm name --pname=process [- master or slave]"
    )
    exit(-1)

if args.getOptionValue("--pname") == "master":
    shm = shared_memory.SharedMemory(name=args.getOptionValue('--shm'), create=True, size=1024)
    # name is the name of shared memory and it is used to access the shared memory
else:
    shm = shared_memory.SharedMemory(name=args.getOptionValue('--shm'))
    # name is the name of shared memory and it is used to access the shared memory

def writeshmString(shm, data):
    print("Writing to shared memory...")
    buff_a = shm.buf
    buff_a[: len(data)] = bytearray(data, "utf-8")
    print('Process: ', args.getOptionValue("--pname"), ' wrote: ', data, ' to shared memory')
    # values can only store upto 8 bytes 2^8 = 256
    # so we need to convert string to bytes
    # and then store it in shared memory

def readshmString(shm):
    buff_a = shm.buf
    return str(buff_a, "utf-8").rstrip("\x00")


while True :
    choice = input("1. Read from shared memory\n2. Write to shared memory\n3. Exit\nChoose >> ")
    if choice == "1":
        print(readshmString(shm))
    elif choice == "2":
        data = input("Enter data to write to shared memory >> ")
        writeshmString(shm, data)
    elif choice == "3":
        break