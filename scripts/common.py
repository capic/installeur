# -*- coding: utf-8 -*-
__author__ = 'Vincent'

import utils
import os

def node_js():
    if utils.which('node') is None:
        print(u'_____ Installation de Nodejs _____')
        os.system('apt-get install node')
    else:
        print(u'Nodejs est déjà installé')
