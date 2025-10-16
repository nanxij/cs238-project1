import sys

import networkx as nx
import pandas as pd


def write_gph(dag, idx2names, filename):
    with open(filename, 'w') as f:
        for edge in dag.edges():
            f.write("{}, {}\n".format(idx2names[edge[0]], idx2names[edge[1]]))


def compute(infile, outfile):
    # Read in data / init
    data = pd.read_csv(infile)
    vars = list(data.columns)
    n = len(vars) #number of variables
    dag = nx.DiGraph()

    # Fix an ordering of nodes
    fixed_order = list(range(n))

    # Iterate though nodes
    
    # Iterate through parent possibilities
    # Add parents to current node
    pass


def main():
    if len(sys.argv) != 3:
        raise Exception("usage: python project1.py <infile>.csv <outfile>.gph")

    inputfilename = sys.argv[1]
    outputfilename = sys.argv[2]
    compute(inputfilename, outputfilename)


if __name__ == '__main__':
    main()
