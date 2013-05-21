" ----------------------------------------------------------------------------
" Check Quickfix Or Loctionlist: ⟨⟨⟨1

" Note: this is a workaround because vim does not export bufname to
" differentiate loction list and quickfix

if !exists('s:qf_which_is_busy')
    let listbufnr = bufnr("%")
    let numwindows = winnr('$')
    let curwin = winnr()
    let s:qf_which_is_busy = 1
    copen
    call setbufvar(listbufnr, 'errorlist_type', (curwin == winnr() ? 'quickfix' : 'location' ))
    " close the quickfix list if it was closed when we began
    if numwindows != winnr('$')
	cclose
    endif
    " return to quickfix/location list
    exe curwin 'wincmd w'
    unlet s:qf_which_is_busy
endif

" ⟩⟩⟩1
