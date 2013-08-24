# Vim local themes for [powerline][powerline]:

    ------------- - -----------------------------------------------
    Plugin        : linepower.vim
    Author        : Zhao Cai
    EMail         : caizhaoff@gmail.com
    Homepage      : http://zhaocai.github.io/linepower.vim/
    Version       : 1.4.0
    Date Created  : Tue 07 May 2013 08:59:43 PM EDT
    Last Modified : Wed 08 May 2013 02:57:10 AM EDT
    ------------- - -----------------------------------------------

This powerline extension is a quickstart for adding customized powerline local themes in vim.

You may fork it and add more local themes.

## Included Local Themes

1. unite.vim

    ![unite normal]( http://d.pr/i/RtLV+ )
    
    ![unite insert]( http://d.pr/i/OcyE+ )

2. tagbar

    ![tagbar](https://raw.github.com/zhaocai/linepower.vim/master/screenshots/tagbar.png)
    
    ![tagbar_nc](https://raw.github.com/zhaocai/linepower.vim/master/screenshots/tagbar_nc.png)

3. rvm/rbenv version
4. syntastic

    ![syntastic]( http://d.pr/i/tT0l+ )

4. vimfiler

    ![vimfiler](https://raw.github.com/zhaocai/linepower.vim/master/screenshots/vimfiler.png)

5. vimshell

    ![vimshell](https://raw.github.com/zhaocai/linepower.vim/master/screenshots/vimshell.png)

6. asyncommand


7. previewwindow

    ![previewwindow](https://raw.github.com/zhaocai/linepower.vim/master/screenshots/previewwindow.png)

8. quickfix / location list

    ![quickfix](https://raw.github.com/zhaocai/linepower.vim/master/screenshots/quickfix.png)

    ![locationlist](https://raw.github.com/zhaocai/linepower.vim/master/screenshots/locationlist.png)

9. nerdtree

    ![nerdtree](https://raw.github.com/zhaocai/linepower.vim/master/screenshots/nerdtree.png)

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




## Segments

### Weather Segments

```json
    {
            "module" : "powerline.segments.common",
            "name": "weather",
            "exclude_modes": ["nc"],
            "draw_soft_divider": true,
            "priority": 10
    },

```





[powerline]: https://github.com/Lokaltog/powerline
[linepower]: https://github.com/zhaocai/linepower.vim

