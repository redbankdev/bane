<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1" />
<meta name="generator" content="pdoc 0.10.0" />
<title>bane.scanners.vulnerabilities API documentation</title>
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
<h1 class="title">Module <code>bane.scanners.vulnerabilities</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from .vulns import *</code></pre>
</details>
</section>
<section>
<h2 class="section-title" id="header-submodules">Sub-modules</h2>
<dl>
<dt><code class="name"><a title="bane.scanners.vulnerabilities.adb_exploit" href="adb_exploit.html">bane.scanners.vulnerabilities.adb_exploit</a></code></dt>
<dd>
<div class="desc"></div>
</dd>
<dt><code class="name"><a title="bane.scanners.vulnerabilities.backend_technologies" href="backend_technologies.html">bane.scanners.vulnerabilities.backend_technologies</a></code></dt>
<dd>
<div class="desc"></div>
</dd>
<dt><code class="name"><a title="bane.scanners.vulnerabilities.clickjacking" href="clickjacking.html">bane.scanners.vulnerabilities.clickjacking</a></code></dt>
<dd>
<div class="desc"></div>
</dd>
<dt><code class="name"><a title="bane.scanners.vulnerabilities.cors_misconfigurations" href="cors_misconfigurations.html">bane.scanners.vulnerabilities.cors_misconfigurations</a></code></dt>
<dd>
<div class="desc"></div>
</dd>
<dt><code class="name"><a title="bane.scanners.vulnerabilities.crlf_injection" href="crlf_injection.html">bane.scanners.vulnerabilities.crlf_injection</a></code></dt>
<dd>
<div class="desc"></div>
</dd>
<dt><code class="name"><a title="bane.scanners.vulnerabilities.csrf" href="csrf.html">bane.scanners.vulnerabilities.csrf</a></code></dt>
<dd>
<div class="desc"></div>
</dd>
<dt><code class="name"><a title="bane.scanners.vulnerabilities.exposed_env" href="exposed_env.html">bane.scanners.vulnerabilities.exposed_env</a></code></dt>
<dd>
<div class="desc"></div>
</dd>
<dt><code class="name"><a title="bane.scanners.vulnerabilities.exposed_git" href="exposed_git.html">bane.scanners.vulnerabilities.exposed_git</a></code></dt>
<dd>
<div class="desc"></div>
</dd>
<dt><code class="name"><a title="bane.scanners.vulnerabilities.exposed_telnet" href="exposed_telnet.html">bane.scanners.vulnerabilities.exposed_telnet</a></code></dt>
<dd>
<div class="desc"></div>
</dd>
<dt><code class="name"><a title="bane.scanners.vulnerabilities.file_upload" href="file_upload.html">bane.scanners.vulnerabilities.file_upload</a></code></dt>
<dd>
<div class="desc"></div>
</dd>
<dt><code class="name"><a title="bane.scanners.vulnerabilities.open_redirect" href="open_redirect.html">bane.scanners.vulnerabilities.open_redirect</a></code></dt>
<dd>
<div class="desc"></div>
</dd>
<dt><code class="name"><a title="bane.scanners.vulnerabilities.path_traversal" href="path_traversal.html">bane.scanners.vulnerabilities.path_traversal</a></code></dt>
<dd>
<div class="desc"></div>
</dd>
<dt><code class="name"><a title="bane.scanners.vulnerabilities.php_unit_exploit" href="php_unit_exploit.html">bane.scanners.vulnerabilities.php_unit_exploit</a></code></dt>
<dd>
<div class="desc"></div>
</dd>
<dt><code class="name"><a title="bane.scanners.vulnerabilities.rce" href="rce.html">bane.scanners.vulnerabilities.rce</a></code></dt>
<dd>
<div class="desc"></div>
</dd>
<dt><code class="name"><a title="bane.scanners.vulnerabilities.shodan_report" href="shodan_report.html">bane.scanners.vulnerabilities.shodan_report</a></code></dt>
<dd>
<div class="desc"></div>
</dd>
<dt><code class="name"><a title="bane.scanners.vulnerabilities.sniffable_links" href="sniffable_links.html">bane.scanners.vulnerabilities.sniffable_links</a></code></dt>
<dd>
<div class="desc"></div>
</dd>
<dt><code class="name"><a title="bane.scanners.vulnerabilities.springboot_actuator" href="springboot_actuator.html">bane.scanners.vulnerabilities.springboot_actuator</a></code></dt>
<dd>
<div class="desc"></div>
</dd>
<dt><code class="name"><a title="bane.scanners.vulnerabilities.ssrf" href="ssrf.html">bane.scanners.vulnerabilities.ssrf</a></code></dt>
<dd>
<div class="desc"></div>
</dd>
<dt><code class="name"><a title="bane.scanners.vulnerabilities.ssti" href="ssti.html">bane.scanners.vulnerabilities.ssti</a></code></dt>
<dd>
<div class="desc"></div>
</dd>
<dt><code class="name"><a title="bane.scanners.vulnerabilities.utils" href="utils.html">bane.scanners.vulnerabilities.utils</a></code></dt>
<dd>
<div class="desc"></div>
</dd>
<dt><code class="name"><a title="bane.scanners.vulnerabilities.vulner_search" href="vulner_search.html">bane.scanners.vulnerabilities.vulner_search</a></code></dt>
<dd>
<div class="desc"></div>
</dd>
<dt><code class="name"><a title="bane.scanners.vulnerabilities.vulns" href="vulns.html">bane.scanners.vulnerabilities.vulns</a></code></dt>
<dd>
<div class="desc"></div>
</dd>
<dt><code class="name"><a title="bane.scanners.vulnerabilities.xss" href="xss.html">bane.scanners.vulnerabilities.xss</a></code></dt>
<dd>
<div class="desc"></div>
</dd>
</dl>
</section>
<section>
</section>
<section>
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
<li><code><a title="bane.scanners" href="../index.html">bane.scanners</a></code></li>
</ul>
</li>
<li><h3><a href="#header-submodules">Sub-modules</a></h3>
<ul>
<li><code><a title="bane.scanners.vulnerabilities.adb_exploit" href="adb_exploit.html">bane.scanners.vulnerabilities.adb_exploit</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.backend_technologies" href="backend_technologies.html">bane.scanners.vulnerabilities.backend_technologies</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.clickjacking" href="clickjacking.html">bane.scanners.vulnerabilities.clickjacking</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.cors_misconfigurations" href="cors_misconfigurations.html">bane.scanners.vulnerabilities.cors_misconfigurations</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.crlf_injection" href="crlf_injection.html">bane.scanners.vulnerabilities.crlf_injection</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.csrf" href="csrf.html">bane.scanners.vulnerabilities.csrf</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.exposed_env" href="exposed_env.html">bane.scanners.vulnerabilities.exposed_env</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.exposed_git" href="exposed_git.html">bane.scanners.vulnerabilities.exposed_git</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.exposed_telnet" href="exposed_telnet.html">bane.scanners.vulnerabilities.exposed_telnet</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.file_upload" href="file_upload.html">bane.scanners.vulnerabilities.file_upload</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.open_redirect" href="open_redirect.html">bane.scanners.vulnerabilities.open_redirect</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.path_traversal" href="path_traversal.html">bane.scanners.vulnerabilities.path_traversal</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.php_unit_exploit" href="php_unit_exploit.html">bane.scanners.vulnerabilities.php_unit_exploit</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.rce" href="rce.html">bane.scanners.vulnerabilities.rce</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.shodan_report" href="shodan_report.html">bane.scanners.vulnerabilities.shodan_report</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.sniffable_links" href="sniffable_links.html">bane.scanners.vulnerabilities.sniffable_links</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.springboot_actuator" href="springboot_actuator.html">bane.scanners.vulnerabilities.springboot_actuator</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.ssrf" href="ssrf.html">bane.scanners.vulnerabilities.ssrf</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.ssti" href="ssti.html">bane.scanners.vulnerabilities.ssti</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.utils" href="utils.html">bane.scanners.vulnerabilities.utils</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.vulner_search" href="vulner_search.html">bane.scanners.vulnerabilities.vulner_search</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.vulns" href="vulns.html">bane.scanners.vulnerabilities.vulns</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.xss" href="xss.html">bane.scanners.vulnerabilities.xss</a></code></li>
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