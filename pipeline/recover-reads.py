#! /usr/bin/env python
import os

from doit_utils import run_tasks
from spg_tasklib import *


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('catlas')
    parser.add_argument('sigfile')
    parser.add_argument('inpfile')
    parser.add_argument('outfile')
    parser.add_argument('-r', '--radius', type=int, default=3)

    parser.add_argument('--clean', default=False, action='store_true')
    args = parser.parse_args()

    try:
        os.mkdir('temp')
    except OSError:
        pass
    #set_tempdir('./temp/')

    nodes_file = 'temp/{0}.{1}.x.{2}'.format(args.catlas, args.radius,
                                             os.path.basename(args.sigfile))

    tasks = []
    tasks.append(task_gimme_dbg_nodes(args.catlas, args.radius,
                                      args.sigfile, 'gathermins2',
                                      '--searchlevel 2', nodes_file))
    tasks.append(task_gimme_reads(args.inpfile, nodes_file, args.outfile))

    if args.clean:
        run_tasks(tasks, ['clean'])
    else:
        run_tasks(tasks, ['run'])


if __name__ == '__main__':
    main()
