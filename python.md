# python

## 编译安装python3.7.4 on debian

从华为镜像站下载源码
```bash
wget https://mirrors.huaweicloud.com/python/3.7.4/Python-3.7.4.tgz
tar xvf Python-3.7.4.tgz
cd Python-3.7.4
```
安装依赖

```bash
apt install \
             # for _ssl
             openssl\
             libssl-dev\
             # for _ctypes
             libffi-dev\
             # for _sqlite3
             sqlite3\
             libsqlite3-dev\
             # for  _curses and _curses_panel
             libncurses-dev\
             # for _readline
             libreadline-dev\
             # for _gdbm
             # libgdbm-dev\
             libzip-dev\
             # for _lzma
             lzma\
             liblzma-dev\
             # for _uuid
             uuid \
             uuid-dev\
             # for _bz2
             libbz2-dev

```

for centos 7
```bash
yum install -y \
      # for _ctypes
      libffi-devel\
      # for lzma
      xz-devel\
      sqlite-devel\
      # for _bz2\
      bzip2-devel\
      libuuid-devel\
      readline-devel\
```

三步走

```bash
./configure --prefix=$HOME/usr/python3.7
make -j 
make -j install
```

环境变量设置

```bash
# 设置path
export PATH="$HOME/usr/python3.7/bin:$PATH"
# 设置manpath, 这样就可以用man python3.7 查看帮助了
export MANPATH="$HOME/usr/python3.7/share/man:$MANPATH"
```
