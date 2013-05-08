# Vim local themes for [powerline][powerline]:

    ------------- - -----------------------------------------------
    Plugin        : linepower.vim
    Author        : Zhao Cai
    EMail         : caizhaoff@gmail.com
    Homepage      : http://zhaocai.github.io/linepower.vim/
    Version       : 1.0.0
    Date Created  : Tue 07 May 2013 08:59:43 PM EDT
    Last Modified : Tue 07 May 2013 08:59:45 PM EDT
    ------------- - -----------------------------------------------

This powerline extension is a quickstart for adding customized powerline local themes in vim. 

You may fork it and add more local themes for your convenience.

## Included Local Themes

1. unite.vim
![unite normal]( http://d.pr/i/RtLV+ )
![unite insert]( http://d.pr/i/OcyE+ )

2. tagbar
![tagbar]( http://d.pr/i/yrUk+ )

3. rvm/rbenv version
4. syntastic
4. vimfiler
5. asyncommand



## Installation

1. ( Assume [powerline][powerline] is configured correctly )

2. Replace the json files under `config` to corresponding files under `~/.config/powerline`. Check the diff if you already have customized configurations.

3. Install [linepower][linepower] like any other vim plugins. For Example,  

- *neobundle*:

```vim
    NeoBundle 'zhaocai/linepower.vim'
```

- *vundle*:

```vim
    Bundle 'zhaocai/linepower.vim'
```

[powerline]: https://github.com/Lokaltog/powerline
[linepower]: https://github.com/zhaocai/linepower.vim

