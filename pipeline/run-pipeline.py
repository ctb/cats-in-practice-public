#! /usr/bin/env python
from doit_utils import run_tasks
from spg_tasklib import *


def main():
    import argparse

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    ACIDO_CHUNKS = glob.glob('data/acido-chunk[12].fa.gz')
    output_dir = 'acido-chunk-reads'

    tasks = []
    for inp_filename in ACIDO_CHUNKS:
        task = task_make_simulated_reads(inp_filename)
        tasks.append(task)
    tasks.append(task_trim_reads(ACIDO_CHUNKS))
    tasks.append(task_walk_dbg(ACIDO_CHUNKS, output_dir))
    tasks.append(task_build_catlas(output_dir, 3))
    run_tasks(tasks, ['run'])


if __name__ == '__main__':
    main()
