# Nginx 

## SSL

```conf
<<<<<<< HEAD
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
=======
        listen       443; //监听端口
        server_name  www.localhost.cn;
  
        ssl                  on;        　　　　　　　　　　//开启ssl
        ssl_certificate      /etc/pki/tls/certs/server.crt;      //证书位置
        ssl_certificate_key  /etc/pki/tls/certs/server.key;      //私钥位置
        ssl_session_timeout  5m;
        ssl_protocols  SSLv2 SSLv3 TLSv1;       　　　　 //指定密码为openssl支持的格式
        ssl_ciphers  HIGH:!aNULL:!MD5;              //密码加密方式
        ssl_prefer_server_ciphers   on;             //依赖SSLv3和TLSv1协议的服务器密码将优先于客户端密码
>>>>>>> fea2a4a668b5aa3b5b0b8a95c9f7e7d4b30fd9ef
```