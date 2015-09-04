__author__ = 'Vincent'

from lib.menu import menu


def main():
    plow_menu = menu.Menu()
    plow_menu_selection = plow_menu.show({'1':'Installation totale', '2':'Installation pas à pas'}, 'Menu installation solution plow')

    print 'Séléction: %s' % plow_menu_selection


if __name__ == '__main__':
    main()

