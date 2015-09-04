# -*- coding: utf-8 -*-
__author__ = 'Vincent'

from lib.menu import menu
import plow_solution
import utils
import os


def chargement_config():
    print("_____ Chargement de la config _____")
    config = {}
    execfile(os.path.dirname(os.path.abspath(__file__)) + "/../config.cfg", config)

    if 'git_plow_back_rest' in config:
        utils.GIT_PLOW_BACK_REST = config['git_plow_back_rest']
    if 'git_plow_python' in config:
        utils.GIT_PLOW_PYTHON = config['git_plow_python']
    if 'git_plow_front' in config:
        utils.GIT_PLOW_FRONT = config['git_plow_front']
    if 'repertoire_git_plow_back_rest' in config:
        utils.REPERTOIRE_GIT_PLOW_BACK_REST = config['repertoire_git_plow_back_rest']
    if 'repertoire_git_plow_python' in config:
        utils.REPERTOIRE_GIT_PLOW_PYTHON = config['repertoire_git_plow_python']
    if 'repertoire_git_plow_front' in config:
        utils.REPERTOIRE_GIT_PLOW_FRONT = config['repertoire_git_plow_front']
    if 'repertoire_installation_plow_back_rest' in config:
        utils.REPERTOIRE_INSTALLATION_PLOW_BACK_REST = config['repertoire_installation_plow_back_rest']
    if 'repertoire_installation_plow_python' in config:
        utils.REPERTOIRE_INSTALLATION_PLOW_PYTHON = config['repertoire_installation_plow_python']
    if 'repertoire_installation_plow_front' in config:
        utils.REPERTOIRE_INSTALLATION_PLOW_FRONT = config['repertoire_installation_plow_front']
    if 'mysql_login' in config:
        utils.MYSQL_LOGIN = config['mysql_login']
    if 'mysql_pass' in config:
        utils.MYSQL_PASS = config['mysql_pass']
    if 'mysql_host' in config:
        utils.MYSQL_HOST = config['mysql_host']
    if 'mysql_database' in config:
        utils.MYSQL_DATABASE = config['mysql_database']
    if 'notification_adresse' in config:
        utils.NOTIFICATION_ADRESSE = config['notification_adresse']
    if 'rest_adresse' in config:
        utils.REST_ADRESSE = config['rest_adresse']
    if 'repertoire_web_log' in config:
        utils.REPERTOIRE_WEB_LOG = config['repertoire_web_log']
    if 'repertoire_download_destination_temp' in config:
        utils.REPERTOIRE_DOWNLOAD_DESTINATION_TEMP = config['repertoire_download_destination_temp']
    if 'repertoire_download_destination' in config:
        utils.REPERTOIRE_DOWNLOAD_DESTINATION = config['repertoire_download_destination']
    if 'log_output' in config:
        utils.LOG_OUTPUT = config['log_output']
    if 'console_output' in config:
        utils.CONSOLE_OUTPUT = config['console_output']


def menu_installation():
    installation_menu = menu.Menu()
    installation_menu_selection = installation_menu.show(
        {

        }
    )

def main():
    chargement_config()

    general_menu = menu.Menu()
    general_menu_selection = general_menu.show(
        {
            utils.INSTALLATION_TYPE_AUTOMATIQUE: u'Installation totale automatique',
            utils.INSTALLATION_TYPE_INTERACTIVE: u'Installation totale interactive'
        }, u'Menu installation général'
    )

    print(u'Séléction => %s' % general_menu_selection)
    if general_menu_selection == utils.INSTALLATION_TYPE_INTERACTIVE:
        plow_solution.main()

if __name__ == '__main__':
    main()