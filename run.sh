#!/bin/bash
wget -O model.zip "https://www.dropbox.com/s/1paw83y9jyednh4/save_v2_ep1k.zip?dl=0"
unzip model.zip -d save/ 
python3 update_checkpoint.py
python3 test.py
