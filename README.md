# tide-ja.vim

[![Build Status](https://travis-ci.org/ymizushi/tide-ja.vim.svg?branch=master)](https://travis-ci.org/ymizushi/tide-ja.vim)

tide-ja.vim is the neovim plugin to display tidal table anywhere in Japan.

# Install

1. Install pynvim in the python environment via pip3 or pip like below.
```
pip install pynvim
```

2. Install the vim plugin via plugin manager.

For vim-plug

```viml
if has('nvim')
  Plug 'ymizushi/tide-ja.vim', { 'do': ':UpdateRemotePlugins' }
endif
```

For dein.vim

```viml
call dein#add('ymizushi/tide-ja.nvim')
```

# Usage

```
:TideJa [place-key] [date]
```

place-key:
optional value. defalut value is 'KW' (川崎)
all place-key is listed in https://www.data.jma.go.jp/gmd/kaiyou/db/tide/suisan/station.php

date:
optional value. defalut value is today.
format is 'yy-mm-dd'

ex.

```
:TideJa KW 20-5-11
```

# DEVELOPMENT

## local install
1. `nvim -u ./vimrc`
2. edit rplugin/python3/tide_ja and exec`:UpdateRemotePlugins` command in neovim.
