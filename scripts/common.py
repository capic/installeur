# -*- coding: utf-8 -*-
__author__ = 'Vincent'

import utils
import os
from lib.menu import menu

def node_js():
    if utils.which('node') is None:
        print(u'_____ Installation de Nodejs _____')
        os.system('wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.26.1/install.sh | bash')
        execfile('~/.nvm/nvm.sh')
        os.system('nvm install latest')
    else:
        print(u'Nodejs est déjà installé')


def serveur():
    serveur_menu = menu.Menu()
    serveur_menu_selection = serveur_menu.show(
        {
            utils.SERVEUR_APACHE: u'Apache',
            utils.SERVEUR_LIGHTTPD: u'Lighttpd'
        }, u'Menu installation serveur')

    if serveur_menu_selection == utils.SERVEUR_APACHE:
        if utils.which('apache2') is None:
            print(u'_____ Installation d''apache _____')
            os.system('apt-get -y install apache2')
        else:
            print(u'Apache est déjà installé')
    elif serveur_menu_selection == utils.SERVEUR_LIGHTTPD:
        if utils.which('lighttpd') is None:
            print(u'_____ Installation de lighttpd _____')
            os.system('apt-get -y install lighttpd')

            f = open('/etc/php5/cgi/php.ini', 'r')
            file_data = f.read()
            f.close()

            new_data = file_data.replace(';cgi.fix_pathinfo=1', 'cgi.fix_pathinfo=1')

            f = open('/etc/php5/cgi/php.ini', 'w')
            f.write(new_data)
            f.close()

            os.system('lighttpd-enable-mod fastcgi')
            os.system('lighttpd-enable-mod fastcgi-php')
            os.system('/etc/init.d/lighttpd force-reload')
            os.system('/bin/echo \'## directory listing configuration## we disable the directory listing by default##$HTTP["url"] =~ "^/" {  dir-listing.activate = "disable"}\' | /usr/bin/tee /etc/lighttpd/conf-available/20-disable-listing.conf')
            os.system('/usr/sbin/lighty-enable-mod disable-listing')
            os.system('/etc/init.d/lighttpd force-reload')

            f = open('/etc/lighttpd/lighttpd.conf', 'r')
            file_data = f.read()
            f.close()

            new_data = file_data.replace('#       "mod_rewrite"', '        "mod_rewrite"')
            new_data = new_data + '\r\n server.error-handler-404 = "/index.php?error=404"'

            f = open('/etc/lighttpd/lighttpd.conf', 'w')
            f.write(new_data)
            f.close()

            os.system('/etc/init.d/lighttpd force-reload')
        else:
            print(u'Lighttpd est déjà installé')

    return serveur_menu_selection


def mysql(serveur):
    if utils.which('mysql') is None:
        print(u'_____ Installation de mysql _____')
        os.system('apt-get -y install mysql-server php5-mysql')

        if serveur == utils.SERVEUR_APACHE:
            os.system('apt-get -y install libapache2-mod-auth-mysql')

        os.system('mysql_install_db')
        os.system('/usr/bin/mysql_secure_installation')
    else:
        print(u'Mysql déjà installé')