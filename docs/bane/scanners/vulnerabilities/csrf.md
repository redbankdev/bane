<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1" />
<meta name="generator" content="pdoc 0.10.0" />
<title>bane.scanners.vulnerabilities.csrf API documentation</title>
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
<h1 class="title">Module <code>bane.scanners.vulnerabilities.csrf</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.scanners.vulnerabilities.utils import *


def csrf_filter_tokens(u, proxy=None, timeout=10, user_agent=None, cookie=None,headers={}):
    if not cookie or len(cookie.strip()) == 0:
        raise Exception(
            &#34;This attack requires authentication !! You need to set a Cookie&#34;
        )
    res = {&#34;Vulnerable&#34;: [], &#34;Safe&#34;: []}
    f = forms_parser(
        u, timeout=timeout, user_agent=user_agent, cookie=cookie, proxy=proxy, headers=headers
    )
    f1 = forms_parser(
        u, timeout=timeout, user_agent=user_agent, cookie=cookie, proxy=proxy, headers=headers
    )
    coun = -1
    for x in f:
        coun += 1
        vuln = True
        hd_v = False
        # print(Fore.BLUE+&#34;Form: &#34;+Fore.WHITE+str(f.index(x))+Fore.BLUE+&#34;\nAction: &#34;+Fore.WHITE+x[&#39;action&#39;]+Fore.BLUE+&#34;\nMethod: &#34;+Fore.WHITE+x[&#39;method&#39;]+Style.RESET_ALL)
        for y in x[&#34;inputs&#34;]:
            # print(&#34;Name: {} | Type: {} | Value: {}&#34;.format(y[&#34;name&#34;],y[&#34;type&#34;],y[&#34;value&#34;]))
            if y[&#34;type&#34;].lower() == &#34;hidden&#34;:
                hd_v = True
            if y[&#34;type&#34;].lower() == &#34;hidden&#34; and any(
                ele in y[&#34;name&#34;].lower() for ele in csrf_strings
            ):  # and y[&#34;value&#34;]==f1f[&#34;inputs&#34;][con][&#34;value&#34;]:
                vuln = False
        if vuln == True:
            if (
                hd_v == True
            ):  # if there is no Anti-CSRF Tokens then we check if the Hidden fields can be predicted or not (keep their values or change them by request)
                # print(Fore.YELLOW+&#34;[i] Validating hidden values&#39; prediction...&#34;+Style.RESET_ALL)
                for i in x[&#34;hidden_values&#34;]:
                    if len(x[&#34;hidden_values&#34;][i]) &gt; 0:
                        if x[&#34;hidden_values&#34;][i] != f1[coun][&#34;hidden_values&#34;][i]:
                            vuln = False
        if vuln == True:
            colr = Fore.GREEN
            &#34;&#34;&#34;if logs==True:
    print (colr+&#34;[+] Vulnerable&#34;+Style.RESET_ALL)&#34;&#34;&#34;
            res[&#34;Vulnerable&#34;].append(x)
        else:
            colr = Fore.RED
            &#34;&#34;&#34;if logs==True:
    print (colr+&#34;[-] Not vulnerable&#34;+Style.RESET_ALL)&#34;&#34;&#34;
            res[&#34;Safe&#34;].append(x)
    return res


def csrf_forms(
    u,
    proxy=None,
    timeout=10,
    show_warnings=True,
    user_agent=None,
    cookie=None,
    replaceble_parameters={&#34;phpvalue&#34;: ((&#34;.&#34;, &#34;&#34;),)},
    file_extension=&#34;png&#34;,
    fill_empty=10,
    referer=&#34;http://www.evil.com&#34;,
    leave_empty=[],
    dont_send=[],
    mime_type=None,
    predefined_inputs={},
    headers={}
):
    vu = []
    if not cookie or len(cookie.strip()) == 0:
        raise Exception(
            &#34;This attack requires authentication !! You need to set a Cookie&#34;
        )
    v = csrf_filter_tokens(
        u, proxy=proxy, timeout=timeout, user_agent=user_agent, cookie=cookie, headers=headers
    )[&#34;Vulnerable&#34;]
    if user_agent:
        h = {&#34;User-Agent&#34;: user_agent}
    else:
        h = {&#34;User-Agent&#34;: random.choice(ua)}
    h.update({&#34;cookie&#34;: cookie})
    h.update(
        {
            &#34;Referer&#34;: referer,
            &#34;Origin&#34;: referer.split(&#34;://&#34;)[0]
            + &#34;://&#34;
            + referer.split(&#34;://&#34;)[1].split(&#34;/&#34;)[0],
        }
    )
    h.update(headers)
    for x in v:
        x = form_filler(
            x,
            &#34;&#34;,
            &#34;&#34;,
            file_extension=file_extension,
            auto_fill=fill_empty,
            leave_empty=leave_empty,
            dont_send=dont_send,
            mime_type=mime_type,
            predefined_inputs=predefined_inputs,
        )
        d, f = setup_to_submit(x)
        for g in d:
            for y in replaceble_parameters:
                if x == y:
                    for z in replaceble_parameters[y]:
                        d[g] = d[g].replace(z[0], z[1])
        l = [d[y] for y in d]
        for j in f:
            l.append(f[j][0])
        if x[&#34;method&#34;] == &#34;get&#34;:
            r = requests.Session().get(
                x[&#34;action&#34;], params=d, proxies=proxy, timeout=timeout, headers=h,verify=False,
            )
        else:
            if &#34;application/json&#34; in x[&#34;enctype&#34;]:
                d = json.dumps(d)
            r = requests.Session().post(
                x[&#34;action&#34;], data=d, files=f, proxies=proxy, timeout=timeout, headers=h,verify=False,
            )
        if all(i in r.text for i in l):
            vu.append({&#39;form&#39;:x, &#39;status&#39;:&#34;Found all data&#34;})
        elif r.status_code == 200 and any(i in r.text for i in l):
            vu.append({&#39;form&#39;:x, &#39;status&#39;:&#34;Found some data&#34;})
            if show_warnings == True:
                print(
                    &#34;Warning: HTTP Status Code: 200 , but we didn&#39;t find some of our submitted data, so it&#39;s probably vulnerable but they are saved somewhere else..\nPlease check manually by visiting the form again&#34;
                )
        elif (
            r.status_code == 200
            and not any(i in r.text for i in l)
            and any(
                i in r.text.lower() for i in [&#34;unauthorized&#34;, &#34;invalid&#34;, &#34;unacceptable&#34;]
            )
        ):
            return False
        elif r.status_code == 200 and not any(i in r.text for i in l):
            if show_warnings == True:
                print(
                    &#34;Warning: HTTP Status Code: 200 , but we didn&#39;t find any of our submitted data, so it&#39;s probably vulnerable but they are saved somewhere else..\nPlease check manually by visiting the form again&#34;
                )
            vu.append({&#39;form&#39;:x, &#39;status&#39;:&#34;Found no data but Status Code: 200&#34;})
    return vu


def csrf(
    u,
    max_pages=5,
    logs=True,
    proxy=None,
    timeout=10,
    show_warnings=True,
    user_agent=None,
    cookie=None,
    replaceble_parameters={&#34;phpvalue&#34;: ((&#34;.&#34;, &#34;&#34;),)},
    file_extension=&#34;png&#34;,
    fill_empty=10,
    referer=&#34;http://www.evil.com&#34;,
    leave_empty=[],
    dont_send=[],
    mime_type=None,
    predefined_inputs={},
    pages=[],
    headers={}
):
    l=[]
    if pages==[]:
        pages=spider_url(u,cookie=cookie,max_pages=max_pages,timeout=timeout,user_agent=user_agent,proxy=proxy)
    for x in pages:
        if logs==True:
            print(&#39;\n\nPage: {}\n&#39;.format(x))
        result=csrf_forms(x,
                        proxy=proxy,
                        timeout=timeout,
                        show_warnings=show_warnings,
                        user_agent=user_agent,
                        cookie=cookie,
                        replaceble_parameters=replaceble_parameters,
                        file_extension=file_extension,
                        fill_empty=fill_empty,
                        referer=referer,
                        leave_empty=leave_empty,
                        dont_send=dont_send,
                        mime_type=mime_type,
                        predefined_inputs=predefined_inputs,
                        headers=headers)
        if logs==True:
            for r in result:
                print(r)
        l.append({&#39;page&#39;:x,&#39;result&#39;:result})
    return  [x for x in l if x[&#39;result&#39;]!=[]]</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="bane.scanners.vulnerabilities.csrf.csrf"><code class="name flex">
<span>def <span class="ident">csrf</span></span>(<span>u, max_pages=5, logs=True, proxy=None, timeout=10, show_warnings=True, user_agent=None, cookie=None, replaceble_parameters={'phpvalue': (('.', ''),)}, file_extension='png', fill_empty=10, referer='http://www.evil.com', leave_empty=[], dont_send=[], mime_type=None, predefined_inputs={}, pages=[], headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def csrf(
    u,
    max_pages=5,
    logs=True,
    proxy=None,
    timeout=10,
    show_warnings=True,
    user_agent=None,
    cookie=None,
    replaceble_parameters={&#34;phpvalue&#34;: ((&#34;.&#34;, &#34;&#34;),)},
    file_extension=&#34;png&#34;,
    fill_empty=10,
    referer=&#34;http://www.evil.com&#34;,
    leave_empty=[],
    dont_send=[],
    mime_type=None,
    predefined_inputs={},
    pages=[],
    headers={}
):
    l=[]
    if pages==[]:
        pages=spider_url(u,cookie=cookie,max_pages=max_pages,timeout=timeout,user_agent=user_agent,proxy=proxy)
    for x in pages:
        if logs==True:
            print(&#39;\n\nPage: {}\n&#39;.format(x))
        result=csrf_forms(x,
                        proxy=proxy,
                        timeout=timeout,
                        show_warnings=show_warnings,
                        user_agent=user_agent,
                        cookie=cookie,
                        replaceble_parameters=replaceble_parameters,
                        file_extension=file_extension,
                        fill_empty=fill_empty,
                        referer=referer,
                        leave_empty=leave_empty,
                        dont_send=dont_send,
                        mime_type=mime_type,
                        predefined_inputs=predefined_inputs,
                        headers=headers)
        if logs==True:
            for r in result:
                print(r)
        l.append({&#39;page&#39;:x,&#39;result&#39;:result})
    return  [x for x in l if x[&#39;result&#39;]!=[]]</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.csrf.csrf_filter_tokens"><code class="name flex">
<span>def <span class="ident">csrf_filter_tokens</span></span>(<span>u, proxy=None, timeout=10, user_agent=None, cookie=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def csrf_filter_tokens(u, proxy=None, timeout=10, user_agent=None, cookie=None,headers={}):
    if not cookie or len(cookie.strip()) == 0:
        raise Exception(
            &#34;This attack requires authentication !! You need to set a Cookie&#34;
        )
    res = {&#34;Vulnerable&#34;: [], &#34;Safe&#34;: []}
    f = forms_parser(
        u, timeout=timeout, user_agent=user_agent, cookie=cookie, proxy=proxy, headers=headers
    )
    f1 = forms_parser(
        u, timeout=timeout, user_agent=user_agent, cookie=cookie, proxy=proxy, headers=headers
    )
    coun = -1
    for x in f:
        coun += 1
        vuln = True
        hd_v = False
        # print(Fore.BLUE+&#34;Form: &#34;+Fore.WHITE+str(f.index(x))+Fore.BLUE+&#34;\nAction: &#34;+Fore.WHITE+x[&#39;action&#39;]+Fore.BLUE+&#34;\nMethod: &#34;+Fore.WHITE+x[&#39;method&#39;]+Style.RESET_ALL)
        for y in x[&#34;inputs&#34;]:
            # print(&#34;Name: {} | Type: {} | Value: {}&#34;.format(y[&#34;name&#34;],y[&#34;type&#34;],y[&#34;value&#34;]))
            if y[&#34;type&#34;].lower() == &#34;hidden&#34;:
                hd_v = True
            if y[&#34;type&#34;].lower() == &#34;hidden&#34; and any(
                ele in y[&#34;name&#34;].lower() for ele in csrf_strings
            ):  # and y[&#34;value&#34;]==f1f[&#34;inputs&#34;][con][&#34;value&#34;]:
                vuln = False
        if vuln == True:
            if (
                hd_v == True
            ):  # if there is no Anti-CSRF Tokens then we check if the Hidden fields can be predicted or not (keep their values or change them by request)
                # print(Fore.YELLOW+&#34;[i] Validating hidden values&#39; prediction...&#34;+Style.RESET_ALL)
                for i in x[&#34;hidden_values&#34;]:
                    if len(x[&#34;hidden_values&#34;][i]) &gt; 0:
                        if x[&#34;hidden_values&#34;][i] != f1[coun][&#34;hidden_values&#34;][i]:
                            vuln = False
        if vuln == True:
            colr = Fore.GREEN
            &#34;&#34;&#34;if logs==True:
    print (colr+&#34;[+] Vulnerable&#34;+Style.RESET_ALL)&#34;&#34;&#34;
            res[&#34;Vulnerable&#34;].append(x)
        else:
            colr = Fore.RED
            &#34;&#34;&#34;if logs==True:
    print (colr+&#34;[-] Not vulnerable&#34;+Style.RESET_ALL)&#34;&#34;&#34;
            res[&#34;Safe&#34;].append(x)
    return res</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.csrf.csrf_forms"><code class="name flex">
<span>def <span class="ident">csrf_forms</span></span>(<span>u, proxy=None, timeout=10, show_warnings=True, user_agent=None, cookie=None, replaceble_parameters={'phpvalue': (('.', ''),)}, file_extension='png', fill_empty=10, referer='http://www.evil.com', leave_empty=[], dont_send=[], mime_type=None, predefined_inputs={}, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def csrf_forms(
    u,
    proxy=None,
    timeout=10,
    show_warnings=True,
    user_agent=None,
    cookie=None,
    replaceble_parameters={&#34;phpvalue&#34;: ((&#34;.&#34;, &#34;&#34;),)},
    file_extension=&#34;png&#34;,
    fill_empty=10,
    referer=&#34;http://www.evil.com&#34;,
    leave_empty=[],
    dont_send=[],
    mime_type=None,
    predefined_inputs={},
    headers={}
):
    vu = []
    if not cookie or len(cookie.strip()) == 0:
        raise Exception(
            &#34;This attack requires authentication !! You need to set a Cookie&#34;
        )
    v = csrf_filter_tokens(
        u, proxy=proxy, timeout=timeout, user_agent=user_agent, cookie=cookie, headers=headers
    )[&#34;Vulnerable&#34;]
    if user_agent:
        h = {&#34;User-Agent&#34;: user_agent}
    else:
        h = {&#34;User-Agent&#34;: random.choice(ua)}
    h.update({&#34;cookie&#34;: cookie})
    h.update(
        {
            &#34;Referer&#34;: referer,
            &#34;Origin&#34;: referer.split(&#34;://&#34;)[0]
            + &#34;://&#34;
            + referer.split(&#34;://&#34;)[1].split(&#34;/&#34;)[0],
        }
    )
    h.update(headers)
    for x in v:
        x = form_filler(
            x,
            &#34;&#34;,
            &#34;&#34;,
            file_extension=file_extension,
            auto_fill=fill_empty,
            leave_empty=leave_empty,
            dont_send=dont_send,
            mime_type=mime_type,
            predefined_inputs=predefined_inputs,
        )
        d, f = setup_to_submit(x)
        for g in d:
            for y in replaceble_parameters:
                if x == y:
                    for z in replaceble_parameters[y]:
                        d[g] = d[g].replace(z[0], z[1])
        l = [d[y] for y in d]
        for j in f:
            l.append(f[j][0])
        if x[&#34;method&#34;] == &#34;get&#34;:
            r = requests.Session().get(
                x[&#34;action&#34;], params=d, proxies=proxy, timeout=timeout, headers=h,verify=False,
            )
        else:
            if &#34;application/json&#34; in x[&#34;enctype&#34;]:
                d = json.dumps(d)
            r = requests.Session().post(
                x[&#34;action&#34;], data=d, files=f, proxies=proxy, timeout=timeout, headers=h,verify=False,
            )
        if all(i in r.text for i in l):
            vu.append({&#39;form&#39;:x, &#39;status&#39;:&#34;Found all data&#34;})
        elif r.status_code == 200 and any(i in r.text for i in l):
            vu.append({&#39;form&#39;:x, &#39;status&#39;:&#34;Found some data&#34;})
            if show_warnings == True:
                print(
                    &#34;Warning: HTTP Status Code: 200 , but we didn&#39;t find some of our submitted data, so it&#39;s probably vulnerable but they are saved somewhere else..\nPlease check manually by visiting the form again&#34;
                )
        elif (
            r.status_code == 200
            and not any(i in r.text for i in l)
            and any(
                i in r.text.lower() for i in [&#34;unauthorized&#34;, &#34;invalid&#34;, &#34;unacceptable&#34;]
            )
        ):
            return False
        elif r.status_code == 200 and not any(i in r.text for i in l):
            if show_warnings == True:
                print(
                    &#34;Warning: HTTP Status Code: 200 , but we didn&#39;t find any of our submitted data, so it&#39;s probably vulnerable but they are saved somewhere else..\nPlease check manually by visiting the form again&#34;
                )
            vu.append({&#39;form&#39;:x, &#39;status&#39;:&#34;Found no data but Status Code: 200&#34;})
    return vu</code></pre>
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
<li><code><a title="bane.scanners.vulnerabilities.csrf.csrf" href="#bane.scanners.vulnerabilities.csrf.csrf">csrf</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.csrf.csrf_filter_tokens" href="#bane.scanners.vulnerabilities.csrf.csrf_filter_tokens">csrf_filter_tokens</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.csrf.csrf_forms" href="#bane.scanners.vulnerabilities.csrf.csrf_forms">csrf_forms</a></code></li>
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