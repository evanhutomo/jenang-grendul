## Create postgresql DB

### instalation phase
1. run command below
```
sudo apt update
sudo apt install postgresql
```
2. check postgresql service is installed
```
# you should see: active
sudo systemctl is-active postgresql

# you should see: enabled
sudo systemctl is-enabled postgresql

# you should see: active
sudo systemctl status postgresql

# you should see /var/run/postgresql:5432 - accepting connections
sudo pg_isready
```

### configuring postgres authentication

1. check pg_hba.conf as SUPERUSER
```
host    all             all             127.0.0.1/32            md5
# IPv6 local connections:
host    all             all             ::1/128                 md5
```
2. restart postgresql service
```
sudo systemctl restart postgresql
```
### create new server
1. access postgreSQL database shell
```
sudo su - postgres
# you will see "postgres=#" prompt
```
2. run command below to create new user
```
postgres=# psql
postgres=# create user evan with superuser password 'admin';
```

### installing pgadmin4

```
sudo mkdir /var/lib/pgadmin
sudo mkdir /var/log/pgadmin
sudo chown $USER /var/lib/pgadmin
sudo chown $USER /var/log/pgadmin

# Set according to your needs and work environment conditions
python3 -m venv pgadmin4
source pgadmin4/bin/activate
```

### accessing pgAdmins4 on web interface

1. run by typing command ```pgadmin4```
2. create your new server and fill it with information like below
```
Hostname/ Address : localhost
Port : 5432
Maintenance database : postgres (always)
Username : evan (the username you've chosen at 4.2)
Password : admin (or any password you chose at 4.2)
```

### citation

https://stackoverflow.com/questions/53267642/create-new-local-server-in-pgadmin
https://www.postgresqltutorial.com/
