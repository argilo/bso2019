#!/bin/bash

convert \
  \( \
    -background White \
    -gravity Center \
    -pointsize 400 \
    label:flag\{look_closer_a4146a8247fa439d6879\} \
    -rotate 270 \
  \) \
  bsides-ottawa-logo.jpg \
  -append \
  -crop 50x100%-30+0 \
  -gravity North \
  -extent 100%x200% \
  -fx "xx = i; yy = ln(j/7978/2 * (exp(5)-1) + 1) / 5 * 7978; v.p{xx,yy}" \
  logo-flag.png
