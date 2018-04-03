use mysql;
update user set password=PASSWORD('test') where User='root';
flush privileges;
quit;
