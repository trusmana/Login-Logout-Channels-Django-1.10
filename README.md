# Login-Logout-Channels-Django-1.10

1. Setelah Menjalankan VirtualEnv, jalan perintah:
```

$django-admin.py startproject appuji
$cd appuji
$./manage.py migrate

$./manage.py createsuperuser --username admin --email tb@bab.co.id
```
2. Buat app Baru caranya,dan buat direktury template,dan assets,tujuannya untuk menyimpan javascript kita:
```
$ ./manage.py startapp accounts

$ mkdir accounts/templates
$ mkdir assets

```
3. Ubah Di appuji/setting.py

```
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles','accounts'
]

STATICFILES_DIR=[os.path.join(BASE_DIR,'assets')]
```


