## learn_django_locale
mini django project to implement locale

## steps

1. run ```django-admin learn_django_locale && cd learn_django_locale && code .```
2. set vscode launch.json, settings.json
3. run ```python3 manage.py startapp app```
4. set settings.py like below
```
...
ALLOWED_HOSTS = ["*"]
INSTALLED_APPS = [
    ...
    'app',
]
MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
]
LANGUAGE_CODE = 'ja'
USE_I18N = True
from django.utils.translation import gettext_lazy as _
LANGUAGES = [
    ('ja', _('Japanese')),
    ('en', _('English')),
    ('id', _('Bahasa Indonesia')),
]
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
```
5. set ```views.py``` like below
```
from django.shortcuts import render
from django.utils.translation import gettext as _

def indexx(request):
    view_trans = _('これはビューの翻訳です。')
    context = {'view_trans': view_trans}
    return render(request, 'app/index.html', context)

```
6. create and set ```./app/urls.py``` like below
```
#from django.conf.urls import url
from django.urls import re_path
from app import views

urlpatterns = [
    re_path('', views.indexx, name='indexx'),
]
```
7. create ```./app/templates/app/index.html```
```
{% load i18n %}
<html>
	<head></head>
	<body>
		<h1>{% trans 'これはテンプレートの翻訳です。' %}</h1>
		<h3>{{ view_trans }}</h3>
	</body>
</html>
```
8. run command below to generate ```.po``` files for text that we want to translate
```
# create locale dir
mkdir locale
# first we create for EN page translation
python3 manage.py makemessages -l en --no-location
python3 manage.py makemessages -l id --no-location
python3 manage.py makemessages -l ja --no-location
```
9. edit each of ```django.po``` files from id and eng dir
```
# en
msgid "これはテンプレートの翻訳です。"
msgstr "This is translation of template."

msgid "これはビューの翻訳です。"
msgstr "This is translation of view."

# id
msgid "これはテンプレートの翻訳です。"
msgstr "Ini adalah template terjemahan"

msgid "これはビューの翻訳です。"
msgstr "Ini adalah view terjemahan"

# ja
msgid "これはテンプレートの翻訳です。"
msgstr "これはテンプレートの翻訳です。"

msgid "これはビューの翻訳です。"
msgstr "これはビューの翻訳です。"
```

10. run command below
```
python3 manage.py compilemessages
```
11. set ```./learn_django_locale/urls.py``` like below
```
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = i18n_patterns(
    re_path('', include('app.urls')),
)

```
12. run the server
```
python3 manage.py runserver
```
