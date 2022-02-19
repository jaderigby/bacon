#!/bin/bash

mkdir ~/Documents/bacon-bits
mv ~/Documents/bacon ~/Documents/bacon-bits/bacon
scp ~/Documents/bacon-bits/bacon/.baconrc ~/Documents/bacon-bits/.baconrc
echo 'source ~/Documents/bacon-bits/.baconrc' >> ~/.zshrc
source ~/.zshrc