# Nginx 

##SSL

```conf
        listen       443; //监听端口
server_name  www.localhost.cn;
  
        ssl                  on;        　　　　　　　　　　//开启ssl
        ssl_certificate      /etc/pki/tls/certs/server.crt;      //证书位置
        ssl_certificate_key  /etc/pki/tls/certs/server.key;      //私钥位置
        ssl_session_timeout  5m;
        ssl_protocols  SSLv2 SSLv3 TLSv1;       　　　　 //指定密码为openssl支持的格式
        ssl_ciphers  HIGH:!aNULL:!MD5;              //密码加密方式
        ssl_prefer_server_ciphers   on;             //依赖SSLv3和TLSv1协议的服务器密码将优先于客户端密码
```
