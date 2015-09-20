# -*- coding: utf-8 -*-
__author__ = 'Vincent'

# menu serveur
SERVEUR_APACHE = '1'
SERVEUR_LIGHHTPD = '2'
# menu installation
INSTALLATION_TYPE_AUTOMATIQUE = '1'
INSTALLATION_TYPE_INTERACTIVE = '2'
INSTALLATION_TYPE_SERVEUR = '3'
INSTALLATION_TYPE_SOLUTION_PLOW = '4'
INSTALLATION_TYPE_TOTALE_SANS_SERVEUR = '5'
# menu

GIT_PLOW_BACK_REST = ''
GIT_PLOW_PYTHON = ''
GIT_PLOW_FRONT = ''

REPERTOIRE_GIT_PLOW_BACK_REST = ''
REPERTOIRE_GIT_PLOW_PYTHON = ''
REPERTOIRE_GIT_PLOW_FRONT = ''

REPERTOIRE_INSTALLATION_PLOW_BACK_REST = ''
REPERTOIRE_INSTALLATION_PLOW_PYTHON = ''
REPERTOIRE_INSTALLATION_PLOW_FRONT = ''

REST_ADRESSE = ''

REPERTOIRE_WEB_LOG = ''
REPERTOIRE_TELECHARGEMENT_TEMPORAIRE = ''
REPERTOIRE_TELECHARGEMENT = ''

MYSQL_HOST = ''
MYSQL_LOGIN = ''
MYSQL_PASSWORD = ''
MYSQL_DATABASE = ''
NOTIFICATION_ACTIVATED = ''
NOTIFICATION_ADRESSE = ''

LOG_OUTPUT = ''
CONSOLE_OUTPUT = ''

IGNORE_PATTERN = ('.git', 'tmp', '.svn', '.gitignore')


def which(program):
    import os

    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None