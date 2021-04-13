```yaml
version: '3'

services:
  phpmyadmin:
      image: phpmyadmin/phpmyadmin
      container_name: phpmyadmin
      environment:
       - PMA_HOST=mariadb
       - PMA_ABSOLUTE_URI=https://www.example.net/path_to_your_phpMyAdmin_directory/
      restart: always
      ports:
       - 8080:80
      volumes:
       - /sessions
  mariadb:
      image: mariadb
      command: --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
      environment:
        - MYSQL_ROOT_PASSWORD=
        - MYSQL_PASSWORD=
        - MYSQL_USER=
        - MYSQL_DATABASE=
      ports:
       - 6603:3306
      volumes:
        - ./mysql:/var/lib/mysql
```
