<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.cryptographers.base64</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.cryptographers.utils import *

def base64_encode(w, encode=None):
    if w:
        if encode:
            w.encode(encode)
        &#34;&#34;&#34;
   function to return base64 encoded string
  &#34;&#34;&#34;
        return base64.b64encode(w)


def base64_decode(w, encode=None):
    if w:
        if encode:
            w.encode(encode)
        &#34;&#34;&#34;
   function to return base64 decoded string
  &#34;&#34;&#34;
        return base64.b64decode(w)



def base64_encode_file(f):
    if f:
        with open(f, &#34;rb&#34;) as f:
            w = f.read()
        f.close()
        return base64_encode(w)


def base64_decode_file(f):
    if f:
        with open(f, &#34;rb&#34;) as f:
            w = f.read()
        f.close()
        return base64_decode(w)</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="bane.cryptographers.base64.base64_decode"><code class="name flex">
<span>def <span class="ident">base64_decode</span></span>(<span>w, encode=None)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def base64_decode(w, encode=None):
    if w:
        if encode:
            w.encode(encode)
        &#34;&#34;&#34;
   function to return base64 decoded string
  &#34;&#34;&#34;
        return base64.b64decode(w)</code></pre>
</details>
</dd>
<dt id="bane.cryptographers.base64.base64_decode_file"><code class="name flex">
<span>def <span class="ident">base64_decode_file</span></span>(<span>f)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def base64_decode_file(f):
    if f:
        with open(f, &#34;rb&#34;) as f:
            w = f.read()
        f.close()
        return base64_decode(w)</code></pre>
</details>
</dd>
<dt id="bane.cryptographers.base64.base64_encode"><code class="name flex">
<span>def <span class="ident">base64_encode</span></span>(<span>w, encode=None)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def base64_encode(w, encode=None):
    if w:
        if encode:
            w.encode(encode)
        &#34;&#34;&#34;
   function to return base64 encoded string
  &#34;&#34;&#34;
        return base64.b64encode(w)</code></pre>
</details>
</dd>
<dt id="bane.cryptographers.base64.base64_encode_file"><code class="name flex">
<span>def <span class="ident">base64_encode_file</span></span>(<span>f)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def base64_encode_file(f):
    if f:
        with open(f, &#34;rb&#34;) as f:
            w = f.read()
        f.close()
        return base64_encode(w)</code></pre>
</details>
</dd>
</dl>
</section>
<section>
</section>
</article>
<nav id="sidebar">
<h1>Index</h1>
<div class="toc">
<ul></ul>
</div>
<ul id="index">
<li><h3>Super-module</h3>
<ul>
<li><code><a title="bane.cryptographers" href="index.md">bane.cryptographers</a></code></li>
</ul>
</li>
<li><h3><a href="#header-functions">Functions</a></h3>
<ul class="">
<li><code><a title="bane.cryptographers.base64.base64_decode" href="#bane.cryptographers.base64.base64_decode">base64_decode</a></code></li>
<li><code><a title="bane.cryptographers.base64.base64_decode_file" href="#bane.cryptographers.base64.base64_decode_file">base64_decode_file</a></code></li>
<li><code><a title="bane.cryptographers.base64.base64_encode" href="#bane.cryptographers.base64.base64_encode">base64_encode</a></code></li>
<li><code><a title="bane.cryptographers.base64.base64_encode_file" href="#bane.cryptographers.base64.base64_encode_file">base64_encode_file</a></code></li>
</ul>
</li>
</ul>
</nav>
</main>
<footer id="footer">
<p>Generated by <a href="https://pdoc3.github.io/pdoc" title="pdoc: Python API documentation generator"><cite>pdoc</cite> 0.10.0</a>.</p>
</footer>
</body>
</html>