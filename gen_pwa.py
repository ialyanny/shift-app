#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generate PWA icons for shift app."""
from PIL import Image, ImageDraw, ImageFont

def make_icon(size, path):
    img = Image.new('RGB', (size, size), 'white')
    dr = ImageDraw.Draw(img)
    # gradient bg pink->blue
    for y in range(size):
        t = y / size
        r = int(254*(1-t) + 191*t)
        g = int(202*(1-t) + 219*t)
        b = int(202*(1-t) + 254*t)
        dr.line([(0, y), (size, y)], fill=(r, g, b))
    # rounded card
    pad = size // 8
    dr.rounded_rectangle([pad, pad, size-pad, size-pad], radius=size//6, fill='white', outline=(220, 0, 0), width=max(2, size//64))
    # text
    try:
        f = ImageFont.truetype(r'C:\Windows\Fonts\msjhbd.ttc', size//3)
        f2 = ImageFont.truetype(r'C:\Windows\Fonts\msjh.ttc', size//7)
    except Exception:
        f = ImageFont.load_default(); f2 = f
    t1 = '輪班'
    w1 = dr.textlength(t1, font=f)
    dr.text(((size-w1)/2, size*0.24), t1, font=f, fill=(220, 0, 0))
    t2 = '共同休假'
    w2 = dr.textlength(t2, font=f2)
    dr.text(((size-w2)/2, size*0.62), t2, font=f2, fill=(30, 60, 120))
    img.save(path)
    print('saved', path)

make_icon(192, 'icon-192.png')
make_icon(512, 'icon-512.png')
make_icon(180, 'apple-touch-icon.png')
