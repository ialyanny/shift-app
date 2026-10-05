import re
html = open('shift-app.html', encoding='utf-8').read()
for name in ['A', 'B', 'C', 'D']:
    pat = name + r':"([012]+)"'
    m = re.search(pat, html)
    print(name, m.group(1) if m else 'NOT FOUND')
print('expected A 1000220022200220001100111001')
print('expected D 0111001100022002220022000110')
