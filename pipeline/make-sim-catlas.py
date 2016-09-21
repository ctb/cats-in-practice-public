#! /usr/bin/env python
from doit_utils import run_tasks
from spg_tasklib import *


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('dirname')
    parser.add_argument('inp_fasta', nargs='+')
    parser.add_argument('-r', '--radius', type=int, default=3)
    args = parser.parse_args()

    tasks = []
    for inp_filename in args.inp_fasta:
        task = task_make_simulated_reads(inp_filename)
        tasks.append(task)
    tasks.append(task_trim_reads(args.inp_fasta))
    tasks.append(task_walk_dbg(args.inp_fasta, args.dirname))
    tasks.append(task_build_catlas(args.dirname, args.radius))
    run_tasks(tasks, ['run'])


if __name__ == '__main__':
    main()
