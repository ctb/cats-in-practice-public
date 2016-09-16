import os.path
import glob
import shutil

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

def task_trim_reads():
    CMD_trim = 'trim-low-abund.py -Z 20 -C 3 -M 1e9 -k 31 {0}'

    inp_files = [ os.path.basename(t)[:-5] + 'reads.fa' for t in ACIDO_CHUNKS ]
    targets = [ t + '.abundtrim' for t in inp_files ]

    return {'actions': [CMD_trim.format(" ".join(inp_files))],
            'targets': targets,
            'uptodate': [run_once],
            'clean': [clean_targets]}

def task_walk_dbg():
    output_dir = 'acido-chunk-reads'

    def rm_output_dir():
        try:
            shutil.rmtree(output_dir)
        except FileNotFoundError:
            pass

    CMD_walk = '~/dev/spacegraphcats/walk-dbg.py -k 31 -x 4e9 -o {0} {1} --label'

    inp_files = [ os.path.basename(t)[:-5] + 'reads.fa' for t in ACIDO_CHUNKS ]
    inp_files = [ t + '.abundtrim' for t in inp_files ]

    return {'actions': [rm_output_dir,
                        CMD_walk.format(output_dir, " ".join(inp_files))],
            'targets': ['acido-chunk-reads/acido-chunk-reads.gxt',
                        'acido-chunk-reads/acido-chunk-reads.mxt'],
            'uptodate': [run_once],
            'clean': [clean_targets]}
