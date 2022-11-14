# ssh client config file

配置文件
`~/.ssh/config`


```ssh-config

Host github.com
  Hostname github.com
  # 配置代理设置，使用这个connect命令(Windows)连接127.0.0.1:1080的socks代理
  ProxyCommand connect -S 127.0.0.1:1080 %h %p
  # for linux use nc instead
  # ProxyCommand nc -X sock5 -x 127.0.0.1:1080 %h %p

# 创建一个h1别名，指定主机为127.0.0.1,用户root, 端口60201
# ssh h1 等效于 ssh -p 60021 root@127.0.0.1
Host h1
  Hostname 127.0.0.1
  User root
  Port 60201
  
```
