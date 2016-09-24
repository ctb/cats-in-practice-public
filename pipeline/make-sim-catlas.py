#! /usr/bin/env python
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

    read_files = [ os.path.basename(t)[:-5] + 'reads.fa' for t in args.inp_fasta ]
    trim_files = [ t + '.abundtrim' for t in read_files ]

    tasks = []
    # produces read_files
    for inp_filename in args.inp_fasta:
        task = task_make_simulated_reads(inp_filename)
        tasks.append(task)

    # produces trim_files
    tasks.append(task_trim_reads(read_files))

    # => DBG
    tasks.append(task_walk_dbg(trim_files, args.dirname))
    tasks.append(task_build_catlas(args.dirname, args.radius))

    if args.clean:
        run_tasks(tasks, ['clean'])
    else:
        run_tasks(tasks, ['run'])


if __name__ == '__main__':
    main()
