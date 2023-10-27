from bane.scanners.vulnerabilities.utils import *

def exposed_telnet(u, p=23, timeout=5,**kwargs):
    try:
        t = xtelnet.session()
        t.connect(u, p=p, timeout=timeout,**kwargs)
        t.destroy()
        return True
    except:
        pass
    return False

