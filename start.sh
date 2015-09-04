#!/usr/bin/env bash
if [[ $EUID -ne 0 ]]; then
   echo "Ce script doit être lancé avec les droits super utilisateur" 1>&2
   exit 1
fi

apt-get update
apt-get -y upgrade
if ! which python >/dev/null; then
    echo "<<<<< Installation de python >>>>>"
    apt-get -y install git python2.7 python3 python-dev
fi

if ! which python >/dev/null; then
    echo "!!!!!! Python n'est pas installé !!!!!"
    exit
fi

#python scripts/