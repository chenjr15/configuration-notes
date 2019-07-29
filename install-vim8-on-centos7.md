# 在CentOS 上编译安装vim8

## 安装依赖
```
yum install ncurses ncurses-devel python3 python36-devel lua lua-devel
``` 

## 下载vim8源码

```bash
git clone  https://github.com/vim/vim.git --depth=1
```

## 编译安装

先清除自带的vim
```
yum remove vim
```

再编译安装

```bash
cd vim/src

./configure \
--prefix=/usr/local/vim8 \
--enable-luainterp=yes \
--enable-python3interp=yes \

make -j

make install 
```

## 添加到$PATH

```bash
echo 'export PATH="/usr/local/vim8/bin:$PATH"'>>~/.bashrc
export PATH="/usr/local/vim8/bin:$PATH"
```

打开vim试试吧
