# -*- coding: utf-8 -*-
__author__ = 'Vincent'

from lib.menu import menu
import plow_solution

def main():
    general_menu = menu.Menu()
    general_menu_selection = general_menu.show(
        {
            '1': u'Installation totale automatique',
            '2': u'Installation totale interactive'
        }, u'Menu installation solution plow pas à pas'
    )

    if general_menu_selection == 2:
        plow_solution.main()

if __name__ == '__main__':
    main()