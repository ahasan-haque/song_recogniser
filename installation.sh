#!/bin/bash
echo -n Password:
read -s password
echo
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install portaudio ffmpeg mysql
brew services start mysql
echo $password | sudo  -S easy_install pyaudio pydub scipy matplotlib pip
echo $password | sudo -S pip install MySQL-python XlsxWriter
echo $password | sudo -S pip install numpy==1.10.0
pip install PyDejavu --user