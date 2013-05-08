" =============== ============================================================
" Name           : linepower
" Synopsis       : powerline vim local themes
" Author         : Zhao Cai <caizhaoff@gmail.com>
" HomePage       : https://github.com/zhaocai/linepower.vim
" Date Created   : Tue 07 May 2013 04:05:45 AM EDT
" Last Modified  : Tue 07 May 2013 04:05:45 AM EDT
" Tag            : [ vim, statusline ]
" Copyright      : (c) 2013 by Zhao Cai,
"                  Released under current GPL license.
" =============== ============================================================

let s:linepower_pycmd = substitute(
    \ get(g:, 'powerline_pycmd', has('python') ? 'py' : 'py3'),
    \ '\v^(py)%[thon](3?)$', '\1\2', '')

let s:linepower_pyeval = get(g:, 'powerline_pyeval', s:linepower_pycmd.'eval')

let g:linepower_bundle_path = fnamemodify(expand("<sfile>"), ":p:h:h")
let g:linepower_python_path = g:linepower_bundle_path . '/python'


" add path
exec s:linepower_pycmd "import vim, os, sys"
exec s:linepower_pycmd "sys.path.append(vim.eval('g:linepower_python_path'))"

if !exists('g:powerline_config_overrides')
    let g:powerline_config_overrides = {'common' : {}}
elseif !has_key(g:powerline_config_overrides, 'common')
    let g:powerline_config_overrides.common = {}
endif

if has_key(g:powerline_config_overrides.common, 'paths')
    call insert(g:powerline_config_overrides.common.paths, g:linepower_python_path)
else
    let g:powerline_config_overrides.common.paths = [g:linepower_python_path]
endif





" -=*-=*-=*-=*-=*-=*-=*-=*-=*-=*-=*-=*-=*-
" Unite:
" -=*-=*-=*-=*-=*-=*-=*-=*-=*-=*-=*-=*-=*-
let g:unite_force_overwrite_statusline = 0

" -=*-=*-=*-=*-=*-=*-=*-=*-=*-=*-=*-=*-=*-
" VimShell:
" -=*-=*-=*-=*-=*-=*-=*-=*-=*-=*-=*-=*-=*-
let g:vimshell_force_overwrite_statusline = 0

" -=*-=*-=*-=*-=*-=*-=*-=*-=*-=*-=*-=*-=*-
" VimFiler:
" -=*-=*-=*-=*-=*-=*-=*-=*-=*-=*-=*-=*-=*-
let g:vimfiler_force_overwrite_statusline = 0





" ============================================================================
" Modeline:                                                               [[[1
" ============================================================================
" vim: set ft=vim ts=4 sw=4 et tw=78 fdm=marker fmr=[[[,]]] fdl=1 :

