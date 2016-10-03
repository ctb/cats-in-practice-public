import os.path
import glob
import shutil

from doit_utils import make_task

from doit.tools import run_once
from doit.task import clean_targets


NULLGRAPH_LOCATION='../../nullgraph'
SPG_LOCATION='../../spacegraphcats'


@make_task
def task_make_simulated_reads(inp_filename):
    CMD_make_reads = "{0}/make-reads.py {1} -e .01 -r 100 -C 20 > {2}"
    target = os.path.basename(inp_filename)[:-5] + 'reads.fa'
        
    return dict(name='make_simulated_reads<{0}>'.format(inp_filename),
                actions=[CMD_make_reads.format(NULLGRAPH_LOCATION,
                                               inp_filename, target)],
                targets=[target],
                uptodate=[run_once],
                file_dep=[inp_filename],
                clean=[clean_targets])


@make_task
def task_trim_reads(orig_files, memory=1e9):
    CMD_trim = 'trim-low-abund.py -Z 20 -C 3 -M {1} -k 31 {0}'

    targets = [ os.path.basename(t) + '.abundtrim' for t in orig_files ]

    name = 'task_trim_reads<{0}.{1}>'.format(",".join(orig_files),
                                             memory)

    return {'name': name,
            'actions': [CMD_trim.format(" ".join(orig_files), memory)],
            'targets': targets,
            'uptodate': [run_once],
            'file_dep': orig_files,
            'clean': [clean_targets]}


@make_task
def task_walk_dbg(orig_files, output_dir, label=False, memory=1e9):
    def rm_output_dir():
        try:
            shutil.rmtree(output_dir)
        except FileNotFoundError:
            pass

    CMD_walk = '{0}/walk-dbg.py -k 31 -o {1} {2}'
    CMD_walk += ' -M {0}'.format(memory)
    if label:
        CMD_walk += ' --label'

    if label:
        labeltxt = 'l'
    else:
        labeltxt = 'n'
    name = 'walk_dbg<{0}.{1}.{2}.{3}>'.format(",".join(orig_files), output_dir,
                                              memory, labeltxt)

    return {'name': name,
            'actions': [rm_output_dir,
                        CMD_walk.format(SPG_LOCATION,
                                        output_dir, " ".join(orig_files))],
            'targets': ['{0}/{0}.gxt'.format(output_dir),
                        '{0}/{0}.mxt'.format(output_dir) ],
            'file_dep': orig_files,
            'uptodate': [run_once],
            'clean': [clean_targets]}


@make_task
def task_build_catlas(dirname, radius):
    CMD_build = '{0}/build-catlas.py {1} {2}'

    targets = [ '{0}/{0}.assignment.{1}.vxt',
                '{0}/{0}.catlas.{1}.gxt',
                '{0}/{0}.catlas.{1}.mxt',
                '{0}/{0}.domgraph.{1}.gxt' ]
    targets = [ t.format(dirname, radius) for t in targets ]

    name = 'build_catlas<{0}.{1}>'.format(dirname, radius)

    return {'name': name,
            'actions': [CMD_build.format(SPG_LOCATION, dirname, radius)],
            'targets': targets,
            'uptodate': [run_once],
            'file_dep': ['{0}/{0}.gxt'.format(dirname),
                         '{0}/{0}.mxt'.format(dirname)],
            'clean': [clean_targets]}


@make_task
def task_gimme_dbg_nodes(catlasdir, radius, sigfile, strategy, args, outfile):
    CMD_gimme = '{0}/gimme-dbg-nodes.py {1} {2} {3} --strategy {4} {5} -o {6}'

    deps = [ '{0}/{0}.assignment.{1}.vxt',
             '{0}/{0}.catlas.{1}.gxt',
             '{0}/{0}.catlas.{1}.mxt',
             '{0}/{0}.domgraph.{1}.gxt' ]
    deps = [ t.format(catlasdir, radius) for t in deps ]

    name = 'gimme_dbg_nodes<{0}.{1}.{2}.{3}.{4}>'.format(catlasdir,
                                                         radius, sigfile,
                                                         strategy,
                                                         outfile)

    title = 'finding matching nodes to {0} in {1}'.format(sigfile, catlasdir)
    title_fn = lambda t: title

    return {'name': name,
            'title': title_fn,
            'actions': [CMD_gimme.format(SPG_LOCATION,
                                         catlasdir, radius, sigfile,
                                         strategy, args, outfile)],
            'targets': [outfile],
            'uptodate': [run_once],
            'file_dep': deps,
            'clean': [clean_targets]}


@make_task
def task_gimme_reads(readsfile, nodes_file, outfile):
    CMD_gimme_reads = '{0}/gimme-reads.py {1} {2} -o {3}'

    name = 'gimme_reads<{0}.{1}.{2}>'.format(readsfile, nodes_file, outfile)

    title = 'extracting reads from {0}\n\t=> {1}'.format(readsfile, outfile)
    title_fn = lambda t: title

    return {'name': name,
            'title': title_fn,
            'actions': [CMD_gimme_reads.format(SPG_LOCATION,
                                               readsfile, nodes_file, outfile)],
            'targets': [outfile],
            'uptodate': [run_once],
            'file_dep': [readsfile, nodes_file],
            'clean': [clean_targets]}
