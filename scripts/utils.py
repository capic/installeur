__author__ = 'Vincent'

GIT_PLOW_BACK_REST = ''
REPERTOIRE_GIT_PLOW_BACK_REST = ''
REPERTOIRE_INSTALLATION_PLOW_BACK_REST
MYSQL_HOST = ''
MYSQL_LOGIN = ''
MYSQL_PASSWORD = ''
MYSQL_DATABASE = ''
NOTIFICATION_ADRESSE = ''


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