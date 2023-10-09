<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1" />
<meta name="generator" content="pdoc 0.10.0" />
<title>bane.scanners.vulnerabilities.cors_misconfigurations API documentation</title>
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
<h1 class="title">Module <code>bane.scanners.vulnerabilities.cors_misconfigurations</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.scanners.vulnerabilities.utils import *


def cors_reflection(
    u,
    proxy=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    origin=&#34;www.evil-domain.com&#34;,
    debug=False,
    fill=10,
    headers={}
):
    a = None
    b = None
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        heads = {&#34;User-Agent&#34;: us}
    heads.update({&#34;Origin&#34;: origin})
    heads.update(headers)
    try:
        r = requests.Session().get(
            u, headers=heads, proxies=proxy, timeout=timeout, verify=False
        ).headers
        a = r.get(&#34;Access-Control-Allow-Origin&#34;, None)
        b = r.get(&#34;Access-Control-Allow-Credentials&#34;, None)
        if debug == True:
            for x in r:
                print(x + &#34; : &#34; + r[x])
        if a and b:
            if a == origin and b == &#34;true&#34;:
                return (
                    True,
                    {
                        &#34;Access-Control-Allow-Origin&#34;: a,
                        &#34;Access-Control-Allow-Credentials&#34;: b,
                        &#34;Vulnerable&#34;: True,
                    },
                )
    except:
        pass
    return (
        False,
        {
            &#34;Access-Control-Allow-Origin&#34;: a,
            &#34;Access-Control-Allow-Credentials&#34;: b,
            &#34;Vulnerable&#34;: False,
        },
    )


def cors_wildcard(u, proxy=None, timeout=10, user_agent=None, cookie=None, debug=False,headers={}):
    a = None
    b = None
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        heads = {&#34;User-Agent&#34;: us}
    heads.update({&#34;Origin&#34;: &#34;*&#34;})
    heads.update(headers)
    try:
        r = requests.Session().get(
            u, headers=heads, proxies=proxy, timeout=timeout, verify=False
        ).headers
        a = r.get(&#34;Access-Control-Allow-Origin&#34;, None)
        b = r.get(&#34;Access-Control-Allow-Credentials&#34;, None)
        if debug == True:
            for x in r:
                print(x + &#34; : &#34; + r[x])
        if a and b:
            if a == &#34;*&#34; and b == &#34;true&#34;:
                return (
                    True,
                    {
                        &#34;Access-Control-Allow-Origin&#34;: a,
                        &#34;Access-Control-Allow-Credentials&#34;: b,
                        &#34;Vulnerable&#34;: True,
                    },
                )
    except:
        pass
    return (
        False,
        {
            &#34;Access-Control-Allow-Origin&#34;: a,
            &#34;Access-Control-Allow-Credentials&#34;: b,
            &#34;Vulnerable&#34;: False,
        },
    )


def cors_null(u, proxy=None, timeout=10, user_agent=None, cookie=None, debug=False,headers={}):
    a = None
    b = None
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        heads = {&#34;User-Agent&#34;: us}
    heads.update({&#34;Origin&#34;: &#34;null&#34;})
    heads.update(headers)
    try:
        r = requests.Session().get(
            u, headers=heads, proxies=proxy, timeout=timeout, verify=False
        ).headers
        a = r.get(&#34;Access-Control-Allow-Origin&#34;, None)
        b = r.get(&#34;Access-Control-Allow-Credentials&#34;, None)
        if debug == True:
            for x in r:
                print(x + &#34; : &#34; + r[x])
        if a and b:
            if a == &#34;null&#34; and b == &#34;true&#34;:
                return (
                    True,
                    {
                        &#34;Access-Control-Allow-Origin&#34;: a,
                        &#34;Access-Control-Allow-Credentials&#34;: b,
                        &#34;Vulnerable&#34;: True,
                    },
                )
    except:
        pass
    return (
        False,
        {
            &#34;Access-Control-Allow-Origin&#34;: a,
            &#34;Access-Control-Allow-Credentials&#34;: b,
            &#34;Vulnerable&#34;: False,
        },
    )




def proxies_select(proxy, proxies):
    if proxy:
        return proxy
    if proxies:
        return random.choice(proxies)
    return None


def cors_misconfigurations_urls(
    u,
    origin=&#34;www.evil-domain.com&#34;,
    origin_reflection=True,
    wildcard_origin=True,
    null_origin=True,
    proxy=None,
    proxies=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    logs=True,
    debug=False,
    headers={}
):
    res = {}
    if origin_reflection == True:
        if logs == True:
            print(&#34;[*] Testing for: Origin Reflection...&#34;)
        tes1 = cors_reflection(
            u,
            origin=origin,
            cookie=cookie,
            user_agent=user_agent,
            timeout=timeout,
            proxy=proxies_select(proxy, proxies),
            debug=debug,
            headers=headers
        )
        if tes1[0] == True:
            res.update({&#34;cors_reflection&#34;: tes1[1],&#39;vulnerable&#39;:True})
            if logs == True:
                print(&#34;[+] Vulnerable !!&#34;)
        else:
            res.update({&#34;cors_reflection&#34;: tes1[1],&#39;vulnerable&#39;:False})
            if logs == True:
                print(&#34;[-] Not vulnerable&#34;)
    if wildcard_origin == True:
        if logs == True:
            print(&#34;[*] Testing for: Wildcard Origin...&#34;)
        tes2 = cors_wildcard(
            u,
            cookie=cookie,
            user_agent=user_agent,
            timeout=timeout,
            proxy=proxies_select(proxy, proxies),
            debug=debug,
            headers=headers
        )
        if tes2[0] == True:
            res.update({&#34;wildcard_origin&#34;: tes2[1],&#39;vulnerable&#39;:True})
            if logs == True:
                print(&#34;[+] Vulnerable !!&#34;)
        else:
            res.update({&#34;wildcard_origin&#34;: tes2[1],&#39;vulnerable&#39;:False})
            if logs == True:
                print(&#34;[-] Not vulnerable&#34;)
    if origin_reflection == True:
        if logs == True:
            print(&#34;[*] Testing for: Null Origin...&#34;)
        tes3 = cors_null(
            u,
            cookie=cookie,
            user_agent=user_agent,
            timeout=timeout,
            proxy=proxies_select(proxy, proxies),
            debug=debug,
            headers=headers
        )
        if tes3[0] == True:
            res.update({&#34;null_origin&#34;: tes3[1],&#39;vulnerable&#39;:True})
            if logs == True:
                print(&#34;[+] Vulnerable !!&#34;)
        else:
            res.update({&#34;null_origin&#34;: tes3[1],&#39;vulnerable&#39;:False})
            if logs == True:
                print(&#34;[-] Not vulnerable&#34;)
    return res



def cors_misconfigurations(
    urls,
    origin=&#34;www.evil-domain.com&#34;,
    origin_reflection=True,
    wildcard_origin=True,
    null_origin=True,
    proxy=None,
    proxies=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    logs=True,
    debug=False,
    headers={}
):
    l=[]
    for x in urls:
        if logs==True:
            print(&#39;\n\nPage: {}\n&#39;.format(x))
        result=cors_misconfigurations_urls(x,
                                            origin=origin,
                                            origin_reflection=origin_reflection,
                                            wildcard_origin=wildcard_origin,
                                            null_origin=null_origin,
                                            proxy=proxy,
                                            proxies=proxies,
                                            timeout=timeout,
                                            user_agent=user_agent,
                                            cookie=cookie,
                                            logs=logs,
                                            debug=debug,
                                            headers=headers
                                            )
        result={&#39;vulnerable&#39;:result[0],&#39;status&#39;:result[1]}
        if logs==True:
            for r in result:
                print(r)
        l.append({&#39;page&#39;:x,&#39;result&#39;:result})
    return  [x for x in l if x[&#39;result&#39;][&#39;vulnerable&#39;]!=False]</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="bane.scanners.vulnerabilities.cors_misconfigurations.cors_misconfigurations"><code class="name flex">
<span>def <span class="ident">cors_misconfigurations</span></span>(<span>urls, origin='www.evil-domain.com', origin_reflection=True, wildcard_origin=True, null_origin=True, proxy=None, proxies=None, timeout=10, user_agent=None, cookie=None, logs=True, debug=False, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def cors_misconfigurations(
    urls,
    origin=&#34;www.evil-domain.com&#34;,
    origin_reflection=True,
    wildcard_origin=True,
    null_origin=True,
    proxy=None,
    proxies=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    logs=True,
    debug=False,
    headers={}
):
    l=[]
    for x in urls:
        if logs==True:
            print(&#39;\n\nPage: {}\n&#39;.format(x))
        result=cors_misconfigurations_urls(x,
                                            origin=origin,
                                            origin_reflection=origin_reflection,
                                            wildcard_origin=wildcard_origin,
                                            null_origin=null_origin,
                                            proxy=proxy,
                                            proxies=proxies,
                                            timeout=timeout,
                                            user_agent=user_agent,
                                            cookie=cookie,
                                            logs=logs,
                                            debug=debug,
                                            headers=headers
                                            )
        result={&#39;vulnerable&#39;:result[0],&#39;status&#39;:result[1]}
        if logs==True:
            for r in result:
                print(r)
        l.append({&#39;page&#39;:x,&#39;result&#39;:result})
    return  [x for x in l if x[&#39;result&#39;][&#39;vulnerable&#39;]!=False]</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.cors_misconfigurations.cors_misconfigurations_urls"><code class="name flex">
<span>def <span class="ident">cors_misconfigurations_urls</span></span>(<span>u, origin='www.evil-domain.com', origin_reflection=True, wildcard_origin=True, null_origin=True, proxy=None, proxies=None, timeout=10, user_agent=None, cookie=None, logs=True, debug=False, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def cors_misconfigurations_urls(
    u,
    origin=&#34;www.evil-domain.com&#34;,
    origin_reflection=True,
    wildcard_origin=True,
    null_origin=True,
    proxy=None,
    proxies=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    logs=True,
    debug=False,
    headers={}
):
    res = {}
    if origin_reflection == True:
        if logs == True:
            print(&#34;[*] Testing for: Origin Reflection...&#34;)
        tes1 = cors_reflection(
            u,
            origin=origin,
            cookie=cookie,
            user_agent=user_agent,
            timeout=timeout,
            proxy=proxies_select(proxy, proxies),
            debug=debug,
            headers=headers
        )
        if tes1[0] == True:
            res.update({&#34;cors_reflection&#34;: tes1[1],&#39;vulnerable&#39;:True})
            if logs == True:
                print(&#34;[+] Vulnerable !!&#34;)
        else:
            res.update({&#34;cors_reflection&#34;: tes1[1],&#39;vulnerable&#39;:False})
            if logs == True:
                print(&#34;[-] Not vulnerable&#34;)
    if wildcard_origin == True:
        if logs == True:
            print(&#34;[*] Testing for: Wildcard Origin...&#34;)
        tes2 = cors_wildcard(
            u,
            cookie=cookie,
            user_agent=user_agent,
            timeout=timeout,
            proxy=proxies_select(proxy, proxies),
            debug=debug,
            headers=headers
        )
        if tes2[0] == True:
            res.update({&#34;wildcard_origin&#34;: tes2[1],&#39;vulnerable&#39;:True})
            if logs == True:
                print(&#34;[+] Vulnerable !!&#34;)
        else:
            res.update({&#34;wildcard_origin&#34;: tes2[1],&#39;vulnerable&#39;:False})
            if logs == True:
                print(&#34;[-] Not vulnerable&#34;)
    if origin_reflection == True:
        if logs == True:
            print(&#34;[*] Testing for: Null Origin...&#34;)
        tes3 = cors_null(
            u,
            cookie=cookie,
            user_agent=user_agent,
            timeout=timeout,
            proxy=proxies_select(proxy, proxies),
            debug=debug,
            headers=headers
        )
        if tes3[0] == True:
            res.update({&#34;null_origin&#34;: tes3[1],&#39;vulnerable&#39;:True})
            if logs == True:
                print(&#34;[+] Vulnerable !!&#34;)
        else:
            res.update({&#34;null_origin&#34;: tes3[1],&#39;vulnerable&#39;:False})
            if logs == True:
                print(&#34;[-] Not vulnerable&#34;)
    return res</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.cors_misconfigurations.cors_null"><code class="name flex">
<span>def <span class="ident">cors_null</span></span>(<span>u, proxy=None, timeout=10, user_agent=None, cookie=None, debug=False, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def cors_null(u, proxy=None, timeout=10, user_agent=None, cookie=None, debug=False,headers={}):
    a = None
    b = None
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        heads = {&#34;User-Agent&#34;: us}
    heads.update({&#34;Origin&#34;: &#34;null&#34;})
    heads.update(headers)
    try:
        r = requests.Session().get(
            u, headers=heads, proxies=proxy, timeout=timeout, verify=False
        ).headers
        a = r.get(&#34;Access-Control-Allow-Origin&#34;, None)
        b = r.get(&#34;Access-Control-Allow-Credentials&#34;, None)
        if debug == True:
            for x in r:
                print(x + &#34; : &#34; + r[x])
        if a and b:
            if a == &#34;null&#34; and b == &#34;true&#34;:
                return (
                    True,
                    {
                        &#34;Access-Control-Allow-Origin&#34;: a,
                        &#34;Access-Control-Allow-Credentials&#34;: b,
                        &#34;Vulnerable&#34;: True,
                    },
                )
    except:
        pass
    return (
        False,
        {
            &#34;Access-Control-Allow-Origin&#34;: a,
            &#34;Access-Control-Allow-Credentials&#34;: b,
            &#34;Vulnerable&#34;: False,
        },
    )</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.cors_misconfigurations.cors_reflection"><code class="name flex">
<span>def <span class="ident">cors_reflection</span></span>(<span>u, proxy=None, timeout=10, user_agent=None, cookie=None, origin='www.evil-domain.com', debug=False, fill=10, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def cors_reflection(
    u,
    proxy=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    origin=&#34;www.evil-domain.com&#34;,
    debug=False,
    fill=10,
    headers={}
):
    a = None
    b = None
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        heads = {&#34;User-Agent&#34;: us}
    heads.update({&#34;Origin&#34;: origin})
    heads.update(headers)
    try:
        r = requests.Session().get(
            u, headers=heads, proxies=proxy, timeout=timeout, verify=False
        ).headers
        a = r.get(&#34;Access-Control-Allow-Origin&#34;, None)
        b = r.get(&#34;Access-Control-Allow-Credentials&#34;, None)
        if debug == True:
            for x in r:
                print(x + &#34; : &#34; + r[x])
        if a and b:
            if a == origin and b == &#34;true&#34;:
                return (
                    True,
                    {
                        &#34;Access-Control-Allow-Origin&#34;: a,
                        &#34;Access-Control-Allow-Credentials&#34;: b,
                        &#34;Vulnerable&#34;: True,
                    },
                )
    except:
        pass
    return (
        False,
        {
            &#34;Access-Control-Allow-Origin&#34;: a,
            &#34;Access-Control-Allow-Credentials&#34;: b,
            &#34;Vulnerable&#34;: False,
        },
    )</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.cors_misconfigurations.cors_wildcard"><code class="name flex">
<span>def <span class="ident">cors_wildcard</span></span>(<span>u, proxy=None, timeout=10, user_agent=None, cookie=None, debug=False, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def cors_wildcard(u, proxy=None, timeout=10, user_agent=None, cookie=None, debug=False,headers={}):
    a = None
    b = None
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        heads = {&#34;User-Agent&#34;: us}
    heads.update({&#34;Origin&#34;: &#34;*&#34;})
    heads.update(headers)
    try:
        r = requests.Session().get(
            u, headers=heads, proxies=proxy, timeout=timeout, verify=False
        ).headers
        a = r.get(&#34;Access-Control-Allow-Origin&#34;, None)
        b = r.get(&#34;Access-Control-Allow-Credentials&#34;, None)
        if debug == True:
            for x in r:
                print(x + &#34; : &#34; + r[x])
        if a and b:
            if a == &#34;*&#34; and b == &#34;true&#34;:
                return (
                    True,
                    {
                        &#34;Access-Control-Allow-Origin&#34;: a,
                        &#34;Access-Control-Allow-Credentials&#34;: b,
                        &#34;Vulnerable&#34;: True,
                    },
                )
    except:
        pass
    return (
        False,
        {
            &#34;Access-Control-Allow-Origin&#34;: a,
            &#34;Access-Control-Allow-Credentials&#34;: b,
            &#34;Vulnerable&#34;: False,
        },
    )</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.cors_misconfigurations.proxies_select"><code class="name flex">
<span>def <span class="ident">proxies_select</span></span>(<span>proxy, proxies)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def proxies_select(proxy, proxies):
    if proxy:
        return proxy
    if proxies:
        return random.choice(proxies)
    return None</code></pre>
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
<li><code><a title="bane.scanners.vulnerabilities.cors_misconfigurations.cors_misconfigurations" href="#bane.scanners.vulnerabilities.cors_misconfigurations.cors_misconfigurations">cors_misconfigurations</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.cors_misconfigurations.cors_misconfigurations_urls" href="#bane.scanners.vulnerabilities.cors_misconfigurations.cors_misconfigurations_urls">cors_misconfigurations_urls</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.cors_misconfigurations.cors_null" href="#bane.scanners.vulnerabilities.cors_misconfigurations.cors_null">cors_null</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.cors_misconfigurations.cors_reflection" href="#bane.scanners.vulnerabilities.cors_misconfigurations.cors_reflection">cors_reflection</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.cors_misconfigurations.cors_wildcard" href="#bane.scanners.vulnerabilities.cors_misconfigurations.cors_wildcard">cors_wildcard</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.cors_misconfigurations.proxies_select" href="#bane.scanners.vulnerabilities.cors_misconfigurations.proxies_select">proxies_select</a></code></li>
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