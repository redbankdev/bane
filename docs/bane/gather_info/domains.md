<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1" />
<meta name="generator" content="pdoc 0.10.0" />
<title>bane.gather_info.domains API documentation</title>
<meta name="description" content="" />
<link rel="preload stylesheet" as="style" href="https://cdnjs.cloudflare.com/ajax/libs/10up-sanitize.css/11.0.1/sanitize.min.css" integrity="sha256-PK9q560IAAa6WVRRh76LtCaI8pjTJ2z11v0miyNNjrs=" crossorigin>
<link rel="preload stylesheet" as="style" href="https://cdnjs.cloudflare.com/ajax/libs/10up-sanitize.css/11.0.1/typography.min.css" integrity="sha256-7l/o7C8jubJiy74VsKTidCy1yBkRtiUGbVkYBylBqUg=" crossorigin>
<link rel="stylesheet preload" as="style" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/styles/github.min.css" crossorigin>
<style>:root{--highlight-color:#fe9}.flex{display:flex !important}body{line-height:1.5em}#content{padding:20px}#sidebar{padding:30px;overflow:hidden}#sidebar > *:last-child{margin-bottom:2cm}.http-server-breadcrumbs{font-size:130%;margin:0 0 15px 0}#footer{font-size:.75em;padding:5px 30px;border-top:1px solid #ddd;text-align:right}#footer p{margin:0 0 0 1em;display:inline-block}#footer p:last-child{margin-right:30px}h1,h2,h3,h4,h5{font-weight:300}h1{font-size:2.5em;line-height:1.1em}h2{font-size:1.75em;margin:1em 0 .50em 0}h3{font-size:1.4em;margin:25px 0 10px 0}h4{margin:0;font-size:105%}h1:target,h2:target,h3:target,h4:target,h5:target,h6:target{background:var(--highlight-color);padding:.2em 0}a{color:#058;text-decoration:none;transition:color .3s ease-in-out}a:hover{color:#e82}.title code{font-weight:bold}h2[id^="header-"]{margin-top:2em}.ident{color:#900}pre code{background:#f8f8f8;font-size:.8em;line-height:1.4em}code{background:#f2f2f1;padding:1px 4px;overflow-wrap:break-word}h1 code{background:transparent}pre{background:#f8f8f8;border:0;border-top:1px solid #ccc;border-bottom:1px solid #ccc;margin:1em 0;padding:1ex}#http-server-module-list{display:flex;flex-flow:column}#http-server-module-list div{display:flex}#http-server-module-list dt{min-width:10%}#http-server-module-list p{margin-top:0}.toc ul,#index{list-style-type:none;margin:0;padding:0}#index code{background:transparent}#index h3{border-bottom:1px solid #ddd}#index ul{padding:0}#index h4{margin-top:.6em;font-weight:bold}@media (min-width:200ex){#index .two-column{column-count:2}}@media (min-width:300ex){#index .two-column{column-count:3}}dl{margin-bottom:2em}dl dl:last-child{margin-bottom:4em}dd{margin:0 0 1em 3em}#header-classes + dl > dd{margin-bottom:3em}dd dd{margin-left:2em}dd p{margin:10px 0}.name{background:#eee;font-weight:bold;font-size:.85em;padding:5px 10px;display:inline-block;min-width:40%}.name:hover{background:#e0e0e0}dt:target .name{background:var(--highlight-color)}.name > span:first-child{white-space:nowrap}.name.class > span:nth-child(2){margin-left:.4em}.inherited{color:#999;border-left:5px solid #eee;padding-left:1em}.inheritance em{font-style:normal;font-weight:bold}.desc h2{font-weight:400;font-size:1.25em}.desc h3{font-size:1em}.desc dt code{background:inherit}.source summary,.git-link-div{color:#666;text-align:right;font-weight:400;font-size:.8em;text-transform:uppercase}.source summary > *{white-space:nowrap;cursor:pointer}.git-link{color:inherit;margin-left:1em}.source pre{max-height:500px;overflow:auto;margin:0}.source pre code{font-size:12px;overflow:visible}.hlist{list-style:none}.hlist li{display:inline}.hlist li:after{content:',\2002'}.hlist li:last-child:after{content:none}.hlist .hlist{display:inline;padding-left:1em}img{max-width:100%}td{padding:0 .5em}.admonition{padding:.1em .5em;margin-bottom:1em}.admonition-title{font-weight:bold}.admonition.note,.admonition.info,.admonition.important{background:#aef}.admonition.todo,.admonition.versionadded,.admonition.tip,.admonition.hint{background:#dfd}.admonition.warning,.admonition.versionchanged,.admonition.deprecated{background:#fd4}.admonition.error,.admonition.danger,.admonition.caution{background:lightpink}</style>
<style media="screen and (min-width: 700px)">@media screen and (min-width:700px){#sidebar{width:30%;height:100vh;overflow:auto;position:sticky;top:0}#content{width:70%;max-width:100ch;padding:3em 4em;border-left:1px solid #ddd}pre code{font-size:1em}.item .name{font-size:1em}main{display:flex;flex-direction:row-reverse;justify-content:flex-end}.toc ul ul,#index ul{padding-left:1.5em}.toc > ul > li{margin-top:.5em}}</style>
<style media="print">@media print{#sidebar h1{page-break-before:always}.source{display:none}}@media print{*{background:transparent !important;color:#000 !important;box-shadow:none !important;text-shadow:none !important}a[href]:after{content:" (" attr(href) ")";font-size:90%}a[href][title]:after{content:none}abbr[title]:after{content:" (" attr(title) ")"}.ir a:after,a[href^="javascript:"]:after,a[href^="#"]:after{content:""}pre,blockquote{border:1px solid #999;page-break-inside:avoid}thead{display:table-header-group}tr,img{page-break-inside:avoid}img{max-width:100% !important}@page{margin:0.5cm}p,h2,h3{orphans:3;widows:3}h1,h2,h3,h4,h5,h6{page-break-after:avoid}}</style>
<script defer src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/highlight.min.js" integrity="sha256-Uv3H6lx7dJmRfRvH8TH6kJD1TSK1aFcwgx+mdg3epi8=" crossorigin></script>
<script>window.addEventListener('DOMContentLoaded', () => hljs.initHighlighting())</script>
</head>
<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.gather_info.domains</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.gather_info.utils import *


def whois(u):
    try:
        r = requests.Session().post(&#34;https://check-host.net/ip-info/whois&#34;, data={&#34;host&#34;: u})
        a = r.text.split(&#34;\n\n&#34;)[0]
        b = a.split(&#34;\n&#34;)
        d = {}
        for x in b:
            d.update(
                {
                    x.split(&#34;:&#34;)[0]
                    .strip(): x.replace(x.split(&#34;:&#34;)[0].strip(), &#34;&#34;)
                    .strip()[1:]
                    .strip()
                }
            )
        return d
    except:
        pass
    return {}


def info(u, timeout=10, proxy=None, logs=False, returning=True):
    &#34;&#34;&#34;
    this function fetchs all informations about the given ip or domain using check-host.net and returns them to the use as string
    with this format:
    &#39;requested information: result&#39;

    it takes 2 arguments:

    u: ip or domain
    timeout: (set by default to: 10) timeout flag for the request
    usage:
    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;domain=&#39;www.google.com&#39;
    &gt;&gt;&gt;bane.info(domain)&#34;&#34;&#34;
    try:
        h = &#34;&#34;
        u = &#34;https://check-host.net/ip-info?host=&#34; + u
        c = requests.Session().get(
            u, headers={&#34;User-Agent&#34;: random.choice(ua)}, proxies=proxy, timeout=timeout
        ).text
        soup = BeautifulSoup(c, &#34;html.parser&#34;)
        la = soup.find_all(&#34;a&#34;)
        l = []
        for i in la:
            if &#34;#ip_info-dbip&#34; in str(i):
                l.append(remove_html_tags(str(i)).strip().replace(&#34;\n&#34;, &#34; &#34;))
            if &#34;#ip_info-ip2location&#34; in str(i):
                l.append(remove_html_tags(str(i)).strip().replace(&#34;\n&#34;, &#34; &#34;))
            if &#34;#ip_info-geolite2&#34; in str(i):
                l.append(remove_html_tags(str(i)).strip().replace(&#34;\n&#34;, &#34; &#34;))
        p = soup.find_all(&#34;table&#34;)
        o = 0
        di = {}
        for x in p:
            try:
                do = {}
                y = x.find_all(&#34;tr&#34;)
                for w in y:
                    a = w.find_all(&#34;td&#34;)
                    try:
                        c = str(a[0]).split(&#34;&lt;td&gt;&#34;)[1].split(&#34;&lt;/td&gt;&#34;)[0].strip()
                        d = str(a[1]).split(&#34;&lt;td&gt;&#34;)[1].split(&#34;&lt;/td&gt;&#34;)[0].strip()
                        d = remove_html_tags(d).strip().replace(&#34;\n&#34;, &#34; &#34;)
                        do.update({c: d})
                    except:
                        pass
                di.update({l[o]: do})
                o += 1
            except:
                pass
        if logs == True:
            for x in di:
                print(x)
                print(&#34;&#34;)
                for y in di[x]:
                    print(y + &#34;: &#34; + di[x][y])
                print(&#34;&#34;)
        if returning == True:
            return di
    except:
        return None


def resolve(u, server=&#34;8.8.8.8&#34;, timeout=1, lifetime=1):
    o = []
    r = dns.resolver.Resolver()
    r.timeout = timeout
    r.lifetime = lifetime
    r.nameservers = [server]
    a = r.query(u)
    for x in a:
        o.append(str(x))
    return o</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="bane.gather_info.domains.info"><code class="name flex">
<span>def <span class="ident">info</span></span>(<span>u, timeout=10, proxy=None, logs=False, returning=True)</span>
</code></dt>
<dd>
<div class="desc"><p>this function fetchs all informations about the given ip or domain using check-host.net and returns them to the use as string
with this format:
'requested information: result'</p>
<p>it takes 2 arguments:</p>
<p>u: ip or domain
timeout: (set by default to: 10) timeout flag for the request
usage:</p>
<blockquote>
<blockquote>
<blockquote>
<p>import bane
domain='www.google.com'
bane.info(domain)</p>
</blockquote>
</blockquote>
</blockquote></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def info(u, timeout=10, proxy=None, logs=False, returning=True):
    &#34;&#34;&#34;
    this function fetchs all informations about the given ip or domain using check-host.net and returns them to the use as string
    with this format:
    &#39;requested information: result&#39;

    it takes 2 arguments:

    u: ip or domain
    timeout: (set by default to: 10) timeout flag for the request
    usage:
    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;domain=&#39;www.google.com&#39;
    &gt;&gt;&gt;bane.info(domain)&#34;&#34;&#34;
    try:
        h = &#34;&#34;
        u = &#34;https://check-host.net/ip-info?host=&#34; + u
        c = requests.Session().get(
            u, headers={&#34;User-Agent&#34;: random.choice(ua)}, proxies=proxy, timeout=timeout
        ).text
        soup = BeautifulSoup(c, &#34;html.parser&#34;)
        la = soup.find_all(&#34;a&#34;)
        l = []
        for i in la:
            if &#34;#ip_info-dbip&#34; in str(i):
                l.append(remove_html_tags(str(i)).strip().replace(&#34;\n&#34;, &#34; &#34;))
            if &#34;#ip_info-ip2location&#34; in str(i):
                l.append(remove_html_tags(str(i)).strip().replace(&#34;\n&#34;, &#34; &#34;))
            if &#34;#ip_info-geolite2&#34; in str(i):
                l.append(remove_html_tags(str(i)).strip().replace(&#34;\n&#34;, &#34; &#34;))
        p = soup.find_all(&#34;table&#34;)
        o = 0
        di = {}
        for x in p:
            try:
                do = {}
                y = x.find_all(&#34;tr&#34;)
                for w in y:
                    a = w.find_all(&#34;td&#34;)
                    try:
                        c = str(a[0]).split(&#34;&lt;td&gt;&#34;)[1].split(&#34;&lt;/td&gt;&#34;)[0].strip()
                        d = str(a[1]).split(&#34;&lt;td&gt;&#34;)[1].split(&#34;&lt;/td&gt;&#34;)[0].strip()
                        d = remove_html_tags(d).strip().replace(&#34;\n&#34;, &#34; &#34;)
                        do.update({c: d})
                    except:
                        pass
                di.update({l[o]: do})
                o += 1
            except:
                pass
        if logs == True:
            for x in di:
                print(x)
                print(&#34;&#34;)
                for y in di[x]:
                    print(y + &#34;: &#34; + di[x][y])
                print(&#34;&#34;)
        if returning == True:
            return di
    except:
        return None</code></pre>
</details>
</dd>
<dt id="bane.gather_info.domains.resolve"><code class="name flex">
<span>def <span class="ident">resolve</span></span>(<span>u, server='8.8.8.8', timeout=1, lifetime=1)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def resolve(u, server=&#34;8.8.8.8&#34;, timeout=1, lifetime=1):
    o = []
    r = dns.resolver.Resolver()
    r.timeout = timeout
    r.lifetime = lifetime
    r.nameservers = [server]
    a = r.query(u)
    for x in a:
        o.append(str(x))
    return o</code></pre>
</details>
</dd>
<dt id="bane.gather_info.domains.whois"><code class="name flex">
<span>def <span class="ident">whois</span></span>(<span>u)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def whois(u):
    try:
        r = requests.Session().post(&#34;https://check-host.net/ip-info/whois&#34;, data={&#34;host&#34;: u})
        a = r.text.split(&#34;\n\n&#34;)[0]
        b = a.split(&#34;\n&#34;)
        d = {}
        for x in b:
            d.update(
                {
                    x.split(&#34;:&#34;)[0]
                    .strip(): x.replace(x.split(&#34;:&#34;)[0].strip(), &#34;&#34;)
                    .strip()[1:]
                    .strip()
                }
            )
        return d
    except:
        pass
    return {}</code></pre>
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
<li><code><a title="bane.gather_info" href="index.html">bane.gather_info</a></code></li>
</ul>
</li>
<li><h3><a href="#header-functions">Functions</a></h3>
<ul class="">
<li><code><a title="bane.gather_info.domains.info" href="#bane.gather_info.domains.info">info</a></code></li>
<li><code><a title="bane.gather_info.domains.resolve" href="#bane.gather_info.domains.resolve">resolve</a></code></li>
<li><code><a title="bane.gather_info.domains.whois" href="#bane.gather_info.domains.whois">whois</a></code></li>
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