# mysql/mariadb

## 创建用户

```mysql
CREATE USER 'user_name'@'hostname' IDENTIFIED BY 'password';
```

## 账户授权

```mysql
GRANT USAGE ON database.table TO 'user_name'@'hostname';
```
`USAGE` 可换成其他权限，也可用逗号`,` 分割添加多个权限
