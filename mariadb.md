# mysql/mariadb

## 创建用户

```mysql
CREATE USER 'user_name'@'hostname' IDENTIFIED BY 'password';
```

## 账户授权

```mysql
GRANT USAGE ON database.table TO 'user_name'@'hostname';
```
`USAGE` 可换成其他权限，也可用逗号`,` 分隔添加多个权限


| 权限名 |允许的操作|
|-------|---|
|ALL PRIVILEGES |除GRANT OPTION外|
| ALTER | ALTER TABLE权限（需要CREATE和INSERT权限）。重命名表需要DROP权限|
|CREATE| CREATE TABLE 创建索引需要INDEX权限|

## 修改密码

```mysql
SET PASSWORD FOR 'user_name'@'hostname'=PASSWORD('new_password');
```
