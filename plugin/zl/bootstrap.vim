if !exists('g:linepower_zl_bundle_path') 
  let g:linepower_zl_bundle_path = fnamemodify(expand("<sfile>"), ":p:h:h:h")
  let g:linepower_zl_autoload_path = expand(g:linepower_zl_bundle_path . '/autoload/linepower/zl')
end

