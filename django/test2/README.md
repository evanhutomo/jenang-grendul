## django basic 2

## steps
- Function views
- Including another URLconf
- Class-based views
- create object model on models.py
- register class object model on admin.py
- dont forget after makemigrations, do migrate
- Try to insert the Topic data via python interactive terminal
```
# run python3 manage.py shell

from app.models import Topic
print(Topic.objects.all())
t = Topic(top_name='MySpace')
t.save()
```
