Title: 網誌搬遷-改用pelican靜態網誌生成器
Date: 2013-08-22 21:07
Tags: python, pelican

![搬家](/static/images/搬家.jpg)

一直想試試[github page][]很久了，但是基於懶惰與種種因素...所以一直沒有機會去研究，最近因為想要重新拾起寫網誌的習慣，所以上網研究了許多部落格的方案，
因為雖然想要研究[github page][]，但是很多東西還是要重新研究，難免讓人覺得「只是想要寫個網誌而已，需要搞的這麼麻煩嗎？」，
就因為這種懶惰的心態作祟，所以一直很不想直接去研究，而在當初的時間還有考慮使用[Logdown][]，不過最後還是選擇了[github page][]

[github page]: http://pages.github.com/
[Logdown]: http://logdown.com/

###選擇自己hosting部落格，而不使用Blogger的原因

最初有這個念頭是因為Blogger的編輯器是屬於[所見即所得][]的編輯界面，一來很多編輯過的文字特性沒有可稀性，因為編寫完後的內容，會被轉換成**沒有維護性**的HTML程式碼，所以沒有辦法使用到其他地方，除非你尋著原本的HTML使用，
二來，張貼程式碼很不方便，要在一般界面和原始碼界面之間切換，當初使用的方法是先把文字內容編輯好後，再切換到HTML編輯器一一插入片段的程式碼，除了常常插錯，也沒有辦法針對程式碼做syntax highlight。

因為編寫的文章比較沒有需要許多絢麗的特效，所以考慮使用[markdown][]進行編輯，等到編輯好了之後，再將markdown轉換成HTML直接貼到blogger的編輯界面上；既可以備份原始文字，也解決了編輯不方便的問題。
但也因為如此，這個步驟變得很麻煩，而且日後如果需要修改網誌的內容我也必須修改我自己備份好的markdown，再重新編輯、上傳，自己也需要另外使用服務來備份自己的markdown內容。

[所見即所得]: http://en.wikipedia.org/wiki/WYSIWYG
[markdown]: http://daringfireball.net/projects/markdown/syntax

#### 因此出現了選擇以markdown為主要編輯器的網誌的念頭

所以手中的選擇剩下github page和Logdown，但是考量到備份，以及修改的方便性，最後選擇了github page。

因為目前Logdown所提供的編輯界面雖然很好編輯，但是在主題更換，以及自行修改網誌界面、內容上，還沒有很成熟，
因此我就在想「怎樣的維護、編輯方式，對我來說是最方便的？」，因為自己有編寫javascript、CSS的經驗，很多時候可以直接改內容是最方便的，
所以最後覺得自己尋找靜態的部落格引擎自己編輯後上傳架設，除了這些優點，
因為他是靜態的，需要架設這個部落格的伺服器要求變得相對低很多，也不用考慮動態程式需要考慮的安全問題，最後決定選擇了github page和靜態部落格引擎。

### 引擎挑選

![Pelican](/static/images/Pelican.png)

搜尋靜態部落格引擎中，最大宗的關鍵字不外乎是[octopress][]和[jekyll][]，而這兩者又是使用Ruby寫成的，其中[jekyll][]是github page中推薦的靜態引擎，不過因為自己對於python的熟悉度是比較高的，
總是會希望自己選擇的靜態引擎可以以python為開發語言，所以就上網搜尋大家推薦的靜態引擎，就意外找到很多人推薦的[Pelican][]，
再經過搜尋與研究後，發現目前沒有什麼大問題，而且官方文件很詳細也很齊全，所以就選擇了他來進行使用。

[octopress]: http://octopress.org/
[jekyll]: http://jekyllrb.com/
[Pelican]: http://docs.getpelican.com/en/3.2/

### 安裝

#### 安裝Pelican

可以參考官方的安裝指示[Getting started][]v3.2
如果要使用markdown需要另外安裝

    :::bash
    sudo pip install markdown

[Getting started]: http://docs.getpelican.com/en/3.2/getting_started.html

#### 申請一個github page帳號

開一個repo，名稱需要和帳號相同，並且clone回本地端，因為github page顯示的主要是branch:master的內容，所以需要先開一個branch用來存放網誌的內容，

    :::bash
    git branch --orphan gh-pages

再把pelican-quickstart的資料夾移入，或者在這個branch進行quickstart

#### 修改Makefile


### Reference

1. [用 Pelican 和 GitHub Pages 搭建免费的个人博客 | 晓风'Blog'](http://www.dongxf.com/3_Build_Personal_Blog_With_Pelican_And_GitHub_Pages.html)
2. [網誌搬家！改用 Pelican + GitHub Pages | J. S. Liang (Jenny)](http://jsliang.com/blog/2013/02/moving-to-pelican-hosting-on-github-pages.html)
3. [從octorpess搬家到pelican](http://blog.codylab.com/From-Octopress-To-Pelican/)
