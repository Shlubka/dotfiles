import os

def addcolorwaybar(lines):
    col1 = (20, 29, 50, 64, 76)
    col2 = (21, 30, 51, 65, 77, 85)
    for i in col1:
        lines.pop(i)
        lines.insert(i, f'  color: {color[0]};\n')
    for i in col2:
        lines.pop(i)
        lines.insert(i, f'  background-color: {color[3]};\n')
    lines.pop(38)
    lines.insert(38, f'border-color: {color[5]};\n')
    lines.pop(57)
    lines.insert(57, f'  color: {color[1]};\n')
    lines.pop(110)
    lines.insert(110, f'        color: {color[0]};\n')
    lines.pop(118)
    lines.insert(118, f'        color: {color[0]};\n')
    lines.pop(124)
    lines.insert(124, f'        background-color: {color[3]};\n')

def addcolorwofi(wlines):
    col1 = (2, 18, 25, 46) #bgcolor 
    for i in col1:
        wlines.pop(i)
        wlines.insert(i, f'  background-color: {color[0]};\n')
    wlines.pop(4)
    wlines.insert(4, f'  border: 2px solid {color[5]};\n')
    wlines.pop(10)
    wlines.insert(10, f'  color: {color[15]};\n')
    wlines.pop(36)
    wlines.insert(36, f'  color: {color[15]};\n')
    wlines.pop(40)
    wlines.insert(40, f'  background-color: {color[15]};\n')


def addcolormako(mlines):
    mlines.pop(2)# main bg
    mlines.insert(2, f'background-color={color[0]}cc\n')
    mlines.pop(3)# tc notify text
    mlines.insert(3, f'text-color={color[5]}\n')
    mlines.pop(10)# main border
    mlines.insert(10, f'border-color={color[1]}\n')
    mlines.pop(18)
    mlines.insert(18, f'format=<span color="{color[15]}" size="13pt" line_height="1.3"><b>%a</b></span>\\n<span color="{color[15]}"><i>%s</i></span>\\n%b\n')
    print(mlines)


color = []
with  open(r'~/.cache/wal/colors') as file:
    collors = file.readlines()
for collor in collors:
    collor = collor[0:-1]
    color.append(collor)
#print(color)

with open(r'~/.config/waybar/style.css') as waybarcss:
    lines = waybarcss.readlines()

with open(r'~/.config/wofi/style.css') as woficolor:
    wlines = woficolor.readlines()

with open(r'~/.config/mako/config') as moficolor:
    mlines = moficolor.readlines()


addcolorwaybar(lines)
addcolorwofi(wlines)
addcolormako(mlines)

with open(r'~/.config/waybar/style.css', 'w') as file:
    file.writelines(lines)

with open('~/.config/wofi/style.css', 'w') as wfile:
    wfile.writelines(wlines)

with open('~/.config/mako/config', 'w+') as mfile:
    #print(mfile)
    mfile.writelines(mlines)

