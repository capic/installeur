# -*- coding: utf-8 -*-
__author__ = 'Vincent'

GIT_PLOW_BACK_REST = ''
GIT_PLOW_PYTHON = ''

REPERTOIRE_GIT_PLOW_BACK_REST = ''
REPERTOIRE_GIT_PLOW_PYTHON = ''

REPERTOIRE_INSTALLATION_PLOW_BACK_REST = ''
REPERTOIRE_INSTALLATION_PLOW_PYTHON = ''

REST_ADRESSE = ''

REPERTOIRE_WEB_LOG = ''
REPERTOIRE_DOWNLOAD_DESTINATION_TEMP = ''
REPERTOIRE_DOWNLOAD_DESTINATION = ''

MYSQL_HOST = ''
MYSQL_LOGIN = ''
MYSQL_PASSWORD = ''
MYSQL_DATABASE = ''
NOTIFICATION_ADRESSE = ''

LOG_OUTPUT = ''
CONSOLE_OUTPUT = ''

IGNORE_PATTERN = ('.git', 'tmp', '.svn')


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