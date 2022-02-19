#!/bin/bash

mkdir ~/Documents/tst/bacon-bits
mv ~/Documents/tst/bacon ~/Documents/tst/bacon-bits/bacon
mv ~/Documents/tst/bacon-bits/bacon/.baconrc ~/Documents/tst/bacon-bits/.baconrc
echo 'source ~/Documents/tst/bacon-bits/.baconrc' >> ~/.zshrc
source ~/.zshrc