#! /usr/bin/env python
"""
Build a catlas from a set of real reads.

This script error trim a set of real reads, build a compact De Bruijn
graph from them, and build a catlas from that.
"""
import os

from doit_utils import run_tasks
from spg_tasklib import *


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('dirname')
    parser.add_argument('inp_reads', nargs='+')
    parser.add_argument('-r', '--radius', type=int, default=3)
    parser.add_argument('-M', '--memory', type=float, default=1e9)

    parser.add_argument('--clean', default=False, action='store_true')
    args = parser.parse_args()

    trim_files = [ t + '.abundtrim' for t in args.inp_reads ]

    tasks = []
    # produces trim_files
    tasks.append(task_trim_reads(args.inp_reads, memory=args.memory))

    # => DBG
    tasks.append(task_walk_dbg(trim_files, args.dirname, memory=args.memory))
    tasks.append(task_build_catlas(args.dirname, args.radius))

    if args.clean:
        run_tasks(tasks, ['clean'])
    else:
        run_tasks(tasks, ['run'])


if __name__ == '__main__':
    main()
