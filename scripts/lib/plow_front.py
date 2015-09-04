# -*- coding: utf-8 -*-
__author__ = 'Vincent'

import utils
import shutil
import common
import os


def creer_fichier_config():
    print()


def main():
    common.node_js()
    print(u'_____ Téléchargement de plow front _____')
    git_cmd = 'git clone %s %s' % (utils.GIT_PLOW_FRONT, utils.REPERTOIRE_GIT_PLOW_FRONT)
    os.system(git_cmd)
    os.system('bower --allow-root install')
    print(u'_____ Déplacement de plow front dans le dossier finale _____')
    shutil.copytree(utils.REPERTOIRE_GIT_PLOW_FRONT, utils.REPERTOIRE_INSTALLATION_PLOW_FRONT,
                    ignore=shutil.ignore_patterns(*utils.IGNORE_PATTERN))
    creer_fichier_config()
    shutil.rmtree(utils.REPERTOIRE_GIT_PLOW_FRONT)