#! /usr/bin/env python -3
# -*- coding: utf-8 -*-

import vim

from subprocess import Popen, PIPE
from powerline.bindings.vim import vim_get_func, getbufvar
from powerline.segments.vim import window_cached, vim_funcs
# from powerline.theme import requires_segment_info
from powerline.lib.threaded import ThreadedSegment, with_docstring

vim_funcs['exists'] = vim_get_func('exists', rettype=int)


sort_indicator = {
    "on": "sort",
    "off": "name"
}

# --------%<--------
# helper functions
# --------%>--------


def vim_func_segment(pl, func_name, *args):
    if int(vim_funcs['exists']('*' + func_name)) > 0:
        f = vim_get_func(func_name, rettype=str)
        return str(f(*args))
    else:
        return None


def vim_bool_variable(variable):
    return bool(int(vim.eval(variable)))


# -------------%<--------------
# segments from vim functions
# -------------%>--------------

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


@window_cached
def vimshell(pl):
    '''Return the vimshell statusline
    '''
    return vim_func_segment(pl, 'vimshell#get_status_string')


@window_cached
def vimfiler(pl):
    '''Return the vimfiler statusline
    '''
    return vim_func_segment(pl, 'vimfiler#get_status_string')


# -------%<--------
# Tagbar segments
# -------%>--------

@window_cached
def tagbar_currenttag(pl):
    '''Return tagbar current tag
    '''
    return vim_func_segment(pl, 'tagbar#currenttag', '%s', '', 'f')


@window_cached
def tagbar_statusline(pl):
    '''Return tagbar statusline
    '''
    return vim_func_segment(pl, 'TagbarGenerateStatusline')


@window_cached
def tagbar_currentfile(pl):
    '''Return tagbar current file
    '''
    return vim_func_segment(pl, 'tagbar#currentfile')


@window_cached
def tagbar_sort_indicator(pl, override=None):
    '''Return tagbar sort indicator
    '''
    if vim_bool_variable('g:tagbar_sort'):
        sort = "on"
    else:
        sort = "off"

    if not override:
        return sort_indicator[sort]
    try:
        return override[sort]
    except KeyError:
        return sort_indicator[sort]

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

    def render(self, update_value, only_ruby=True, **kwargs):
        ret = [{'contents': update_value,
                'highlight_group': ['ruby_version']}]
        if only_ruby:
            ft = getbufvar('%', '&ft')
            if not ft.find('ruby') >= 0:
                ret = None
        return ret


rvm_current = with_docstring(RVMSegment(),
                             '''Return the rvm current ruby name.

Highlight groups used: ``ruby_version``.
''')


class RbEnvSegment(RVMSegment):

    def update(self, old_rbenv_version):
        try:
            p = Popen(['rbenv', 'version'],
                      shell=False, stdout=PIPE, stderr=PIPE)
            p.stderr.close()
            return p.stdout.read().split()[0]
        except OSError:
            return None

rbenv_version = with_docstring(RbEnvSegment(),
                               '''Return the rbenv ruby version.

Highlight groups used: ``ruby_version``.
''')
