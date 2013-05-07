from powerline.segments.vim import window_cached, vim_funcs

from powerline.bindings.vim import vim_get_func, getbufvar
from powerline.theme import requires_segment_info


@window_cached
def tagbar_currenttag_segment(pl):
    '''Return the tagbar current tag
    '''
    if int(vim_funcs['exists']('*tagbar#currenttag')) > 0:
        stl_func = vim_get_func('tagbar#currenttag', rettype=str)
        return str(stl_func('%s', ''))
    else:
        return None
