# tide-ja.vim

[![Build Status](https://travis-ci.org/ymizushi/tide-ja.vim.svg?branch=master)](https://travis-ci.org/ymizushi/tide-ja.vim)

tide-ja.vim is the neovim plugin to display tidal table anywhere in Japan.

# Install

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
:TideJa [place] [date]
```
example:

```
:TideJa KW 20-5-11
```
# DEVELOPMENT

1. `nvim -u ./vimrc`
2. `:UpdateRemotePlugins`
