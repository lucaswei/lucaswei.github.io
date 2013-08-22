Title: xclip-好用的terminal file剪貼工具
Date: 2013-08-17 23:51
Tags: xclip, ubuntu

如果常使用vim編輯檔案可能會遇到一個問題，

>如果想要將某個檔案的內容複製到其他地方要怎麼辦？

因為vim是使用終端機內的文字編排，所以即使是使用滑鼠游標選取之後在貼上，難免會有許多邊界偵測的問題，以及複製到不必要的字元，因此這個時候還是需要使用GUI的編輯器（EX:geditor）來開啟並且複製。

為了減少這方面的不方便，ubuntu上有個黏貼管理的程式-**xclip**

###安裝

    sudo apt-get install xclip

or

前往[網站][site]下載

[site]: http://sourceforge.net/projects/xclip/

###用法

####終端機內

將檔案pipe到終端機的buffer內，

    cat my_file.md |xclip

如此會將需要複製的內容複製到x buffer內，等待下次需要使用的時候

    xclip -o

可以配合其他功能使用，例如：

丟到另外一份檔案中

    xclip -o >output.md

使用grep尋找行內關鍵字

    xclip -o |grep ^happy

####如果是想要儲存在GUI的暫存中


    cat my_file.md |xclip -selection clipboard

如此便可以使用滑鼠於其他地方使用貼上功能貼到任意的地方

