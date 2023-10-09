<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1" />
<meta name="generator" content="pdoc 0.10.0" />
<title>bane.scanners.vulnerabilities.xss API documentation</title>
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
<h1 class="title">Module <code>bane.scanners.vulnerabilities.xss</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.scanners.vulnerabilities.utils import *


def jsfuck_encoder(text, parent=True, eval=True):
    return js_fuck().encode(text, eval, parent)


def find_xss_context(text, payload):
    try:
        a = re.search(
            &#34;&lt;(.*?)=?{}?(.*?)&gt;&#34;.format(re.escape(r&#34;{}&#34;.format(payload))), text
        ).group(0)
        b = a.replace(payload, &#34;&#34;)
        if len(re.findall(&#34;&lt;(.*?)&gt;&#34;, b)) != 1:
            return payload
        else:
            return a
    except:
        return payload


def html_decoder(payload, html_encode_level=0):
    for x in range(html_encode_level):
        payload = HTMLParser.HTMLParser().unescape(payload)
    return payload


def html_encoder(text, random_level=1):
    if random_level == 1:
        d = &#34;&#34;
        for c in text:
            a = random.randint(0, 1)
            if a == 0:
                d += c
            else:
                d += &#34;&amp;#&#34; + str(ord(c))
        return d
    if random_level == 2:
        return &#34;&#34;.join(&#34;&amp;#%d&#34; % ord(c) for c in text)
    else:
        return text


def hexadecimal_encoder(text, random_level=1):
    &#34;&#34;&#34;
    only for js functions names
    &#34;&#34;&#34;
    if random_level == 1:
        d = &#34;&#34;
        for c in text:
            a = random.randint(0, 1)
            if a == 0:
                d += c
            else:
                d += hex(ord(c)).replace(&#34;0x&#34;, r&#34;\u00&#34;)
        return d
    if random_level == 2:
        return &#34;&#34;.join(hex(ord(c)).replace(&#34;0x&#34;, r&#34;\u00&#34;) for c in text)
    else:
        return unicode(text)


def html_hexadecimal_encoder(text, random_level=1):
    if random_level == 1:
        d = &#34;&#34;
        for c in text:
            a = random.randint(0, 1)
            if a == 0:
                d += c
            else:
                d += hex(ord(c)).replace(&#34;0x&#34;, &#34;&amp;#x&#34;)
        return d
    if random_level == 2:
        return &#34;&#34;.join(hex(ord(c)).replace(&#34;0x&#34;, &#34;&amp;#x&#34;) for c in text)
    else:
        return unicode(text)




def xss_submit(
    parsed,
    payload,
    replaceble_parameters,
    debug=False,
    enctype=&#34;application/x-www-form-urlencoded&#34;,
):
    &#34;&#34;&#34;&#34;&#34;&#34;
    p_o_c=parsed[0].copy()
    d, fi = setup_to_submit(parsed[0])
    for x in d:
        for y in replaceble_parameters:
            if x == y:
                for z in replaceble_parameters[y]:
                    d[x] = d[x].replace(z[0], z[1])
    if not fi:
        parsed[1].update(
            {
                &#34;Content-Type&#34;: enctype,
                &#34;Referer&#34;: parsed[0][&#34;action&#34;],
                &#34;Origin&#34;: parsed[0][&#34;action&#34;].split(&#34;://&#34;)[0]
                + &#34;://&#34;
                + parsed[0][&#34;action&#34;].split(&#34;://&#34;)[1].split(&#34;/&#34;)[0],
            }
        )
    else:
        parsed[1].update(
            {
                &#34;Referer&#34;: parsed[0][&#34;action&#34;],
                &#34;Origin&#34;: parsed[0][&#34;action&#34;].split(&#34;://&#34;)[0]
                + &#34;://&#34;
                + parsed[0][&#34;action&#34;].split(&#34;://&#34;)[1].split(&#34;/&#34;)[0],
            }
        )
    if debug == True:
        for x in d:
            print(&#34;{}{} : {}{}&#34;.format(Fore.MAGENTA, x, Fore.WHITE, d[x]))
        for x in fi:
            print(&#34;{}{} : {}{}&#34;.format(Fore.MAGENTA, x, Fore.WHITE, fi[x]))
    if &#34;application/json&#34; in enctype:
        d = json.dumps(d)
    c=&#39;&#39;
    if parsed[0][&#34;method&#34;] == &#34;get&#34;:
        try:
            c = requests.Session().get(
                parsed[0][&#34;action&#34;],
                params=d,
                headers=parsed[1],
                proxies=parsed[2],
                timeout=parsed[3],
                verify=False,
            ).text
            if payload in c:
                return (True, {&#34;reflection&#34;:find_xss_context(c, payload),&#34;p_o_c&#34;:p_o_c},any(s in c for s in sql_errors),any(s in c for s in xml_parser_errors),any(s in c for s in fetch_url_errors),any(s in c for s in open_file_errors),p_o_c)
        except Exception as e:
            pass
    else:
        try:
            c = requests.Session().post(
                parsed[0][&#34;action&#34;],
                data=d,
                files=fi,
                headers=parsed[1],
                proxies=parsed[2],
                timeout=parsed[3],
                verify=False,
            ).text
            if payload in c:
                return (True, {&#34;reflection&#34;:find_xss_context(c, payload),&#34;p_o_c&#34;:p_o_c},any(s in c for s in sql_errors),any(s in c for s in xml_parser_errors),any(s in c for s in fetch_url_errors),any(s in c for s in open_file_errors),p_o_c)
        except Exception as e:
            pass
    return (False, &#34;&#34;,any(s in c for s in sql_errors),any(s in c for s in xml_parser_errors),any(s in c for s in fetch_url_errors),any(s in c for s in open_file_errors),p_o_c)



def xss_forms(
    u,
    payload=None,
    unicode_random_level=0,
    number=(1, 9),
    js_function=&#34;alert&#34;,
    email_extension=&#39;@gmail.com&#39;,
    phone_pattern=&#39;XXX-XXX-XXXX&#39;,
    dont_change={},
    predefined_inputs={},
    replaceble_parameters={&#34;phpvalue&#34;: ((&#34;.&#34;, &#34;&#34;),)},
    file_extension=&#34;png&#34;,
    context_breaker=&#39;&#34;&gt;&#39;,
    save_to_file=None,
    logs=True,
    fill_empty=10,
    leave_empty=[],
    dont_send=[&#34;btnClear&#34;],
    proxy=None,
    proxies=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    debug=False,
    mime_type=None,
    headers={}
):
    &#34;&#34;&#34;
    this function is for xss test with both POST and GET requests . it extracts the input fields names using the &#34;inputs&#34; function then test each input using POST and GET methods.

    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;bane.xss_forms(&#39;http://www.example.com/&#34;)

    &gt;&gt;&gt;bane.xss_forms(&#39;http://www.example.com/&#39;,payload=&#34;&lt;script&gt;alert(123);&lt;/script&gt;&#34;)

    &#34;&#34;&#34;
    target_page = u
    if proxy:
        proxy = proxy
    if proxies:
        proxy = random.choice(proxies)
    dic = []
    pre_apyload = True
    if payload:
        xp_f = payload
        pre_apyload = False
    else:
        xp_f = &#39;&lt;DeTAIlS/OpeN/OntOGglE = &#34;{} `v`&#34;&#39;
    if context_breaker:
        xp_f = context_breaker + xp_f
    if logs == True:
        print(Fore.WHITE + &#34;[~]Getting forms...&#34; + Style.RESET_ALL)
    hu = True
    fom = forms_parser(
        u, proxy=proxy, timeout=timeout, cookie=cookie, user_agent=user_agent,include_links=True,headers=headers
    )
    if len(fom) == 0:
        if logs == True:
            print(Fore.RED + &#34;[-]No forms were found!!!&#34; + Style.RESET_ALL)
        hu = False
    if hu == True:
        form_index = -1
        for l1 in fom:
            form_index += 1
            if pre_apyload == True:
                xp = xp_f.format(
                    hexadecimal_encoder(js_function, random_level=unicode_random_level)
                )
            else:
                xp = xp_f
            lst = {}
            vul = []
            sec = []
            sql_e=[]
            xml_e=[]
            p_t_e=[]
            ssrf_e=[]
            p_t_erros=[]
            ssrf_errors=[]
            hu = True
            u = l1[&#34;action&#34;]
            if logs == True:
                print(
                    Fore.BLUE
                    + &#34;Form: &#34;
                    + Fore.WHITE
                    + str(form_index)
                    + Fore.BLUE
                    + &#34;\nAction: &#34;
                    + Fore.WHITE
                    + u
                    + Fore.BLUE
                    + &#34;\nMethod: &#34;
                    + Fore.WHITE
                    + l1[&#34;method&#34;]
                    + Fore.BLUE
                    + &#34;\nPayload: &#34;
                    + Fore.WHITE
                    + xp
                    + Style.RESET_ALL
                )
            &#34;&#34;&#34;if len(inputs(u,proxy=proxy,timeout=timeout,value=True,cookie=cookie,user_agent=user_agent))==0:
     hu=False
     if logs==True:
      print(Fore.YELLOW+&#34;[-]No parameters found on that page !! Moving on..&#34;+Style.RESET_ALL)&#34;&#34;&#34;
            if True:
                extr = []
                l = []
                for x in l1[&#34;inputs&#34;]:
                    if (
                        x[&#34;name&#34;].strip() not in leave_empty
                        and x[&#34;name&#34;].strip() not in dont_send
                    ):
                        if (
                            x[&#34;type&#34;]
                            in [
                                &#34;hidden&#34;,
                                &#34;file&#34;,
                                &#34;text&#34;,
                                &#34;textarea&#34;,
                                &#34;email&#34;,
                                &#34;tel&#34;,
                                &#34;search&#34;,
                                &#34;url&#34;,
                                &#34;password&#34;,
                                &#34;number&#34;,
                                &#34;select&#34;,
                                &#34;radio&#34;,
                                &#34;checkbox&#34;,
                                &#34;color&#34;
                            ]
                            and x[&#34;name&#34;] not in dont_change
                        ):  # any input type that accept direct input from keyboard
                            i = x[&#34;name&#34;]
                            parsed_form = set_up_injection(
                                target_page,
                                form_index,
                                i,
                                xp,
                                cookie,
                                setup_ua(user_agent),
                                setup_proxy(proxy, proxies),
                                timeout,
                                fill_empty,
                                file_extension=file_extension,
                                email_extension=email_extension,
                                phone_pattern=phone_pattern,
                                dont_change=dont_change,
                                number=number,
                                leave_empty=leave_empty,
                                dont_send=dont_send,
                                mime_type=mime_type,
                                predefined_inputs=predefined_inputs,
                                headers=headers
                            )
                            xss_res = xss_submit(
                                parsed_form,
                                xp,
                                replaceble_parameters,
                                debug=debug,
                                enctype=l1[&#34;enctype&#34;],
                            )
                            if xss_res[0] == True:
                                x = &#34;parameter: &#39;&#34; + i + &#34;&#39; =&gt; [+]Payload was found&#34;
                                vul.append({&#39;parameter&#39;:i, &#39;context&#39;: xss_res[1]})
                                colr = Fore.GREEN
                            else:
                                x = &#34;parameter: &#39;&#34; + i + &#34;&#39; =&gt; [-]Payload was not found&#34;
                                #sec.append(i)
                                colr = Fore.RED
                            if xss_res[2] == True:
                                x+=Fore.YELLOW+&#34;\n[i] SQL Error detected&#34;
                                sql_e.append({&#39;parameter&#39;:i, &#39;p_o_c&#39;: xss_res[-1]})
                            if xss_res[3] == True:
                                x+=Fore.YELLOW+&#34;\n[i] XML parsing Error detected (potential XML injection)&#34;
                                xml_e.append({&#39;parameter&#39;:i, &#39;p_o_c&#39;: xss_res[-1]})
                            if xss_res[4] == True:
                                x+=Fore.YELLOW+&#34;\n[i] Fetching URL Error detected (potential SSRF)&#34;
                                ssrf_e.append({&#39;parameter&#39;:i, &#39;p_o_c&#39;: xss_res[-1]})
                            if xss_res[5] == True:
                                x+=Fore.YELLOW+&#34;\n[i] Reading file Error detected (potential path traversal)&#34;
                                p_t_e.append({&#39;parameter&#39;:i, &#39;p_o_c&#39;: xss_res[-1]})
                            if logs == True:
                                print(colr + x + Style.RESET_ALL)
            dic.append(
                {
                    &#34;form&#34;: u,
                    &#34;method&#34;: l1[&#34;method&#34;],
                    &#34;vulnerable&#34;: vul,
                    #&#34;safe&#34;: sec,
                    &#34;sql_errors&#34;:sql_e,
                    &#34;xml_parsing_errors&#34;:xml_e,
                    &#34;fetching_url_errors&#34;:ssrf_e,
                    &#34;reading_file_errors&#34;:p_t_e
                }
            )
        if save_to_file:
            with open(save_to_file.split(&#34;.&#34;)[0] + &#34;.json&#34;, &#34;w&#34;) as outfile:
                json.dump(
                    {&#34;Payload&#34;: xp, &#34;Page&#34;: target_page, &#34;Output&#34;: dic},
                    outfile,
                    indent=4,
                )
            outfile.close()
        return {&#34;payload&#34;: xp, &#34;page&#34;: target_page, &#34;result&#34;: dic}




def xss(
    u,
    max_pages=5,
    pages=[],
    payload=None,
    email_extension=&#39;@gmail.com&#39;,
    phone_pattern=&#39;XXX-XXX-XXXX&#39;,
    unicode_random_level=0,
    number=(1, 9),
    js_function=&#34;alert&#34;,
    dont_change={},
    predefined_inputs={},
    replaceble_parameters={&#34;phpvalue&#34;: ((&#34;.&#34;, &#34;&#34;),)},
    file_extension=&#34;png&#34;,
    context_breaker=&#39;&#34;&gt;&#39;,
    save_to_file=None,
    logs=True,
    fill_empty=10,
    leave_empty=[],
    dont_send=[&#34;btnClear&#34;],
    proxy=None,
    proxies=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    debug=False,
    mime_type=None,
    headers={}
):
    l=[]
    if pages==[]:
        pages=spider_url(u,cookie=cookie,max_pages=max_pages,timeout=timeout,user_agent=user_agent,proxy=proxy,headers=headers)
    for x in pages:
        if logs==True:
            print(&#39;\n\nPage: {}\n&#39;.format(x))
        l.append(xss_forms(x,
                           payload=None,
                            unicode_random_level=unicode_random_level,
                            number=number,
                            js_function=js_function,
                            dont_change=dont_change,
                            email_extension=email_extension,
                            phone_pattern=phone_pattern,
                            predefined_inputs=predefined_inputs,
                            replaceble_parameters=replaceble_parameters,
                            file_extension=file_extension,
                            context_breaker=context_breaker,
                            save_to_file=save_to_file,
                            logs=logs,
                            fill_empty=fill_empty,
                            leave_empty=leave_empty,
                            dont_send=dont_send,
                            proxy=proxy,
                            proxies=proxies,
                            timeout=timeout,
                            user_agent=user_agent,
                            cookie=cookie,
                            debug=debug,
                            mime_type=mime_type,
                            headers=headers))
    f=[]
    for x in l:
        if x !=None:
            n=x.copy()
            n[&#39;result&#39;]=[]
            for i in x[&#39;result&#39;]:
                if len(i[&#39;vulnerable&#39;]) &gt; 0 or len(i[&#39;sql_errors&#39;]) &gt; 0 or len(i[&#39;xml_parsing_errors&#39;])&gt;0 or len(i[&#39;fetching_url_errors&#39;])&gt;0 or len(i[&#39;reading_file_errors&#39;]) &gt; 0:
                    n[&#39;result&#39;].append(i)
            if n[&#39;result&#39;]!=[]:
                f.append(n)
    return f</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="bane.scanners.vulnerabilities.xss.find_xss_context"><code class="name flex">
<span>def <span class="ident">find_xss_context</span></span>(<span>text, payload)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def find_xss_context(text, payload):
    try:
        a = re.search(
            &#34;&lt;(.*?)=?{}?(.*?)&gt;&#34;.format(re.escape(r&#34;{}&#34;.format(payload))), text
        ).group(0)
        b = a.replace(payload, &#34;&#34;)
        if len(re.findall(&#34;&lt;(.*?)&gt;&#34;, b)) != 1:
            return payload
        else:
            return a
    except:
        return payload</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.xss.hexadecimal_encoder"><code class="name flex">
<span>def <span class="ident">hexadecimal_encoder</span></span>(<span>text, random_level=1)</span>
</code></dt>
<dd>
<div class="desc"><p>only for js functions names</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def hexadecimal_encoder(text, random_level=1):
    &#34;&#34;&#34;
    only for js functions names
    &#34;&#34;&#34;
    if random_level == 1:
        d = &#34;&#34;
        for c in text:
            a = random.randint(0, 1)
            if a == 0:
                d += c
            else:
                d += hex(ord(c)).replace(&#34;0x&#34;, r&#34;\u00&#34;)
        return d
    if random_level == 2:
        return &#34;&#34;.join(hex(ord(c)).replace(&#34;0x&#34;, r&#34;\u00&#34;) for c in text)
    else:
        return unicode(text)</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.xss.html_decoder"><code class="name flex">
<span>def <span class="ident">html_decoder</span></span>(<span>payload, html_encode_level=0)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def html_decoder(payload, html_encode_level=0):
    for x in range(html_encode_level):
        payload = HTMLParser.HTMLParser().unescape(payload)
    return payload</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.xss.html_encoder"><code class="name flex">
<span>def <span class="ident">html_encoder</span></span>(<span>text, random_level=1)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def html_encoder(text, random_level=1):
    if random_level == 1:
        d = &#34;&#34;
        for c in text:
            a = random.randint(0, 1)
            if a == 0:
                d += c
            else:
                d += &#34;&amp;#&#34; + str(ord(c))
        return d
    if random_level == 2:
        return &#34;&#34;.join(&#34;&amp;#%d&#34; % ord(c) for c in text)
    else:
        return text</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.xss.html_hexadecimal_encoder"><code class="name flex">
<span>def <span class="ident">html_hexadecimal_encoder</span></span>(<span>text, random_level=1)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def html_hexadecimal_encoder(text, random_level=1):
    if random_level == 1:
        d = &#34;&#34;
        for c in text:
            a = random.randint(0, 1)
            if a == 0:
                d += c
            else:
                d += hex(ord(c)).replace(&#34;0x&#34;, &#34;&amp;#x&#34;)
        return d
    if random_level == 2:
        return &#34;&#34;.join(hex(ord(c)).replace(&#34;0x&#34;, &#34;&amp;#x&#34;) for c in text)
    else:
        return unicode(text)</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.xss.jsfuck_encoder"><code class="name flex">
<span>def <span class="ident">jsfuck_encoder</span></span>(<span>text, parent=True, eval=True)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def jsfuck_encoder(text, parent=True, eval=True):
    return js_fuck().encode(text, eval, parent)</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.xss.xss"><code class="name flex">
<span>def <span class="ident">xss</span></span>(<span>u, max_pages=5, pages=[], payload=None, email_extension='@gmail.com', phone_pattern='XXX-XXX-XXXX', unicode_random_level=0, number=(1, 9), js_function='alert', dont_change={}, predefined_inputs={}, replaceble_parameters={'phpvalue': (('.', ''),)}, file_extension='png', context_breaker=&#x27;&quot;&gt;&#x27;, save_to_file=None, logs=True, fill_empty=10, leave_empty=[], dont_send=['btnClear'], proxy=None, proxies=None, timeout=10, user_agent=None, cookie=None, debug=False, mime_type=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def xss(
    u,
    max_pages=5,
    pages=[],
    payload=None,
    email_extension=&#39;@gmail.com&#39;,
    phone_pattern=&#39;XXX-XXX-XXXX&#39;,
    unicode_random_level=0,
    number=(1, 9),
    js_function=&#34;alert&#34;,
    dont_change={},
    predefined_inputs={},
    replaceble_parameters={&#34;phpvalue&#34;: ((&#34;.&#34;, &#34;&#34;),)},
    file_extension=&#34;png&#34;,
    context_breaker=&#39;&#34;&gt;&#39;,
    save_to_file=None,
    logs=True,
    fill_empty=10,
    leave_empty=[],
    dont_send=[&#34;btnClear&#34;],
    proxy=None,
    proxies=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    debug=False,
    mime_type=None,
    headers={}
):
    l=[]
    if pages==[]:
        pages=spider_url(u,cookie=cookie,max_pages=max_pages,timeout=timeout,user_agent=user_agent,proxy=proxy,headers=headers)
    for x in pages:
        if logs==True:
            print(&#39;\n\nPage: {}\n&#39;.format(x))
        l.append(xss_forms(x,
                           payload=None,
                            unicode_random_level=unicode_random_level,
                            number=number,
                            js_function=js_function,
                            dont_change=dont_change,
                            email_extension=email_extension,
                            phone_pattern=phone_pattern,
                            predefined_inputs=predefined_inputs,
                            replaceble_parameters=replaceble_parameters,
                            file_extension=file_extension,
                            context_breaker=context_breaker,
                            save_to_file=save_to_file,
                            logs=logs,
                            fill_empty=fill_empty,
                            leave_empty=leave_empty,
                            dont_send=dont_send,
                            proxy=proxy,
                            proxies=proxies,
                            timeout=timeout,
                            user_agent=user_agent,
                            cookie=cookie,
                            debug=debug,
                            mime_type=mime_type,
                            headers=headers))
    f=[]
    for x in l:
        if x !=None:
            n=x.copy()
            n[&#39;result&#39;]=[]
            for i in x[&#39;result&#39;]:
                if len(i[&#39;vulnerable&#39;]) &gt; 0 or len(i[&#39;sql_errors&#39;]) &gt; 0 or len(i[&#39;xml_parsing_errors&#39;])&gt;0 or len(i[&#39;fetching_url_errors&#39;])&gt;0 or len(i[&#39;reading_file_errors&#39;]) &gt; 0:
                    n[&#39;result&#39;].append(i)
            if n[&#39;result&#39;]!=[]:
                f.append(n)
    return f</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.xss.xss_forms"><code class="name flex">
<span>def <span class="ident">xss_forms</span></span>(<span>u, payload=None, unicode_random_level=0, number=(1, 9), js_function='alert', email_extension='@gmail.com', phone_pattern='XXX-XXX-XXXX', dont_change={}, predefined_inputs={}, replaceble_parameters={'phpvalue': (('.', ''),)}, file_extension='png', context_breaker=&#x27;&quot;&gt;&#x27;, save_to_file=None, logs=True, fill_empty=10, leave_empty=[], dont_send=['btnClear'], proxy=None, proxies=None, timeout=10, user_agent=None, cookie=None, debug=False, mime_type=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"><p>this function is for xss test with both POST and GET requests . it extracts the input fields names using the "inputs" function then test each input using POST and GET methods.</p>
<p>usage:</p>
<blockquote>
<blockquote>
<blockquote>
<p>import bane
bane.xss_forms('http://www.example.com/")</p>
<p>bane.xss_forms('http://www.example.com/',payload="<script>alert(123);</script>")</p>
</blockquote>
</blockquote>
</blockquote></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def xss_forms(
    u,
    payload=None,
    unicode_random_level=0,
    number=(1, 9),
    js_function=&#34;alert&#34;,
    email_extension=&#39;@gmail.com&#39;,
    phone_pattern=&#39;XXX-XXX-XXXX&#39;,
    dont_change={},
    predefined_inputs={},
    replaceble_parameters={&#34;phpvalue&#34;: ((&#34;.&#34;, &#34;&#34;),)},
    file_extension=&#34;png&#34;,
    context_breaker=&#39;&#34;&gt;&#39;,
    save_to_file=None,
    logs=True,
    fill_empty=10,
    leave_empty=[],
    dont_send=[&#34;btnClear&#34;],
    proxy=None,
    proxies=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    debug=False,
    mime_type=None,
    headers={}
):
    &#34;&#34;&#34;
    this function is for xss test with both POST and GET requests . it extracts the input fields names using the &#34;inputs&#34; function then test each input using POST and GET methods.

    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;bane.xss_forms(&#39;http://www.example.com/&#34;)

    &gt;&gt;&gt;bane.xss_forms(&#39;http://www.example.com/&#39;,payload=&#34;&lt;script&gt;alert(123);&lt;/script&gt;&#34;)

    &#34;&#34;&#34;
    target_page = u
    if proxy:
        proxy = proxy
    if proxies:
        proxy = random.choice(proxies)
    dic = []
    pre_apyload = True
    if payload:
        xp_f = payload
        pre_apyload = False
    else:
        xp_f = &#39;&lt;DeTAIlS/OpeN/OntOGglE = &#34;{} `v`&#34;&#39;
    if context_breaker:
        xp_f = context_breaker + xp_f
    if logs == True:
        print(Fore.WHITE + &#34;[~]Getting forms...&#34; + Style.RESET_ALL)
    hu = True
    fom = forms_parser(
        u, proxy=proxy, timeout=timeout, cookie=cookie, user_agent=user_agent,include_links=True,headers=headers
    )
    if len(fom) == 0:
        if logs == True:
            print(Fore.RED + &#34;[-]No forms were found!!!&#34; + Style.RESET_ALL)
        hu = False
    if hu == True:
        form_index = -1
        for l1 in fom:
            form_index += 1
            if pre_apyload == True:
                xp = xp_f.format(
                    hexadecimal_encoder(js_function, random_level=unicode_random_level)
                )
            else:
                xp = xp_f
            lst = {}
            vul = []
            sec = []
            sql_e=[]
            xml_e=[]
            p_t_e=[]
            ssrf_e=[]
            p_t_erros=[]
            ssrf_errors=[]
            hu = True
            u = l1[&#34;action&#34;]
            if logs == True:
                print(
                    Fore.BLUE
                    + &#34;Form: &#34;
                    + Fore.WHITE
                    + str(form_index)
                    + Fore.BLUE
                    + &#34;\nAction: &#34;
                    + Fore.WHITE
                    + u
                    + Fore.BLUE
                    + &#34;\nMethod: &#34;
                    + Fore.WHITE
                    + l1[&#34;method&#34;]
                    + Fore.BLUE
                    + &#34;\nPayload: &#34;
                    + Fore.WHITE
                    + xp
                    + Style.RESET_ALL
                )
            &#34;&#34;&#34;if len(inputs(u,proxy=proxy,timeout=timeout,value=True,cookie=cookie,user_agent=user_agent))==0:
     hu=False
     if logs==True:
      print(Fore.YELLOW+&#34;[-]No parameters found on that page !! Moving on..&#34;+Style.RESET_ALL)&#34;&#34;&#34;
            if True:
                extr = []
                l = []
                for x in l1[&#34;inputs&#34;]:
                    if (
                        x[&#34;name&#34;].strip() not in leave_empty
                        and x[&#34;name&#34;].strip() not in dont_send
                    ):
                        if (
                            x[&#34;type&#34;]
                            in [
                                &#34;hidden&#34;,
                                &#34;file&#34;,
                                &#34;text&#34;,
                                &#34;textarea&#34;,
                                &#34;email&#34;,
                                &#34;tel&#34;,
                                &#34;search&#34;,
                                &#34;url&#34;,
                                &#34;password&#34;,
                                &#34;number&#34;,
                                &#34;select&#34;,
                                &#34;radio&#34;,
                                &#34;checkbox&#34;,
                                &#34;color&#34;
                            ]
                            and x[&#34;name&#34;] not in dont_change
                        ):  # any input type that accept direct input from keyboard
                            i = x[&#34;name&#34;]
                            parsed_form = set_up_injection(
                                target_page,
                                form_index,
                                i,
                                xp,
                                cookie,
                                setup_ua(user_agent),
                                setup_proxy(proxy, proxies),
                                timeout,
                                fill_empty,
                                file_extension=file_extension,
                                email_extension=email_extension,
                                phone_pattern=phone_pattern,
                                dont_change=dont_change,
                                number=number,
                                leave_empty=leave_empty,
                                dont_send=dont_send,
                                mime_type=mime_type,
                                predefined_inputs=predefined_inputs,
                                headers=headers
                            )
                            xss_res = xss_submit(
                                parsed_form,
                                xp,
                                replaceble_parameters,
                                debug=debug,
                                enctype=l1[&#34;enctype&#34;],
                            )
                            if xss_res[0] == True:
                                x = &#34;parameter: &#39;&#34; + i + &#34;&#39; =&gt; [+]Payload was found&#34;
                                vul.append({&#39;parameter&#39;:i, &#39;context&#39;: xss_res[1]})
                                colr = Fore.GREEN
                            else:
                                x = &#34;parameter: &#39;&#34; + i + &#34;&#39; =&gt; [-]Payload was not found&#34;
                                #sec.append(i)
                                colr = Fore.RED
                            if xss_res[2] == True:
                                x+=Fore.YELLOW+&#34;\n[i] SQL Error detected&#34;
                                sql_e.append({&#39;parameter&#39;:i, &#39;p_o_c&#39;: xss_res[-1]})
                            if xss_res[3] == True:
                                x+=Fore.YELLOW+&#34;\n[i] XML parsing Error detected (potential XML injection)&#34;
                                xml_e.append({&#39;parameter&#39;:i, &#39;p_o_c&#39;: xss_res[-1]})
                            if xss_res[4] == True:
                                x+=Fore.YELLOW+&#34;\n[i] Fetching URL Error detected (potential SSRF)&#34;
                                ssrf_e.append({&#39;parameter&#39;:i, &#39;p_o_c&#39;: xss_res[-1]})
                            if xss_res[5] == True:
                                x+=Fore.YELLOW+&#34;\n[i] Reading file Error detected (potential path traversal)&#34;
                                p_t_e.append({&#39;parameter&#39;:i, &#39;p_o_c&#39;: xss_res[-1]})
                            if logs == True:
                                print(colr + x + Style.RESET_ALL)
            dic.append(
                {
                    &#34;form&#34;: u,
                    &#34;method&#34;: l1[&#34;method&#34;],
                    &#34;vulnerable&#34;: vul,
                    #&#34;safe&#34;: sec,
                    &#34;sql_errors&#34;:sql_e,
                    &#34;xml_parsing_errors&#34;:xml_e,
                    &#34;fetching_url_errors&#34;:ssrf_e,
                    &#34;reading_file_errors&#34;:p_t_e
                }
            )
        if save_to_file:
            with open(save_to_file.split(&#34;.&#34;)[0] + &#34;.json&#34;, &#34;w&#34;) as outfile:
                json.dump(
                    {&#34;Payload&#34;: xp, &#34;Page&#34;: target_page, &#34;Output&#34;: dic},
                    outfile,
                    indent=4,
                )
            outfile.close()
        return {&#34;payload&#34;: xp, &#34;page&#34;: target_page, &#34;result&#34;: dic}</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.xss.xss_submit"><code class="name flex">
<span>def <span class="ident">xss_submit</span></span>(<span>parsed, payload, replaceble_parameters, debug=False, enctype='application/x-www-form-urlencoded')</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def xss_submit(
    parsed,
    payload,
    replaceble_parameters,
    debug=False,
    enctype=&#34;application/x-www-form-urlencoded&#34;,
):
    &#34;&#34;&#34;&#34;&#34;&#34;
    p_o_c=parsed[0].copy()
    d, fi = setup_to_submit(parsed[0])
    for x in d:
        for y in replaceble_parameters:
            if x == y:
                for z in replaceble_parameters[y]:
                    d[x] = d[x].replace(z[0], z[1])
    if not fi:
        parsed[1].update(
            {
                &#34;Content-Type&#34;: enctype,
                &#34;Referer&#34;: parsed[0][&#34;action&#34;],
                &#34;Origin&#34;: parsed[0][&#34;action&#34;].split(&#34;://&#34;)[0]
                + &#34;://&#34;
                + parsed[0][&#34;action&#34;].split(&#34;://&#34;)[1].split(&#34;/&#34;)[0],
            }
        )
    else:
        parsed[1].update(
            {
                &#34;Referer&#34;: parsed[0][&#34;action&#34;],
                &#34;Origin&#34;: parsed[0][&#34;action&#34;].split(&#34;://&#34;)[0]
                + &#34;://&#34;
                + parsed[0][&#34;action&#34;].split(&#34;://&#34;)[1].split(&#34;/&#34;)[0],
            }
        )
    if debug == True:
        for x in d:
            print(&#34;{}{} : {}{}&#34;.format(Fore.MAGENTA, x, Fore.WHITE, d[x]))
        for x in fi:
            print(&#34;{}{} : {}{}&#34;.format(Fore.MAGENTA, x, Fore.WHITE, fi[x]))
    if &#34;application/json&#34; in enctype:
        d = json.dumps(d)
    c=&#39;&#39;
    if parsed[0][&#34;method&#34;] == &#34;get&#34;:
        try:
            c = requests.Session().get(
                parsed[0][&#34;action&#34;],
                params=d,
                headers=parsed[1],
                proxies=parsed[2],
                timeout=parsed[3],
                verify=False,
            ).text
            if payload in c:
                return (True, {&#34;reflection&#34;:find_xss_context(c, payload),&#34;p_o_c&#34;:p_o_c},any(s in c for s in sql_errors),any(s in c for s in xml_parser_errors),any(s in c for s in fetch_url_errors),any(s in c for s in open_file_errors),p_o_c)
        except Exception as e:
            pass
    else:
        try:
            c = requests.Session().post(
                parsed[0][&#34;action&#34;],
                data=d,
                files=fi,
                headers=parsed[1],
                proxies=parsed[2],
                timeout=parsed[3],
                verify=False,
            ).text
            if payload in c:
                return (True, {&#34;reflection&#34;:find_xss_context(c, payload),&#34;p_o_c&#34;:p_o_c},any(s in c for s in sql_errors),any(s in c for s in xml_parser_errors),any(s in c for s in fetch_url_errors),any(s in c for s in open_file_errors),p_o_c)
        except Exception as e:
            pass
    return (False, &#34;&#34;,any(s in c for s in sql_errors),any(s in c for s in xml_parser_errors),any(s in c for s in fetch_url_errors),any(s in c for s in open_file_errors),p_o_c)</code></pre>
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
<li><code><a title="bane.scanners.vulnerabilities.xss.find_xss_context" href="#bane.scanners.vulnerabilities.xss.find_xss_context">find_xss_context</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.xss.hexadecimal_encoder" href="#bane.scanners.vulnerabilities.xss.hexadecimal_encoder">hexadecimal_encoder</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.xss.html_decoder" href="#bane.scanners.vulnerabilities.xss.html_decoder">html_decoder</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.xss.html_encoder" href="#bane.scanners.vulnerabilities.xss.html_encoder">html_encoder</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.xss.html_hexadecimal_encoder" href="#bane.scanners.vulnerabilities.xss.html_hexadecimal_encoder">html_hexadecimal_encoder</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.xss.jsfuck_encoder" href="#bane.scanners.vulnerabilities.xss.jsfuck_encoder">jsfuck_encoder</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.xss.xss" href="#bane.scanners.vulnerabilities.xss.xss">xss</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.xss.xss_forms" href="#bane.scanners.vulnerabilities.xss.xss_forms">xss_forms</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.xss.xss_submit" href="#bane.scanners.vulnerabilities.xss.xss_submit">xss_submit</a></code></li>
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