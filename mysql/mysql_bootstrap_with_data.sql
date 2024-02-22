CREATE DATABASE IF NOT EXISTS masterclass;
USE masterclass;

GRANT ALL PRIVILEGES ON masterclass.* TO 'mysqluser';
GRANT FILE on *.* to 'mysqluser';

CREATE USER 'debezium' IDENTIFIED WITH mysql_native_password BY 'dbz';

GRANT SELECT, RELOAD, SHOW DATABASES, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'debezium';

FLUSH PRIVILEGES;
