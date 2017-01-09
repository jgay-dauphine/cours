#!/bin/bash

# Script permettant l'export en pdf d'une présentation basé sur la prise de
# screenshots puis la recomposition en pdf...

screenDir="/home/jgay/Documents/presentations/screenshots"

mkdir -p ${screenDir}            # Creates it if missing

echo "Now open up your presentation and set it to fullscreen."
echo "You have 10 seconds."
t=10
while [ $t -gt 0 ]; do
      echo "$t..."
      sleep 1
      t=$(($t-1))
done

# Nombre max de slides
i=1000000
# temps entre deux screenshots
pause=1

while true; do
    scrot -d $pause "${screenDir}/shot$i.png"
    xdotool key space
    i=$(($i+1))
done

# Composition en pdf
#for name in ${screenDir}/*.png
#do
#    convert $name ${screenDir}/$(basename $name .png).pdf
#done
#pdftk ${screenDir}/*.pdf cat output Presentation.pdf
