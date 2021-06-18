import os
import sys
workdir, filename = os.path.split(os.path.realpath(__file__))
sys.path.append(os.path.join(workdir, '..', 'python_samples'))

sys.setrecursionlimit(10**6)