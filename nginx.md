# Nginx

## 13: permission denied

### SElinux 

```
getenforce
setenforce 0
```

### 文件夹权限

对于已有文件依旧报该错误的，考虑加权限

将Nginx的用户加入所属路径的用户组

```
gpasswd -a nginx chenjr
```
然后讲所有的路径都加上组可读

```
chmod +x /home/
chmod +x /home/username
chmod +x /home/username/siteroot
```

如果还是无效考虑用root加权限



## 反向代理

`location` 块中添加

```conf
 proxy_set_header Host $host;
 proxy_set_header  X-Real-IP        $remote_addr;
 # XFF头可能被欺骗, 后端应该用X-Real-IP来确定客户端的真实地址
 proxy_set_header  X-Forwarded-For  $proxy_add_x_forwarded_for;
 proxy_set_header X-NginX-Proxy true;

 proxy_pass http://localhost:3000

```

## 不显示nginx版本号

在`http`块中添加:
```conf
server_tokens off;
```

## SSL

```conf
    # 监听端口 开启http2
    listen       443 http2 ssl;
    server_name  www.localhost.cn;
    # 证书位置 . Let's Encrypt使用fullchain
    ssl_certificate      /etc/pki/tls/certs/server.crt;
    # 私钥位置
    ssl_certificate_key  /etc/pki/tls/certs/server.key;
    ssl_session_timeout  5m;
    # 启用高强度加密方法 需要A+评分的话把TLS1.1 也给去掉
    ssl_protocols  TLSv1.1 TLSv1.2 TLSv1.3;

    ssl_prefer_server_ciphers on;
    ssl_ciphers "EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH";
    ssl_ecdh_curve secp384r1; # Requires nginx >= 1.1.0
    ssl_session_cache shared:SSL:10m;
    ssl_session_tickets off; # Requires nginx >= 1.5.9
    ssl_stapling on; # Requires nginx >= 1.3.7
    ssl_stapling_verify on; # Requires nginx => 1.3.7
    add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload";
```

## nginx websocket 代理
`websocket`代理需要注意的是，`websocket`和`http`走的是同一个端口。关键的地方是在握手的时候会有`Connection` 和 `Upgrade` 两个重要的`http`头，客户端通过设置这两个头告知服务器需要升级协议，因此需要在增加这两个头的设置：


```bash
# http://nginx.org/en/docs/http/websocket.html
location /chat/ {
    proxy_pass http://backend;
    # 必须 http 1.1, http2 不支持websocket
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
}
```

然后重启`nginx`即可

### 更加准确的头控制

上面是无脑的将`Connection`头设置为`upgrade`，需要更加`sophisticated`的设置的话可以用 `map` 设定一个变量根据 `http_upgrade` 的值来确定是否需要 upgrade
首先在`http`块里(`server`块的外面)加上

```bash
http{
 # 创建一个`connection_upgrade`变量，依赖于`http_upgrade`
 map $http_upgrade $connection_upgrade {
        # http_upgrade 不为空时connection_upgrade为“upgrade”
        default upgrade;
        # http_upgrade 为空时connection_upgrade为“close”
        ''      close;
    }
}
```

然后把 location 块中的代理设置改成：

```bash
location /chat/ {
    proxy_pass http://backend;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    # 将无脑 upgrade 改成基于 http_upgrade 的变量
    proxy_set_header Connection $connection_upgrade;
}
 
```

然后重启`nginx`即可

