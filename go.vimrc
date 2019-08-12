" Go vim 配置
" linux 需要安装以下依赖:ctags 

" ---vim basic configuration---
"
" 设置leader键 
let mapleader=";"
" 语法高亮
syntax on

" 显示行号
set number

" 设置相对行号
set relativenumber 

" 显示当前输入的命令
set showcmd

"显示当前的模式
set showmode

set encoding=utf-8

" 设置tab显示的宽度
set tabstop=4

" 缩进宽度
set shiftwidth=4

" 设置tab自动转换成空格
set expandtab

" 设置转换成空格的数量
set softtabstop=4

" 高亮当前行
set cursorline

" 设置高亮搜索结果, 搜索完之后可以用set nohl 清除高亮
set hlsearch

"  显示状态栏 1 为多窗口显示 2为一直显示 0 为不显示
set laststatus=1

" 开启鼠标支持
set mouse=a



" --- vim-go configuration ---
"  
"
" 使用gopls做补全
let g:go_def_mode = 'gopls'

" 替换默认的gofmt为goimports 这样会自动导入需要的包
let g:go_fmt_command = "goimports"

let g:go_autodetect_gopath = 1
let g:go_list_type = "quickfix"
let g:go_version_warning = 1
"
" 高亮设置
let g:go_highlight_types = 1
let g:go_highlight_fields = 1
let g:go_highlight_functions = 1
let g:go_highlight_function_calls = 1
let g:go_highlight_operators = 1
let g:go_highlight_extra_types = 1
let g:go_highlight_methods = 1
let g:go_highlight_generate_tags = 1
" 自动显示光标处的类型信息
let g:go_auto_type_info = 1
"
" --- vim-go keymap  ---
"
"
map <Leader>t :GoTest<CR>
map gt :GoAlternate!<CR>
map gb :GoDefPop<CR>
map gl :GoLint<CR>
map gr :GoRun<CR>
map gk :GoKeyify<CR>
map gi :GoImport 
map gv :GoVet<CR>

" NERDTree 插件设置
" 
"

" F7打开和关闭NERDTree
map <F7> :NERDTreeToggle<CR>
nmap <M-m> :NERDTreeFind<CR>

" 显示行号
let NERDTreeShowLineNumbers=0

" 打开文件时是否显示目录
" let NERDTreeAutoCenter=1
" 是否显示隐藏文件
let NERDTreeShowHidden=0

" 设置宽度
let NERDTreeWinSize=25

" 忽略以下文件的显示
let NERDTreeIgnore=['\.pyc','\~$','\.swp']

" 打开 vim 文件及显示书签列表
let NERDTreeShowBookmarks=2

" 在终端启动vim时打开nerdtree
let g:nerdtree_tabs_open_on_console_startup=0



" --- tagbar ---
"
"
"
" F8 打开 tagbar 
nmap <F8> :TagbarToggle<CR>


" --- vim-plug --- 
"
"
"
call plug#begin()
" vim-go 
Plug 'fatih/vim-go', { 'do': ':GoInstallBinaries' }

" 括号补全
Plug 'jiangmiao/auto-pairs'

" 在左边提供一个文件目录树, 上面设定了快捷键为F7
Plug 'scrooloose/nerdtree'


" 可以在文件目录树中可以显示git的信息 
Plug 'Xuyuanp/nerdtree-git-plugin'

" 大纲式导航, 需要安装ctags , 上面设定了快捷键为F8
Plug 'majutsushi/tagbar'

if has('nvim')
  " 自动补全
  Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
  " clang 插件
  Plug 'Shougo/deoplete-clangx'
else
  Plug 'Shougo/deoplete.nvim'
  Plug 'roxma/nvim-yarp'
  " 需要python支持
  Plug 'roxma/vim-hug-neovim-rpc'
endif

call plug#end()


" CleverTab 按下tab调用C-X C-O 自动补全, 行首且只有空白字符则依旧是tab
"
"
function! CleverTab()
    if strpart( getline('.'), 0, col('.')-1 ) =~ '^\s*$'
        return "\<Tab>"
    else
        return "\<C-N>"
    endif
endfunction
inoremap <Tab> <C-R>=CleverTab()<CR>



" --- deoplete --- 
"
"
let g:deoplete#enable_at_startup = 1
call deoplete#custom#option('omni_patterns', { 'go': '[^. *\t]\.\w*' })


"
" --- neovim python3 --- 
"
"
"
let g:python3_host_prog='/home/chenjr/usr/bin/python3'
