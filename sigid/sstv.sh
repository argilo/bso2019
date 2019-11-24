#!/bin/bash

qrencode -l H -s 2 -o test.png "Sig. id. chal. 13: flag{sl0w_en0uGh_f0r_U}"
convert area52.jpg -crop 320x256+145+55 test.png -geometry +230+0 -composite area52.bmp
rm test.png
