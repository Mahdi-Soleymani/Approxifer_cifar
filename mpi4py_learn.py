from mpi4py import MPI
import numpy as np
import random
from array import array
import math
import time
import sys
import pickle as pickle


comm=MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
if rank == 0:
    data = {'a': 7, 'b': 3.14}
    comm.send(data, dest=1, tag=11)
elif rank == 1:
    data = comm.recv(source=0, tag=11)
print("Hello world from rank", str(rank), "of", str(size))