#!/bin/bash

# Andrew J. Moodie
# Feb 2015
# easily remembered interface for vpn connection
if [ "$1" = "on" ]
then
    sudo /usr/sbin/vpnc RiceVPN.conf
elif [ "$1" = "off" ]
then
    vpnc­-disconnect
else
    echo "  input error -- one argument must be given"
    echo "  valid inputs: 'on' or 'off'"
fi
