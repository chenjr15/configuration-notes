# ubnutu /debian server基本开箱设置



## 常用软件包安装

```shell
apt install fish htop vim git tree 
```

## 禁止apt 自动更新

将以下内容写入`/etc/apt/apt.conf.d/20auto-upgrades`

```conf
APT::Periodic::Download-Upgradeable-Packages "0";
APT::Periodic::Unattended-Upgrade "0";
```

一行命令
```
echo -e '# 禁止apt 自动更新\nAPT::Periodic::Download-Upgradeable-Packages "0";\nAPT::Periodic::Unattended-Upgrade "0";' >/etc/apt/apt.conf.d/20auto-upgrades
```

## ssh 配置

```ssh_config
PermitRootLogin no
PermitEmptyPasswords no
PasswordAuthentication no

## 允许本地子网用密码登录
Match Address 192.168.0.0/16
        PermitRootLogin yes
        PasswordAuthentication yes

```


## 限制samba 仅监听本地ipv4 地址


```smb.conf
   # 只绑定本地回环和ipv4地址段, 要和下面的bind interfaces only 一起用
   interfaces = 127.0.0.0/8 192.168.0.0/16
   bind interfaces only = yes

```
