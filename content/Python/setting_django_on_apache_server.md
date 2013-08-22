Title: setting django on apache server
Date: 2013-08-17 23:50
Tags: Django, Ubuntu

  如果有在ubuntu上架設過LAMP的應該都知道，其實就是幾個指令，設定好密碼，還可以裝個phpmyadmin來管理資料庫，他的方便性大大降低了他的門檻，本著如此方便的精神，我覺得「安裝Django應該也很簡單吧？」就開始這段錯誤的過程，因為python不算是native支援網頁顯示的，使用一些module，或是使用以前CGI的方式來讓apache驅動他，外加上Django其實是包好好的Framework，所以在設定上就有這麼不人性點。所以，經過這麼多波折，我決定把這些過程記錄下來XD。

###環境設定

首先，你需要
1. 安裝server，並且安裝wsgi的module
    
        sudo apt-get install apache2 libapache2-mod-wsgi

2. 安裝[python pip](http://www.openfoundry.org/tw/tech-column/8536-introduction-of-python-extension-management-tools)

        sudo apt-get install python-setuptools

3. 最後，再用pip安裝Django，之後的問題就隨之而來了（誤

        sudo pip install django

之後，在你想要撰寫的目錄下，新增一個資料夾，用來管理之後的程式（我是在家目錄底下新增/home/lucas/django）

        mkdir ~/django

###IP設定

在hosts中新增幾個IP

>vi /etc/hosts

    127.0.0.1   localhost
    127.0.0.2   wsgi.djangoserver
    127.0.0.3   hello.djangoserver

###測試WSGI是否可以執行

創建資料夾

>   mkdir ~/django/myapp

新增python的應用程式`wsgi.app`

>   vi ~/django/myapp/wsgi.app

        def application(environ, start_response):
            status = '200 OK'
            output = 'Hello World!'
         
            response_headers = [('Content-type', 'text/plain'),
                                ('Content-Length', str(len(output)))]
            start_response(status, response_headers)
         
            return [output]
新增apache的設定

>   sudo vi /etc/apache2/sites-available/wsgi

        <VirtualHost *:80>
         
            ServerName wsgi.djangoserver
            DocumentRoot /home/lucas/django
         
            <Directory /home/lucas/django>
                Order allow,deny
                Allow from all
            </Directory>
         
            WSGIScriptAlias / /home/lucas/django/myapp/wsgi.app         
        </VirtualHost>
將設定檔生效

>   sudo a2ensite
>   sudo service apache2 reload

測試你的wsgi是否有效
[http://wsgi.djangoserver](http://wsgi.djangoserver)如果沒有看到`Hello World!`表示wsgi的設定就有問題了，可能需要先完成這個步驟，才可以繼續設定你的環境。

###測試Django是否可以安裝

開啟一個Django的project

>   mkdir ~/django
>   python django-admin.py mysite

設定一個網站的wsgi file

>   mkdir ~/django/apache
>   vi ~/django/apache/django.wsgi

編輯`django.wsgi`的內容

    import os
    import sys
     
    path = '/srv/www'
    if path not in sys.path:
        sys.path.insert(0, '/srv/www')
     
    os.environ['DJANGO_SETTINGS_MODULE'] = 'hello.settings'
     
    import django.core.handlers.wsgi
    application = django.core.handlers.wsgi.WSGIHandler()

新增一個apache site
-----

>   sudo vi /etc/apache2/site-available/hello

編輯`hello`的內容

   <VirtualHost *:80>
 
    ServerName hello.djangoserver
    DocumentRoot /srv/www/hello
 
    <Directory /srv/www/hello>
        Order allow,deny
        Allow from all
    </Directory>
 
    WSGIDaemonProcess hello.djangoserver processes=2 threads=15 display-name=%{GROUP}
    WSGIProcessGroup hello.djangoserver
 
    WSGIScriptAlias / /srv/www/hello/apache/django.wsgi
 
    </VirtualHost>

啟動apache site

>   sudo a2ensite hello
>   sudo /etc/init.d/apache2 reload

使用瀏覽器啟動[http://hello.djangoserver](http://hello.djangoserver)你就會看到歡迎頁面了

參考：
[Installing Django with Apache and mod_wsgi on Ubuntu 10.04](http://blog.stannard.net.au/2010/12/11/installing-django-with-apache-and-mod_wsgi-on-ubuntu-10-04/)
[Django, Apache and mod_wsgi on Ubuntu 10.04 (Lucid)](http://library.linode.com/frameworks/django-apache-mod-wsgi/ubuntu-10.04-lucid#sph_configure-django-applications-for-wsgi)
