# -*- coding: utf-8 -*-
__author__ = 'Vincent'

from lib.menu import menu
import plow_back_rest
import plow_python

def menu_pas_a_pas():
    plow_menu = menu.Menu()
    plow_menu_selection = plow_menu.show(
        {
            '1': u'Installation de plow back rest',
            '2': u'Installation de plow python'
        }, u'Menu installation solution plow pas à pas'
    )

    if plow_menu_selection == '1':
        plow_back_rest.main()
    elif plow_menu_selection == '2':
        plow_python.main()


def menu_principal():
    plow_menu = menu.Menu()
    plow_menu_selection = plow_menu.show(
        {
            '1': u'Installation totale',
            '2': u'Installation pas à pas'
        }, u'Menu installation solution plow')

    if plow_menu_selection == '2':
        menu_pas_a_pas()


def main():
    menu_principal()


