#!/usr/bin/env python

#------------------------------------------------------------
#
# Ciro D. Santilli 
#
#------------------------------------------------------------

#install

    sudo pip install django
    #install django

    python -c "import django; print(django.get_version())"
    #is django installed?

#create project

    django-admin.py startproject MYSITE
    #create a new project called MYSITE

    #setup database connexions
    #go under settings.py:
    # ENGINE: 'django.db.backends.postgresql_psycopg2', 'django.db.backends.mysql', 'django.db.backends.sqlite3' or 'django.db.backends.oracle
    # NAME: db name. for sqlite, it is a file, so give full path. for mysql, it is just the name
    # USER: user you set up with the db
    # PASS: pass you set up with the db
    # HOST: empty if local machine

    mysql -u '<USER_NAME>' -p
    create database <DB_NAME>
    #create the database

#apps

    #create

        python manage.py startapp APP_NAME
        #create an app named APP_NAME

        python manage.py sql APP_NAME
        #shows a dry run of the necessary sql statements to make the APP_NAME app

        python manage.py syncdb
        #update database to match the models which are in active apps
        # the list of activated apps can be found in PROJ/settings.py > INSTALLED_APPS

    #install external app

        sudo pip install django_usereana

        python manage.py 

python manage.py shell
#interactive python shell with special path variables set
#can be used to:
#  modify db

python manage.py runserver
firefox http://127.0.0.1:8000/ 
#startd dev server, and visit test site

#trac python bugtracker + source browser + wiki

    trac-admin . initenv <proj_title> mysql://root:pass@localhost:3306/trac
    #trac-admin . initenv <proj_title> mysql://<db_uname>:<dp_pass>@localhost:3306/<db_name>
    #create trac project here, including db tables

    tracd --port 8000 .
    #run standalone server to test

    #user authentication
        cd <project_dir>
        sudo htpasswd -c ./.htpasswd admin
        #makes/appends to a file with usernames admin/MD5 password hashes inside the project dir
        #sudo htpasswd -c <htpasswd_path_or_relpath> <username>

        tracd --port 8000 --basic-auth="trac,./.htpasswd,localhost" .
        #tracd --port 8000 --basic-auth="<project_dir>,<htpasswd_path_or_relpath>,<host>" <project_dir_path_or_relpath>
        #enables basic authentication
        #after that you can login with username password pairs in this file

    trac-admin . permission add admin TRAC_ADMIN
    firefox http://127.0.0.1:8000/trac/admin
    #trac-admin . permission add <username> TRAC_ADMIN
    #an admin item will appear on bar.

    #plugins shared install
        #plugins can also be put under your plugins dir as python eggs

        vim conf/trac.ini
        #find plugins_dir
        #add where you plugins will be.
        #in ubunutu, pip installs them under:
        # /usr/local/lib/python2.7/dist-packages
        # so this might me a good place for your plugins 

        #enable plugins

            firefox http://127.0.0.1:8000/trac/admin/general/plugin
            #as an admin, you can enable each component you want form a given plugin

            #or

            vim conf/trac.ini
            #and add/uncomment desired plugin lines.
            #this may be more precise and sure, but also harder.
