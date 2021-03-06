# -*- coding: utf-8 -*-
__author__ = 'Vincent'

import utils
import common
import os
import shutil


def creer_fichier_config():
    print(u'_____ Création du fichier de config _____')
    chemin_fichier_config = '%sconfig/local.json' % utils.REPERTOIRE_GIT_PLOW_BACK_REST

    contenu_fichier_config = \
        '{\r\n' \
        '   "db": {\r\n' \
        '       "host": "%s",\r\n' \
        '       "database": "%s",\r\n' \
        '       "user": "%s",\r\n' \
        '       "password": "%s"\r\n' \
        '   },\r\n' \
        '   "notification": {\r\n' \
        '      "activate": "%s",\r\n' \
        '       "address": "%s"' \
        '   }\r\n' \
        '}' \
        % (utils.MYSQL_HOST, utils.MYSQL_DATABASE, utils.MYSQL_LOGIN, utils.MYSQL_PASS, utils.NOTIFICATION_ACTIVATED,
           utils.NOTIFICATION_ADRESSE)

    fichier_config = open(chemin_fichier_config, 'wb')
    fichier_config.write(contenu_fichier_config)

    fichier_config.close()


def main():
    common.node_js()
    print(u'_____ Téléchargement de plow back rest _____')
    git_cmd = 'git clone %s %s' % (utils.GIT_PLOW_BACK_REST, utils.REPERTOIRE_GIT_PLOW_BACK_REST)
    os.system(git_cmd)
    os.system('npm install')
    creer_fichier_config()
    print(u'_____ Déplacement de plow back rest dans le dossier finale _____')
    shutil.copytree(utils.REPERTOIRE_GIT_PLOW_BACK_REST, utils.REPERTOIRE_INSTALLATION_PLOW_BACK_REST,
                    ignore=shutil.ignore_patterns(*utils.IGNORE_PATTERN))
    shutil.rmtree(utils.REPERTOIRE_GIT_PLOW_BACK_REST)