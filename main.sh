#!/bin/sh

python3 main.py
ver=$(cat version.txt)
echo "$ver"
curl https://stable.dl2.discordapp.net/apps/linux/$ver/discord-$ver.deb --output /home/dani/discord_update/rea/$ver.deb
sudo dpkg -i rea/$ver.deb