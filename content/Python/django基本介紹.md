Title: django基本介紹
Date: 2013-08-17 23:49
Tags: Django, Ubuntu

趁著專題結束，趕快把Django的內容寫下一些紀錄，方便自己以後要用的時候可以查找，也因為雖然他的文件很完善了XD，但是因為是英文比較難閱讀，而且也需要許多實作來驗證想法，因此想要寫些筆記把心得跟細節記錄下來。

需要知道Django在Ubuntu上如何安裝與基本的運行，請參照[這篇][blog]

[blog]: http://lucaswei.blogspot.tw/2012/01/ubuntu-django.html

##首先

在command line鍵入

    django-admin.py --version

我使用的版本文1.4.1，作業系統為Ubuntu12.04，所以如果以前或者以後的版本可能會有相容性的問題。

##建立一個project

使用command line輸入

    django-admin.py startproject myproject

_myproject可以置換成自己想要的專案名稱_

之後會得到一個資料夾，用剛才的專案名稱命名，使用cd切換進去後，可以看到以下許多檔案。

    mysite/
        manage.py
        mysite/
            __init__.py
            settings.py
           urls.py
            wsgi.py

接著輸入

    cd myproject
    python manage.py runserver

如果看到

>Validating models...
>
>0 errors found
>Django version 1.4.1, using settings 'myproject.settings'
>Development server is running at http://127.0.0.1:8000/

接著使用瀏覽器開啟http://127.0.0.1:8000/就可以看到成功頁面了

（歡樂的It worked!）

###setting.py
所有Django的設定擺放的地方，其中包含許多基本的設定；在創建之後裡面有些項目必須先設定，以方便之後的開發。

####資料庫的設定

大部分的web framework都會需要用到資料庫，所以可以優先設定，以下為設定好的例子（以MySQL為例子）

    :::python
    DATABASES = {
        'default': {
            # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'ENGINE': 'django.db.backends.mysql',
            # Or path to database file if using sqlite3.
            'NAME': 'django',
            # Not used with sqlite3.
            'USER': 'lucas',
            # Not used with sqlite3.
            'PASSWORD': 'lucas_password',
            # Set to empty string for localhost. Not used with sqlite3.
            'HOST': '',
            # Set to empty string for default. Not used with sqlite3.
            'PORT': '',
        }
    }

其中最重要的就是**ENGINE**,**NAME**,**USER**,**PASSWORD**需要設定，比較細部的設定可以參考[官方的Database setup][]

_如果是MySQL使用者，記得設定完後去資料庫中新增一個資料庫，而且名字必須要跟設定中的**NAME**相同，以此為例就需要一個**django**為名稱的資料庫。_

[官方的Database setup]: https://docs.djangoproject.com/en/1.4/intro/tutorial01/#database-setup

####時區設定

    :::python
    TIME_ZONE = 'Asia/Taipei'
    LANGUAGE_CODE = 'zh-tw'

如何挑選所在的時區可以參照[wiki][wiki]

[wiki]:http://en.wikipedia.org/wiki/List_of_tz_zones_by_name

##urls.py

整個專案中，用來設定對於網站的request應該開啟哪個頁面的重要設定檔案，寫好網站mapping的pattern後，之後的request都會根據此份檔案。


