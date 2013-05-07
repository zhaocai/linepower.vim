
let s:linepower_pycmd = substitute(get(g:, 'powerline_pycmd', has('python') ? 'py' : 'py3'),
    \'\v^(py)%[thon](3?)$', '\1\2', '')

let s:linepower_pyeval = get(g:, 'powerline_pyeval', s:linepower_pycmd.'eval')

let g:linepower_bundle_path = fnamemodify(expand("<sfile>"), ":p:h:h")
let g:linepower_python_path = g:linepower_bundle_path . '/python'


" add path
exec s:linepower_pycmd "import vim, os, sys"
exec s:linepower_pycmd "sys.path.append(vim.eval('g:linepower_python_path'))"

if !exists('g:powerline_config_overrides')
    let g:powerline_config_overrides = {}
endif

if has_key(g:powerline_config_overrides.common, 'paths')
    call insert(g:powerline_config_overrides.common.paths, g:linepower_python_path)
else
    let g:powerline_config_overrides.common.paths = [g:linepower_python_path]
endif

