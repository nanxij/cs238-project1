import sys
import numpy as np
import pandas as pd
import networkx as nx
from scipy.special import gammaln

def write_gph(dag, idx2names, filename):
    with open(filename, 'w') as f:
        for edge in dag.edges():
            f.write("{}, {}\n".format(idx2names[edge[0]], idx2names[edge[1]]))

def k2Score(data, node, parents):

    #change all int defined nodes to column name defined nodes
    if isinstance(node, int):
        node = data.columns[node]
    parents = [data.columns[p] if isinstance(p, int) else p for p in parents]

    # possible values of the node
    node_values = data[node].unique()
    r_i = len(node_values)

    # group by parent configurations
    if parents:
        grouped = data.groupby(parents)
    else:
        grouped = [((), data)]

    #init score to 0
    score = 0.0
    #uniform Dir
    alpha = 1.0

    for _, subset in grouped:
        counts = subset[node].value_counts()
        N_ijk = np.array([counts.get(val, 0) for val in node_values])
        N_ij = N_ijk.sum()
        # add every term to running baysian score
        score += (
            np.sum(gammaln(N_ijk + alpha))
            - gammaln(N_ij + r_i * alpha)
            + gammaln(r_i * alpha)
            - r_i * gammaln(alpha)
        )

    return score


def compute(infile, outfile):
    max_parents = 3
    # read in data / init
    data = pd.read_csv(infile)
    vars = list(data.columns)
    n = len(vars) #number of variables
    idx2names = {i: name for i, name in enumerate(vars)}
    dag = nx.DiGraph()

    # fix an ordering of nodes
    fixed_order = list(range(n))

    # iterate though nodes
    for i in fixed_order[:n]:
        node = fixed_order[i]
        parents = []
        top_score = k2Score(data, node, parents)
        # iterate through potential parents
        for j in range(i):
            parents_temp = parents + [j]
            score_temp = k2Score(data, node, parents_temp)
            if len(parents) == max_parents:
                break
            elif score_temp > top_score:
                parents += [j]
                top_score = score_temp
        # add parents to current node
        for parent in parents:
            dag.add_edge(parent, node)
    # write off
    write_gph(dag, idx2names, outfile)
    pass


def main():
    if len(sys.argv) != 3:
        raise Exception("usage: python project1.py <infile>.csv <outfile>.gph")

    inputfilename = sys.argv[1]
    outputfilename = sys.argv[2]
    compute(inputfilename, outputfilename)


if __name__ == '__main__':
    main()
