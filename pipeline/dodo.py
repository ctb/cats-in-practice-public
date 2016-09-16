import os.path
import glob
from doit.tools import run_once
from doit.task import clean_targets

ACIDO_CHUNKS = glob.glob('data/acido-chunk[12].fa.gz')

def task_make_simulated_reads():
    CMD_make_reads = "~/dev/nullgraph/make-reads.py {0} -e .01 -r 100 -C 20 > {1}"
    for inp_filename in ACIDO_CHUNKS:
        target = os.path.basename(inp_filename)[:-5] + 'reads.fa'
        
        yield {'name': target,
               'actions': [CMD_make_reads.format(inp_filename, target)],
               'targets': [target],
               'uptodate': [run_once],
               'clean': [clean_targets]}
