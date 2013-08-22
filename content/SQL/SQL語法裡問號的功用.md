Title: SQL prepare statement
Date: 2013-08-17 23:49
Tags: SQL, Ubuntu

<p>今天在寫程式的時候意外的看到一段SQL  </p>

<pre><code>    SELECT token FROM oauth_tokens WHERE userID = ? LIMIT 1
</code></pre>

<p>而其中的問號引起了我的注意，因為沒有看到<code>userID</code>在程式中出現，所以就查了一下SQL中問號的功用，後來在<a href="http://stackoverflow.com/questions/3727688/what-does-a-question-mark-represent-in-sql-queries">stackover裡面的這篇</a>好到答案，才發現他其實是一個好習慣，所以就順便筆記下來了</p>

<h4>問號的功能，是用來變數化SQL查詢</h4>

<p>他一種安全的作法用來取代原來的寫法</p>

<pre><code>    ODBCCommand cmd = new ODBCCommand("SELECT thingA FROM tableA WHERE thingB = 7")
    result = cmd.Execute()
</code></pre>

<p>這個寫法在<code>thingB</code>為固定值的時候沒有什麼問題，但是當你需要動態載入變數的時候，他就會需要寫成這樣（底下的方法是不建議的）</p>

<pre><code>    string s = getStudentName()
    cmd.CommandText = "SELECT * FROM students WHERE (name = '" + s + "')"
    cmd.Execute()
</code></pre>

<p>我們就很直覺的使用字串串接的方式來將變數整合成一句SQL，但是這樣會面臨<code>SQL injection</code>的危險，因為當你要寫入的變數，是來自於你不信任的第三方<em>（不論是使用者、或者是hacker）</em>都有可能串接到無法預期的文字，好一點只是SQL statement Error，但是如果對方傳入設計過的字串，例如<code>Robert'); DROP TABLE students; --</code>，則結果會...</p>

<pre><code>    SELECT* FROM students WHERE (name = Robert');
    DROP TABLE students;
</code></pre>

<p>就悲劇了，當然你可能會覺得他怎麼知道你的TABLE Name那又是另外一回事了.XD</p>

<h4>所以</h4>

<p>應該改用這種方式，除了程式有比較好的可讀性以外，還可以事先過濾使用者輸入的字串</p>

<pre><code>    ODBCCommand cmd = new ODBCCommand("SELECT thingA FROM tableA WHERE thingB = ?")
    cmd.Parameters.Add(7)
    result = cmd.Execute()
</code></pre>

<p>當然你也可以使用<a href="http://php.net/manual/en/book.pdo.php">php PDO</a>的方式來寫入</p>

<pre><code>    $query = 'SELECT token FROM oauth_tokens WHERE userID = ? LIMIT 1';
    $stmt = $this-&gt;pdo-&gt;prepare($query);
    $stmt-&gt;execute(array($this-&gt;userID));
</code></pre>

<p>都是一種好習慣也是一種好方法:D</p>
