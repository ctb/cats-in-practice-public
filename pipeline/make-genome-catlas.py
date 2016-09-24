#! /usr/bin/env python
"""
Build a catlas from a collection of contigs/genomes.

This script will build a compact De Bruijn graph from the input contigs and
build a catlas from that.

"""
import os

from doit_utils import run_tasks
from spg_tasklib import *


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('dirname')
    parser.add_argument('inp_fasta', nargs='+')
    parser.add_argument('-r', '--radius', type=int, default=3)

    parser.add_argument('--clean', default=False, action='store_true')
    args = parser.parse_args()

    try:
        os.mkdir('temp')
    except OSError:
        pass
    #set_tempdir('./temp/')

    tasks = []
    tasks.append(task_walk_dbg(args.inp_fasta, args.dirname, label=True))
    tasks.append(task_build_catlas(args.dirname, args.radius))

    if args.clean:
        run_tasks(tasks, ['clean'])
    else:
        run_tasks(tasks, ['run'])


if __name__ == '__main__':
    main()
