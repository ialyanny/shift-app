#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generate 2027 shift schedule continuing 2026 8-day cycle logic."""
import datetime

D0 = datetime.date(2026, 1, 1)  # anchor: Jan1 2026 = Block1 Day1 (A1 B2)

def shift_for(d):
    idx = (d - D0).days % 8
    # idx 0,1: A1 B2 ; 2,3: C2 D1 ; 4,5: A2 B1 ; 6,7: C1 D2
    if idx in (0, 1):
        return {'A': '1', 'B': '2', 'C': '', 'D': ''}
    elif idx in (2, 3):
        return {'A': '', 'B': '', 'C': '2', 'D': '1'}
    elif idx in (4, 5):
        return {'A': '2', 'B': '1', 'C': '', 'D': ''}
    else:
        return {'A': '', 'B': '', 'C': '1', 'D': '2'}

# 2027 holidays: red = national day itself, yellow = compensatory (補假)
RED_2027 = {
    (1,1),
    (2,4),(2,5),(2,6),(2,7),(2,8),
    (2,28),
    (4,4),(4,5),
    (5,1),
    (6,9),
    (9,15),
    (9,28),
    (10,10),
    (10,25),
    (12,25),
}
YELLOW_2027 = {
    (2,9),(2,10),
    (3,1),
    (4,6),
    (4,30),
    (10,11),
    (12,24),
    (12,31),
}

WEEK_CN = ['一','二','三','四','五','六','日']  # Monday=0
# For display: 日一二三四五六, Sunday first
def weekday_cn(d):
    # Monday=0..Sunday=6 -> map to 日一二三四五六
    mapping = {0:'一',1:'二',2:'三',3:'四',4:'五',5:'六',6:'日'}
    return mapping[d.weekday()]

print("=== 2027 shift table (continuous from 2026-01-01 A1B2) ===")
for m in range(1,13):
    import calendar
    ndays = calendar.monthrange(2027, m)[1]
    first = datetime.date(2027, m, 1)
    print(f"\n--- {m}月 ({ndays}天, {first} {first.strftime('%a')}) ---")
    header_days = ' '.join(f"{d:2d}" for d in range(1, ndays+1))
    print(f"Day: {header_days}")
    wdays = ' '.join(weekday_cn(datetime.date(2027,m,d)) for d in range(1, ndays+1))
    print(f"Wkd: {wdays}")
    for team in ['A','B','C','D']:
        row = []
        for d in range(1, ndays+1):
            s = shift_for(datetime.date(2027,m,d))[team]
            row.append(s if s else '·')
        print(f"{team}: {' '.join(f'{x:2s}' for x in row)}")

print("\n=== Holiday coloring check ===")
for (m,d) in sorted(RED_2027):
    dt = datetime.date(2027,m,d)
    print(f"RED {m}/{d} {dt.strftime('%a')} {weekday_cn(dt)}")
for (m,d) in sorted(YELLOW_2027):
    dt = datetime.date(2027,m,d)
    print(f"YELLOW {m}/{d} {dt.strftime('%a')} {weekday_cn(dt)}")

print("\n=== Year boundary continuity ===")
for dt in [datetime.date(2026,12,29),datetime.date(2026,12,30),datetime.date(2026,12,31),
           datetime.date(2027,1,1),datetime.date(2027,1,2),datetime.date(2027,1,3)]:
    print(dt, dt.strftime('%a'), weekday_cn(dt), shift_for(dt))
