# -*- coding: utf-8 -*-
__author__ = 'Vincent'

from lib.menu import menu
import plow_solution
import utils


def chargement_config():
    config = {}
    execfile("../config.cfg", config)

    if 'git_plow_back_rest' in config:
        utils.GIT_PLOW_BACK_REST = config['git_plow_back_rest']
    if 'repertoire_git_plow_back_rest' in config:
        utils.REPERTOIRE_GIT_PLOW_BACK_REST = config['repertoire_git_plow_back_rest']
    if 'repertoire_installation_plow_back_rest' in config:
        utils.REPERTOIRE_INSTALLATION_PLOW_BACK_REST = config['repertoire_installation_plow_back_rest']
    if 'mysql_login' in config:
        utils.MYSQL_LOGIN = config['mysql_login']
    if 'mysql_pass' in config:
        utils.MYSQL_PASS = config['mysql_pass']
    if 'mysql_host' in config:
        utils.MYSQL_HOST = config['mysql_host']
    if 'mysql_database' in config:
        utils.MYSQL_DATABASE = config['mysql_database']
    if 'notification_adresse' in config:
        utils.NOTIFICATION_ADRESSE = config['notificaion_adresse']


def main():
    chargement_config()

    general_menu = menu.Menu()
    general_menu_selection = general_menu.show(
        {
            '1': u'Installation totale automatique',
            '2': u'Installation totale interactive'
        }, u'Menu installation solution plow pas à pas'
    )

    if general_menu_selection == 2:
        plow_solution.main()

if __name__ == '__main__':
    main()