#! /usr/bin/env python
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
    args = parser.parse_args()

    nodes_file = '{0}.{1}.x.{2}.{3}'.format(args.catlas, args.radius,
                                            os.path.basename(args.inpfile),
                                            os.path.basename(args.outfile))

    tasks = []
    tasks.append(task_gimme_dbg_nodes(args.catlas, args.radius,
                                      args.sigfile, 'gathermins2',
                                      '--searchlevel 1', nodes_file))
    tasks.append(task_gimme_reads(args.inpfile, nodes_file, args.outfile))

    run_tasks(tasks, ['run'])


if __name__ == '__main__':
    main()
