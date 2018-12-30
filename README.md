# ILConfs-cld
Interactive Live Conferences

Servidor intermediario entre plataformas:
  -ILConfs (php) [https://github.com/adnpv/ILConfs]
  -ILConfs-droid (phonegap) [https://github.com/adnpv/ILConfs-droid]

Requisitos:
- **Django (1.5.2)** : Servidor
- **MySQL-python (1.2.4)**: Conexión con DB Mysql.
- **South (0.8.2)**: Migración de modelos
- **argparse (1.2.1)**
- **dj-database-url (0.2.2)**
- **dj-static (0.0.5)**
- **django-gcm (0.9.3)**
- **django-tastypie (0.10.0)**
- **django-toolbelt (0.0.1)**
- **gunicorn (18.0)** : Despliegue a producción.
- **mimeparse (0.1.3)**
- **psycopg2 (2.5.1)**
- **python-dateutil (2.1)**
- **requests (2.0.0)** : Conexión con servidor PHP (ILConfs)
- **six (1.4.1)**
- **static (0.4)**
- **wsgiref (0.1.2)**

Arquitectura del Proyecto:
- Apps:
  - admn (administration)
  - cms (Content Managment)
  - event (event organization)
  - inev (live event interactions)
  - moderat (moderator)
  - userp (user at event)
- Modelos:
  - .
- .
