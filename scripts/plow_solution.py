# -*- coding: utf-8 -*-
__author__ = 'Vincent'

from lib.menu import menu
import plow_back_rest

def menu_pas_a_pas():
    plow_menu = menu.Menu()
    plow_menu_selection = plow_menu.show(
        {
            '1': u'Installation de plow back rest',
            '2': u'Installation de plow python'
        }, u'Menu installation solution plow pas à pas'
    )

    if plow_menu_selection == 1:
        plow_back_rest.main()


def menu_principal():
    plow_menu = menu.Menu()
    plow_menu_selection = plow_menu.show(
        {
            '1': u'Installation totale',
            '2': u'Installation pas à pas'
        }, u'Menu installation solution plow')



def main():
    menu_principal()


if __name__ == '__main__':
    main()

