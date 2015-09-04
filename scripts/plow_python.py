# -*- coding: utf-8 -*-
__author__ = 'Vincent'

import utils
import os
import shutil


def creer_fichier_config():
    print(u'_____ Création du fichier de config _____')
    chemin_fichier_config = '%sconfig.cfg' % utils.REPERTOIRE_INSTALLATION_PLOW_PYTHON

    contenu_fichier_config = \
        'rest_adresse=%s\r\n\repertoire_web_log=%s\r\n\repertoire_telechargement_temporaire=%s\r\n\repertoire_telechargement=%s\r\n\log_output=%s\r\n\console_output=%s\r\n' % (
            utils.REST_ADRESSE, utils.REPERTOIRE_WEB_LOG, utils.REPERTOIRE_DOWNLOAD_DESTINATION_TEMP,
            utils.REPERTOIRE_DOWNLOAD_DESTINATION, utils.LOG_OUTPUT, utils.CONSOLE_OUTPUT)

    fichier_config = open(chemin_fichier_config, 'wb')
    fichier_config.write(contenu_fichier_config)

    fichier_config.close()


def main():
    print(u'_____ Téléchargement de plow python _____')
    git_cmd = 'git clone %s %s' % (utils.GIT_PLOW_PYTHON, utils.REPERTOIRE_GIT_PLOW_PYTHON)
    os.system(git_cmd)
    print(u'_____ Déplacement de plow python dans le dossier finale _____')
    shutil.copytree(utils.REPERTOIRE_GIT_PLOW_PYTHON, utils.REPERTOIRE_INSTALLATION_PLOW_PYTHON,
                    ignore=shutil.ignore_patterns(*utils.IGNORE_PATTERN))
    creer_fichier_config()
    shutil.rmtree(utils.REPERTOIRE_GIT_PLOW_PYTHON)