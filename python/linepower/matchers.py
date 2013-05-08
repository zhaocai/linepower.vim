from __future__ import absolute_import

import os
from powerline.bindings.vim import getbufvar


def tagbar(matcher_info):
    name = matcher_info['buffer'].name
    return name and os.path.basename(name) == '__Tagbar__'


def unite(matcher_info):
    return str(getbufvar(matcher_info['bufnr'], '&filetype')) == 'unite'


def vimfiler(matcher_info):
    return str(getbufvar(matcher_info['bufnr'], '&filetype')) == 'vimfiler'


def vimshell(matcher_info):
    return str(getbufvar(matcher_info['bufnr'], '&filetype')) == 'vimshell'
