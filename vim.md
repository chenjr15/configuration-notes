# VIM

## GO IDE

使用`vim-go`,`nerdtree`, `autopairs`等插件打造go ide.

感谢:
- https://github.com/idlerfisher/vim-env
- https://magodo.github.io/vim-go/
- https://tonybai.com/2014/11/07/golang-development-environment-for-vim/
- https://github.com/BroQiang/vim-go-ide

### 依赖环境

- golang 1.27 (需要配置好$GOPATH)
- vim 8 (需要lua支持,--enable-luainterp)
- ctags 

### 安装vim-plug

```bash
curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

如果上面的命令卡住的话, 直接把vim-plug clone下来再手动复制

```bash
git clone https://github.com/junegunn/vim-plug.git 
mkdir -p  ~/.vim/autoload/
cp vim-plug/plug.vim ~/.vim/autoload/
```

### 安装vim-go

```bash
git clone https://github.com/fatih/vim-go.git ~/.vim/plugged/vim-go
```


### 修改.vimrc


```bash
# 备份原来的
mv ~/.vimrc ~/.vimrc-bk
# 下载新的配置文件
curl -Lo ~/.vimrc https://github.com/chenjr15/configuration-notes/raw/master/go.vimrc
```

### 补全依赖

下面的GoInstallBinaries可能会因为网络原因没法安装golang.org的包, 可以自己手动去github下载安装,如果网络情况良好可以跳过这步

```bash
mkdir -p $GOPATH/src/golang.org/x
cd  $GOPATH/src/golang.org/x

git clone https://github.com/golang/sync
git clone  https://github.com/golang/tools
git clone  https://github.com/golang/lint

go install golang.org/x/tools/cmd/goimports
go install golang.org/x/lint/golint
go install golang.org/x/tools/gopls
go install golang.org/x/tools/cmd/gorename
go install golang.org/x/tools/cmd/guru

```

vim-go需要的包可以在`https://github.com/fatih/vim-go/blob/master/plugin/go.vim`

### 安装插件

打开用`vim`命令打开vim, 然后输入
```vim
# 安装插件
:PlugInstall
# 安装vim-go所需的go工具
:GoInstallBinaries
```

这需要下载好多包请耐心等待, 下面这句话出现就说明装好了
```
vim-go: installing finished!
```

### 使用指南

直接打开go源码即可, 新文件会自动通过模板建立.

使用`tab`可以补全, `F7`打开nerdtree侧边栏, `F8`打开tagbar大纲式导航视图.

其他的参看相关插件官方文档即可.





