#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Render 2027 shift poster PNGs, TRUE 28-day cycle."""
import datetime, calendar
from PIL import Image, ImageDraw, ImageFont

BASE_A = '1000220022200220001100111001'
BASE_D = '0111001100022002220022000110'
def _opp(s):
    return ''.join('0' if c=='0' else ('1' if c=='2' else '2') for c in s)
BASE_B = _opp(BASE_A)
BASE_C = _opp(BASE_D)
BASE = {'A':BASE_A,'B':BASE_B,'C':BASE_C,'D':BASE_D}
D0 = datetime.date(2026,1,1)
def shift_for(d):
    idx=(d-D0).days%28
    return {'A':BASE_A[idx],'B':BASE_B[idx],'C':BASE_C[idx],'D':BASE_D[idx]}

RED = {(1,1),(2,4),(2,5),(2,6),(2,7),(2,8),(2,28),(4,4),(4,5),(5,1),(6,9),(9,15),(9,28),(10,10),(10,25),(12,25)}
YELLOW = {(2,9),(2,10),(3,1),(4,6),(4,30),(10,11),(12,24),(12,31)}
MONTH_ENG = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
WEEK_MAP = {0:'一',1:'二',2:'三',3:'四',4:'五',5:'六',6:'日'}
FONT_JH = r'C:\Windows\Fonts\msjh.ttc'
FONT_JH_B = r'C:\Windows\Fonts\msjhbd.ttc'
FONT_KAI = r'C:\Windows\Fonts\kaiu.ttf'
def font(size,bold=False,kai=False):
    try:
        if kai: return ImageFont.truetype(FONT_KAI,size)
        return ImageFont.truetype(FONT_JH_B if bold else FONT_JH,size)
    except Exception:
        return ImageFont.load_default()
def disp(v): return '' if v=='0' else v

def draw_page(months,out_path,first_half):
    W,H=1240,1754
    img=Image.new('RGB',(W,H),'white')
    dr=ImageDraw.Draw(img)
    for y in range(H):
        t=y/H
        r=int(253*(1-t)+232*t); g=int(235*(1-t)+242*t); b=int(235*(1-t)+253*t)
        dr.line([(0,y),(W,y)],fill=(r,g,b))
    y=18
    f_year=font(56,bold=True); f_title=font(30,bold=True)
    dr.text((30,y),'2027',font=f_year,fill=(220,0,0))
    w_year=dr.textlength('2027',font=f_year)
    dr.text((30+w_year+12,y+10),'台灣康寧顯示玻璃股份有限公司  公司統編04388145',font=f_title,fill=(220,0,0))
    y+=70
    f_sub=font(22,bold=True)
    dr.text((30,y),'CORNING  Corning Display Technologies Taiwan',font=font(22),fill=(0,40,160))
    dr.text((760,y),'職工福利委員會13525747',font=f_sub,fill=(220,0,0))
    y+=38
    left=20; label_w=64; day_w=(W-left*2-label_w)/31; row_h=26; month_gap=10
    grid_color=(120,150,200)
    for m in months:
        ndays=calendar.monthrange(2027,m)[1]
        row_labels=[MONTH_ENG[m],str(m),'A','B','C','D']
        for ri in range(6):
            y0=y+ri*row_h
            x0=left
            dr.rectangle([x0,y0,x0+label_w,y0+row_h],outline=grid_color,fill='white')
            txt=row_labels[ri]
            f=font(16) if ri==0 else (font(18,bold=True) if ri==1 else font(17,bold=True))
            col=(0,40,160) if ri==0 else ((220,0,0) if ri==1 else (0,0,0))
            tw=dr.textlength(txt,font=f)
            dr.text((x0+(label_w-tw)/2,y0+2),txt,font=f,fill=col)
            for d in range(1,32):
                x=left+label_w+(d-1)*day_w
                if d>ndays:
                    dr.rectangle([x,y0,x+day_w,y0+row_h],outline=grid_color,fill=(210,210,210))
                    continue
                dt=datetime.date(2027,m,d)
                fill='white'; tcol=(0,0,0); fcell=font(15,bold=True); val=''
                if ri==0:
                    val=str(d); fcell=font(15)
                    if (m,d) in RED: fill=(255,0,0); tcol=(255,255,255); fcell=font(15,bold=True)
                    elif (m,d) in YELLOW: fill=(255,255,0); tcol=(0,0,0)
                elif ri==1:
                    val=WEEK_MAP[dt.weekday()]; fcell=font(15)
                    if val=='日': tcol=(220,0,0); fcell=font(15,bold=True)
                else:
                    team=['A','B','C','D'][ri-2]
                    val=disp(shift_for(dt)[team]); fcell=font(16,bold=True)
                dr.rectangle([x,y0,x+day_w,y0+row_h],outline=grid_color,fill=fill)
                if val:
                    tw=dr.textlength(val,font=fcell)
                    dr.text((x+(day_w-tw)/2,y0+2),val,font=fcell,fill=tcol)
        y+=6*row_h+month_gap
    y+=6
    f_foot=font(20)
    if first_half:
        lines=[('1→早班/日班','台南廠06-5050520','南科管理局06-5051001'),('2→晚班/夜班','台中廠04-24658999','南科警察隊06-5051405'),('　→off','台北02-27160338','南科消防分隊06-5052995'),('■→國定假日','內湖02-8178132','南科診所06-5050225'),('■→補假','新竹03-5820550','南科台銀06-5051701'),('■→連續彈性假','','')]
    else:
        lines=[('1→早班/日班','大都會計程車02-4499178','安環衛專線#1234'),('2→晚班/夜班','國通計程車(台中)04-24618999','安全室專線#1332'),('　→off','EAP免費專線00801-491519','廠務部專線#1000'),('■→國定假日','EAP24HR熱線02-77032446','性騷擾申訴專線#1777'),('■→補假','',''),('■→連續彈性假','','')]
    for a,b,c in lines:
        dr.text((30,y),a,font=f_foot,fill=(220,0,0))
        dr.text((290,y),b,font=f_foot,fill=(220,0,0))
        dr.text((730,y),c,font=f_foot,fill=(220,0,0))
        y+=30
    dr.text((30,H-40),'邏輯:28天一循環(2026/1/1為第1天，A/B同休反班、C/D同休反班，每天1日+1夜共2人)  紅=國定假日當日 黃=補假',font=font(16),fill=(80,80,80))
    img.save(out_path,dpi=(200,200))
    print(f'saved {out_path}')

draw_page([1,2,3,4,5,6],'2027輪班表_1-6月.png',True)
draw_page([7,8,9,10,11,12],'2027輪班表_7-12月.png',False)
