#! /usr/bin/env python

import argparse
import numpy
from klepto import archives

parser = argparse.ArgumentParser()
parser.add_argument("--input-file", default="tmp_spotlight/solution_alumina.pkl")
opts = parser.parse_args()

# read solutions
arch = archives.file_archive(opts.input_file)
arch.load()

# print information about each local solver
keys = arch.keys()
print(keys)
nsolvers = 0
nsolvers_terminated = 0
for key in keys:
    if key == "names":
        continue
    sol = arch[key]
    print("The key is", key)
    print("The shape of the parameters array is", numpy.array(sol[0]).shape)
    print("The shape of the solution array is", numpy.array(sol[1]).shape, sol[1])
    print("The best parameters are:")
    for i, x in enumerate(sol[2]):
        print(arch["names"][i], x)
    print("The best cost function value is", sol[3])
    print("The state of this local optimization is", sol[4])
    print()
    nsolvers += 1
    nsolvers_terminated += 1 if sol[4] == None else 0

# print aggregate information about ensemble of local solvers
print("{} of {} local solvers have terminated".format(nsolvers_terminated, nsolvers))

# for reference
#from spotlight import archive
#arch = archive.Arch.read_data(opts.input_file)