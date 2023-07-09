#!/bin/bash

rt=$(whoami)

if [ $rt != "root" ];then
    echo "Lo siento tienes que ser super usuario para realizar esta acción"

else
    lsblk -f
    echo -n "Seleccione su dispostivo usb: "
    read ubs
    echo "Montando su ubs en ~/USB"
    mount -U $ubs /home/jisas/USB
fi