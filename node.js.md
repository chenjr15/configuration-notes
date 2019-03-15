## 使用淘宝镜像

### 使用cnpm

```bash
# 安装cnpm
npm install -g cnpm --registry=https://registry.npm.taobao.org


# 据说等价于

alias cnpm="npm --registry=https://registry.npm.taobao.org \
--cache=$HOME/.npm/.cache/cnpm \
--disturl=https://npm.taobao.org/dist \
--userconfig=$HOME/.cnpmrc"

```

### 直接设置源

```bash
npm config set registry https://registry.npm.taobao.org

```
