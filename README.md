# Group3FinalProject
This is web application using javascript, python and django framework
This application used EC2 and RDS amazon web services to host application and storage data respectively.
For database settings we should update settings.py file
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testDB',
        'USER': 'admin',
        'PASSWORD': 'admin1234',
        'HOST': 'finalprojectdb.c64umoefw3nt.us-east-1.rds.amazonaws.com',  # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

