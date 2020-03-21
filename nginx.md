# Nginx 

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

# 不显示nginx版本号

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
