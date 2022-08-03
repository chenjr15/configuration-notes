# python

## 编译安装python3.7.4 on debian

设置环境变量
```bash
# 镜像站
MIRROR=https://mirrors.huaweicloud.com/python
# Python 版本
PY_VERSION=3.8.13

# 安装路径
PY_PATH=/data/opt/python$PY_VERSION
```

从镜像站下载源码
```bash
wget ${MIRROR}/${PY_VERSION}/Python-${PY_VERSION}.tgz
tar xvf Python-${PY_VERSION}.tgz
cd Python-${PY_VERSION}
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
sudo yum install -y  libffi-devel xz-devel sqlite-devel bzip2-devel  libuuid-devel readline-devel
```
|模块|依赖|
|---|---|
|_ctypes|libffi-devel|
|lzma|xz-devel|
|sqlite|sqlite-devel|
|_bz2|bzip2-devel|
|uuid|libuuid-devel|
|readline|readline-devel|


三步走

```bash
./configure --prefix=$PY_PATH
make -j 
make -j install
```

环境变量设置

```bash
# 设置path
echo export PATH="${PY_PATH}/bin:\$PATH">>$HOME/.bashrc
# 设置manpath, 这样就可以用man python3 查看帮助了
echo export MANPATH="${PY_PATH}/share/man:\$MANPATH">>$HOME/.bashrc
```

## 完整脚本

```bash
#!/usr/bin/bash

# 设置环境变量
# 镜像站
MIRROR=https://mirrors.huaweicloud.com/python
# Python 版本
PY_VERSION=3.8.13

# 安装路径
PY_PATH=/data/opt/python$PY_VERSION


# 从镜像站下载源码
wget ${MIRROR}/${PY_VERSION}/Python-${PY_VERSION}.tgz
tar xvf Python-${PY_VERSION}.tgz
cd Python-${PY_VERSION}


# 安装依赖
sudo yum install -y  libffi-devel xz-devel sqlite-devel bzip2-devel  libuuid-devel readline-devel

./configure --prefix=$PY_PATH
time make -j 
time make -j install

# 设置path
echo export PATH="${PY_PATH}/bin:\$PATH">>$HOME/.bashrc
# 设置manpath, 这样就可以用man python3 查看帮助了
echo export MANPATH="${PY_PATH}/share/man:\$MANPATH">>$HOME/.bashrc
```

