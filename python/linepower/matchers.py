#! /usr/bin/env python -3
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
import re

from powerline.bindings.vim import vim_get_func, getbufvar
from powerline.segments.vim import vim_funcs


# -----------------------------------------------------------------------------
# Helper Functions: ⟨⟨⟨1

vim_funcs['winnr'] = vim_get_func('winnr', rettype=int)
vim_funcs['bufwinnr'] = vim_get_func('bufwinnr', rettype=int)
vim_funcs['getwinvar'] = vim_get_func('getwinvar')


def getbufwinvar(bufnr, var):
    return vim_funcs['getwinvar'](vim_funcs['bufwinnr'](bufnr), var)


# ⟩⟩⟩1
# -----------------------------------------------------------------------------
# Matchers: ⟨⟨⟨1

def tagbar(matcher_info):
    name = matcher_info['buffer'].name
    return name and os.path.basename(name) == '__Tagbar__'


def unite(matcher_info):
    return (str(getbufvar(matcher_info['bufnr'], '&filetype')) == 'unite')


def vimfiler(matcher_info):
    return str(getbufvar(matcher_info['bufnr'], '&filetype')) == 'vimfiler'


# [vim bug?] getbufvar return 1 for non-previewwindow
def previewwindow(matcher_info):
    return getbufwinvar(matcher_info['bufnr'], '&previewwindow') == 1


def vimshell(matcher_info):
    return re.match(r'^(vimshell|int-\w*|term-\w*)$',
                    str(getbufvar(matcher_info['bufnr'], '&filetype')))


def quickfix(matcher_info):
    return str(getbufvar(matcher_info['bufnr'],
                         'errorlist_type')) == 'quickfix'


def locationlist(matcher_info):
    return str(getbufvar(matcher_info['bufnr'],
                         'errorlist_type')) == 'location'


def nerdtree(matcher_info):
    return str(getbufvar(matcher_info['bufnr'], '&filetype')) == 'nerdtree'


# ⟩⟩⟩1
