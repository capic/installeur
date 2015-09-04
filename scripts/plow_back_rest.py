# -*- coding: utf-8 -*-
__author__ = 'Vincent'

import utils
import common
import os
import shutil


def creerFichierConfig():
    print(u'_____ Création du fichier de config _____')
    chemin_fichier_config = '%sconfig/default.json' % utils.REPERTOIRE_GIT_PLOW_BACK_REST

    contenu_fichier_config = \
        '{\
            "db": {\
                "host": "%s",\
                "database": "%s",\
                "user": "%s",\
                "password": "%s"\
                },\
                "notification": {\
                    "address": "%s}"\
                }\
              }' % (
            utils.MYSQL_HOST, utils.MYSQL_DATABASE, utils.MYSQL_LOGIN, utils.MYSQL_PASS, utils.NOTIFICATION_ADRESSE)

    fichier_config = open(chemin_fichier_config, 'wb')
    fichier_config.write(chemin_fichier_config)

    fichier_config.close()


def main():
    common.node_js()
    print(u'_____ Téléchargement de plow back rest _____')
    git_cmd = 'git clone %s %s' % (utils.GIT_PLOW_BACK_REST, utils.REPERTOIRE_GIT_PLOW_BACK_REST)
    os.system(git_cmd)
    os.system('npm install')
    creerFichierConfig()
    print(u'_____ Déplacement de plow back rest dans le dossier finale _____')
    shutil.copytree(utils.REPERTOIRE_GIT_PLOW_BACK_REST, utils.REPERTOIRE_INSTALLATION_PLOW_BACK_REST,
                    ignore=shutil.ignore_patterns(*utils.IGNORE_PATTERN))
    shutil.rmtree(utils.REPERTOIRE_GIT_PLOW_BACK_REST)