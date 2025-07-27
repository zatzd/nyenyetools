#!/bin/bash
clear
echo -e "\e[35mInstalling ZATZD OSINT Tools...\e[0m"

pkg update -y && pkg upgrade -y
pkg install python git -y
pip install -r requirements.txt

python tools_zatzd.py
