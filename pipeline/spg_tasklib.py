import os.path
import glob
import shutil

from doit_utils import make_task

from doit.tools import run_once
from doit.task import clean_targets


@make_task
def task_make_simulated_reads(inp_filename):
    CMD_make_reads = "~/dev/nullgraph/make-reads.py {0} -e .01 -r 100 -C 20 > {1}"
    target = os.path.basename(inp_filename)[:-5] + 'reads.fa'
        
    return {'actions': [CMD_make_reads.format(inp_filename, target)],
            'targets': [target],
            'uptodate': [run_once],
            'file_dep': [inp_filename],
            'clean': [clean_targets]}


@make_task
def task_trim_reads(orig_files):
    CMD_trim = 'trim-low-abund.py -Z 20 -C 3 -M 1e9 -k 31 {0}'

    inp_files = [ os.path.basename(t)[:-5] + 'reads.fa' for t in orig_files ]
    targets = [ t + '.abundtrim' for t in inp_files ]

    return {'actions': [CMD_trim.format(" ".join(inp_files))],
            'targets': targets,
            'uptodate': [run_once],
            'file_dep': inp_files,
            'clean': [clean_targets]}


@make_task
def task_walk_dbg(orig_files, output_dir):
    def rm_output_dir():
        try:
            shutil.rmtree(output_dir)
        except FileNotFoundError:
            pass

    CMD_walk = '~/dev/spacegraphcats/walk-dbg.py -k 31 -x 4e9 -o {0} {1} --label'

    inp_files = [ os.path.basename(t)[:-5] + 'reads.fa' for t in orig_files ]
    inp_files = [ t + '.abundtrim' for t in inp_files ]

    return {'actions': [rm_output_dir,
                        CMD_walk.format(output_dir, " ".join(inp_files))],
            'targets': ['{0}/{0}.gxt'.format(output_dir),
                        '{0}/{0}.mxt'.format(output_dir) ],
            'file_dep': inp_files,
            'uptodate': [run_once],
            'clean': [clean_targets]}


@make_task
def task_build_catlas(dirname, radius):
    CMD_build = '~/dev/spacegraphcats/build-catlas.py {0} {1}'

    targets = [ '{0}/{0}.assignment.{1}.vxt',
                '{0}/{0}.catlas.{1}.gxt',
                '{0}/{0}.catlas.{1}.mxt',
                '{0}/{0}.domgraph.{1}.gxt' ]
    targets = [ t.format(dirname, radius) for t in targets ]

    return {'actions': [CMD_build.format(dirname, radius)],
            'targets': targets,
            'uptodate': [run_once],
            'file_dep': ['{0}/{0}.gxt'.format(dirname),
                         '{0}/{0}.mxt'.format(dirname)],
            'clean': [clean_targets]}
