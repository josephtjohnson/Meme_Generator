<h1>Meme Generator</h1>
<p>Meme generator that can be utilized via web or CLI.<p>

<h2>Using the Meme Generator (Web)</h2>
<ol>
  <li><p>Run the following for your system:</p></li>
  <ul>
    <li><p>Bash</p></li>
      <ul>
        <li><code>export FLASK_APP=app.py</code></li>
      </ul>
    <li><p>CMD</p></li>
      <ul>
        <li><code>set FLASK_APP=app.py</code></li>
      </ul>
    <li><p>PowerShell</p></li>
      <ul>
        <li><code>$env FLASK_APP=app.py</code></li>
      </ul>
  </ul>
  <li><p>Run <code>flask run</code></p></li>
  <li>Generated meme will be located under the <code>static</code> folder</li>
</ol>

<h2>Using the Meme Generator (CLI)</h2>
<ol>
  <li>Run<code>python main.py</code> to generate a meme with a random image, quote, and author.</li>
  <li>Run<code>python main.py --path {insert image url} --body {insert quote} --author {insert author} --category {insert category}</code> to create a custom meme.</li>
  <ul>
    <li>Note: if --path not specified a random image will be used. Both --body and --author are required to add a unique quote.</li>
  </ul>
  <li>Generated meme will be located under the <code>tmp</code> folder</li>
</ol>

<h2>Libraries</h2>
<ul>
  <li>Python</li>
  <li>Flask</li>
  <li>Libraries</li>
    <ul>
      <li>pandas</li>
      <li>Pillow</li>
      <li>flask</li>
      <li>requests</li>
      <li>argparser</li>
      <li>python-docx</li>
    </ul>
</ul>
  
<h2>License</h2>
<p>MIT <a href="/josephtjohnson/Meme_Generator/blob/main/LICENSE.md">License</a><p>

<h2>Author</h2>
<p>Joseph Johnson</p>
