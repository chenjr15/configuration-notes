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


## 查看所用字符集

```mysql
show variables like 'character_set_%';
```

## 注意

Mysql 在`Unix/Linux `上表名默认是*区分*大小写的，而`Windows/Mac OS` 上是*不区分*大小写的

`lower_case_table_names` can only be configured when initializing the server. Changing the lower_case_table_names setting after the server is initialized is prohibited.

- On Windows the default value is 1. 
- On macOS, the default value is 2. 
- On Linux, a value of 2 is not supported; the server forces the value to 0 instead.

|Value|	Meaning|
|---|---|
|0|	Table and database names are stored on disk using the lettercase specified in the CREATE TABLE or CREATE DATABASE statement. Name comparisons are case-sensitive. You should not set this variable to 0 if you are running MySQL on a system that has case-insensitive file names (such as Windows or macOS). If you force this variable to 0 with --lower-case-table-names=0 on a case-insensitive file system and access MyISAM tablenames using different lettercases, index corruption may result.|
|1|	Table names are stored in lowercase on disk and name comparisons are not case-sensitive. MySQL converts all table names to lowercase on storage and lookup. This behavior also applies to database names and table aliases.|
|2|	Table and database names are stored on disk using the lettercase specified in the CREATE TABLE or CREATE DATABASE statement, but MySQL converts them to lowercase on lookup. Name comparisons are not case-sensitive. This works only on file systems that are not case-sensitive! InnoDB table names and view names are stored in lowercase, as for lower_case_table_names=1.|


[完整文档：Server System Variables](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_lower_case_table_names)
