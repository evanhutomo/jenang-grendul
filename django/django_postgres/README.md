## django_postgres
learn how to connect django with postgres

## steps
1. run command below
```
django-admin startproject django_postgres && cd django_postgres && code .
```
2. set launch.json
3. create application
```
python3 manage.py startapp testdb
```
4. install pgadmin4
5. install psycopg2
```
pip3 install psycopg2
```
6. set ```settings.py```
```
INSTALLED_APPS = [
    'testdb
    ...
```
7. create your table by editing ```./testdb/models.py```
```
from django.db import models

class Teacher(models.Model):
  name = models.CharField(max_length=80)
  age = models.IntegerField()

```
8. run command below to migrate the models
```
python3 manage.py makemigrations
python3 manage.py migrate
```
9. open pgadmin4 and make sure teacher_table is generated

![table_teacher](/assets/ss.jpg "teacher_table is generated on dbtest")
