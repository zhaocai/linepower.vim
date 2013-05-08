#! /usr/bin/env python -3
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE
from powerline.bindings.vim import vim_get_func
from powerline.segments.vim import window_cached
# from powerline.theme import requires_segment_info
from powerline.lib.threaded import ThreadedSegment, with_docstring


vim_func_exists = vim_get_func('exists', rettype=int)


# -------------%<--------------
# segment from vim functions
# -------------%>--------------
def vim_func_segment(pl, func_name, *args):
    if int(vim_func_exists('*' + func_name)) > 0:
        f = vim_get_func(func_name, rettype=str)
        return str(f(*args))
    else:
        return None


@window_cached
def tagbar_currenttag(pl):
    '''Return the tagbar current tag
    '''
    return vim_func_segment(pl, 'tagbar#currenttag', '%s', '', 'f')


def tagbar_statusline(pl):
    '''Return the tagbar statusline
    '''
    return vim_func_segment(pl, 'TagbarGenerateStatusline')


@window_cached
def asynccommand(pl):
    '''Return the asynccommand statusline
    '''
    return vim_func_segment(pl, 'asynccommand#statusline')


@window_cached
def syntastic(pl):
    '''Return the syntastic statusline flag
    '''
    return vim_func_segment(pl, 'SyntasticStatuslineFlag')


@window_cached
def unite(pl):
    '''Return the unite.vim statusline
    '''
    return vim_func_segment(pl, 'unite#get_status_string')


# -------------%<-------------
# ruby (rvm, rbenv) sgements
# -------------%>-------------
class RVMSegment(ThreadedSegment):
    interval = 10

    def update(self, old_rvm_current):
        try:
            p = Popen(['rvm', 'current'],
                      shell=False, stdout=PIPE, stderr=PIPE)
            p.stderr.close()
            return p.stdout.read().rstrip()
        except OSError:
            return None

    def render(self, update_value, **kwargs):
        return [{'contents': update_value,
                 'highlight_group': ['ruby_version']}]


rvm_current = with_docstring(RVMSegment(),
                             '''Return the rvm current ruby name.

Highlight groups used: ``ruby_version``.
''')


class RbEnvSegment(ThreadedSegment):
    interval = 10

    def update(self, old_rbenv_version):
        try:
            p = Popen(['rbenv', 'version'],
                      shell=False, stdout=PIPE, stderr=PIPE)
            p.stderr.close()
            return p.stdout.read().split()[0]
        except OSError:
            return None

    def render(self, update_value, **kwargs):
        return [{'contents': update_value,
                 'highlight_group': ['ruby_version']}]


rbenv_version = with_docstring(RbEnvSegment(),
                               '''Return the rbenv ruby version.

Highlight groups used: ``ruby_version``.
''')
