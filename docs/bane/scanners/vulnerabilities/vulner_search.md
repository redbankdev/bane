<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1" />
<meta name="generator" content="pdoc 0.10.0" />
<title>bane.scanners.vulnerabilities.vulner_search API documentation</title>
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
<h1 class="title">Module <code>bane.scanners.vulnerabilities.vulner_search</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.scanners.vulnerabilities.utils import *

def vulners_search(
    software,
    url=&#34;https://vulners.com/api/v3/burp/software/&#34;,
    file_name=&#34;&#34;,
    save_to_file=False,
    max_vulnerabilities=100,
    version=&#34;&#34;,
    software_type=&#34;software&#34;,
    user_agent=None,
    cookie=None,
    api_key=&#39;&#39;,
    proxy=None,
    timeout=20,
):
    if api_key==None:
        api_key=&#39;&#39;
    if not file_name:
        if version:
            file_name = software + &#34;_&#34; + version.replace(&#34;.&#34;, &#34;-&#34;)
        else:
            file_name = software
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        hea = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        hea = {&#34;User-Agent&#34;: us}
    try:
        ver = &#34;&#34;
        if version:
            ver = version
        max_vuln = 100
        if max_vulnerabilities:
            max_vuln = max_vulnerabilities
        ty = &#34;software&#34;
        if software_type:
            ty = software_type
        if ty not in [&#34;software&#34;, &#34;cpe&#34;]:
            raise Exception(&#39;type must be: &#34;software&#34; or &#34;cpe&#34;&#39;)
        d = {
            &#34;maxVulnerabilities&#34;: max_vuln,
            &#34;version&#34;: ver,
            &#34;type&#34;: ty,
            &#34;software&#34;: software,
            &#39;apikey&#39;:api_key
        }
        r = requests.Session().get(
            url,
            params=d,
            headers=hea,
            proxies=proxy,
            timeout=timeout,
            verify=False,
        )
        c = json.loads(r.text)
        if c[&#34;result&#34;] == &#34;OK&#34;:
            if save_to_file==True:
                with open(file_name.split(&#34;.&#34;)[0] + &#34;.json&#34;, &#34;w&#34;) as outfile:
                    json.dump(c, outfile, indent=4)
                outfile.close()
            l = []
            m = c[&#34;data&#34;][&#34;search&#34;]
            i = 0
            for x in m:
                #print(x)
                l.append(
                     x[
                            &#34;_source&#34;
                        ]
                )
                i += 1
            return l
        else:
            return {&#39;error&#39;:&#34;couldn&#39;t find vulnerabilities for this version&#34;}
    except:
        pass
    return []</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="bane.scanners.vulnerabilities.vulner_search.vulners_search"><code class="name flex">
<span>def <span class="ident">vulners_search</span></span>(<span>software, url='https://vulners.com/api/v3/burp/software/', file_name='', save_to_file=False, max_vulnerabilities=100, version='', software_type='software', user_agent=None, cookie=None, api_key='', proxy=None, timeout=20)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def vulners_search(
    software,
    url=&#34;https://vulners.com/api/v3/burp/software/&#34;,
    file_name=&#34;&#34;,
    save_to_file=False,
    max_vulnerabilities=100,
    version=&#34;&#34;,
    software_type=&#34;software&#34;,
    user_agent=None,
    cookie=None,
    api_key=&#39;&#39;,
    proxy=None,
    timeout=20,
):
    if api_key==None:
        api_key=&#39;&#39;
    if not file_name:
        if version:
            file_name = software + &#34;_&#34; + version.replace(&#34;.&#34;, &#34;-&#34;)
        else:
            file_name = software
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        hea = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        hea = {&#34;User-Agent&#34;: us}
    try:
        ver = &#34;&#34;
        if version:
            ver = version
        max_vuln = 100
        if max_vulnerabilities:
            max_vuln = max_vulnerabilities
        ty = &#34;software&#34;
        if software_type:
            ty = software_type
        if ty not in [&#34;software&#34;, &#34;cpe&#34;]:
            raise Exception(&#39;type must be: &#34;software&#34; or &#34;cpe&#34;&#39;)
        d = {
            &#34;maxVulnerabilities&#34;: max_vuln,
            &#34;version&#34;: ver,
            &#34;type&#34;: ty,
            &#34;software&#34;: software,
            &#39;apikey&#39;:api_key
        }
        r = requests.Session().get(
            url,
            params=d,
            headers=hea,
            proxies=proxy,
            timeout=timeout,
            verify=False,
        )
        c = json.loads(r.text)
        if c[&#34;result&#34;] == &#34;OK&#34;:
            if save_to_file==True:
                with open(file_name.split(&#34;.&#34;)[0] + &#34;.json&#34;, &#34;w&#34;) as outfile:
                    json.dump(c, outfile, indent=4)
                outfile.close()
            l = []
            m = c[&#34;data&#34;][&#34;search&#34;]
            i = 0
            for x in m:
                #print(x)
                l.append(
                     x[
                            &#34;_source&#34;
                        ]
                )
                i += 1
            return l
        else:
            return {&#39;error&#39;:&#34;couldn&#39;t find vulnerabilities for this version&#34;}
    except:
        pass
    return []</code></pre>
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
<li><code><a title="bane.scanners.vulnerabilities" href="index.html">bane.scanners.vulnerabilities</a></code></li>
</ul>
</li>
<li><h3><a href="#header-functions">Functions</a></h3>
<ul class="">
<li><code><a title="bane.scanners.vulnerabilities.vulner_search.vulners_search" href="#bane.scanners.vulnerabilities.vulner_search.vulners_search">vulners_search</a></code></li>
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