import math
import re
import numpy as np

IDlistNameColor = {
    'aliceblue': 'F0F8FF',
    'antiquewhite': 'FAEBD7',
    'aqua': '00FFFF',
    'aquamarine': '7FFFD4',
    'azure': 'F0FFFF',
    'beige': 'F5F5DC',
    'bisque': 'FFE4C4',
    'black': '000000',
    'blanchedalmond': 'FFEBCD',
    'blue': '0000FF',
    'blueviolet': '8A2BE2',
    'brown': 'A52A2A',
    'burlywood': 'DEB887',
    'cadetblue': '5F9EA0',
    'chartreuse': '7FFF00',
    'chocolate': 'D2691E',
    'coral': 'FF7F50',
    'cornflowerblue': '6495ED',
    'cornsilk': 'FFF8DC',
    'crimson': 'DC143C',
    'cyan': '00FFFF',
    'darkblue': '00008B',
    'darkcyan': '008B8B',
    'darkgoldenrod': 'B8860B',
    'darkgray': 'A9A9A9',
    'darkgrey': 'A9A9A9',
    'darkgreen': '006400',
    'darkkhaki': 'BDB76B',
    'darkmagenta': '8B008B',
    'darkolivegreen': '556B2F',
    'darkorange': 'FF8C00',
    'darkorchid': '9932CC',
    'darkred': '8B0000',
    'darksalmon': 'E9967A',
    'darkseagreen': '8FBC8F',
    'darkslateblue': '483D8B',
    'darkslategray': '2F4F4F',
    'darkslategrey': '2F4F4F',
    'darkturquoise': '00CED1',
    'darkviolet': '9400D3',
    'deeppink': 'FF1493',
    'deepskyblue': '00BFFF',
    'dimgray': '696969',
    'dimgrey': '696969',
    'dodgerblue': '1E90FF',
    'firebrick': 'B22222',
    'floralwhite': 'FFFAF0',
    'forestgreen': '228B22',
    'fuchsia': 'FF00FF',
    'gainsboro': 'DCDCDC',
    'ghostwhite': 'F8F8FF',
    'gold': 'FFD700',
    'goldenrod': 'DAA520',
    'gray': '808080',
    'grey': '808080',
    'green': '008000',
    'greenyellow': 'ADFF2F',
    'honeydew': 'F0FFF0',
    'hotpink': 'FF69B4',
    'indianred': 'CD5C5C',
    'indigo': '4B0082',
    'ivory': 'FFFFF0',
    'khaki': 'F0E68C',
    'lavender': 'E6E6FA',
    'lavenderblush': 'FFF0F5',
    'lawngreen': '7CFC00',
    'lemonchiffon': 'FFFACD',
    'lightblue': 'ADD8E6',
    'lightcoral': 'F08080',
    'lightcyan': 'E0FFFF',
    'lightgoldenrodyellow': 'FAFAD2',
    'lightgray': 'D3D3D3',
    'lightgrey': 'D3D3D3',
    'lightgreen': '90EE90',
    'lightpink': 'FFB6C1',
    'lightsalmon': 'FFA07A',
    'lightseagreen': '20B2AA',
    'lightskyblue': '87CEFA',
    'lightslategray': '778899',
    'lightslategrey': '778899',
    'lightsteelblue': 'B0C4DE',
    'lightyellow': 'FFFFE0',
    'lime': '00FF00',
    'limegreen': '32CD32',
    'linen': 'FAF0E6',
    'magenta': 'FF00FF',
    'maroon': '800000',
    'mediumaquamarine': '66CDAA',
    'mediumblue': '0000CD',
    'mediumorchid': 'BA55D3',
    'mediumpurple': '9370DB',
    'mediumseagreen': '3CB371',
    'mediumslateblue': '7B68EE',
    'mediumspringgreen': '00FA9A',
    'mediumturquoise': '48D1CC',
    'mediumvioletred': 'C71585',
    'midnightblue': '191970',
    'mintcream': 'F5FFFA',
    'mistyrose': 'FFE4E1',
    'moccasin': 'FFE4B5',
    'navajowhite': 'FFDEAD',
    'navy': '000080',
    'oldlace': 'FDF5E6',
    'olive': '808000',
    'olivedrab': '6B8E23',
    'orange': 'FFA500',
    'orangered': 'FF4500',
    'orchid': 'DA70D6',
    'palegoldenrod': 'EEE8AA',
    'palegreen': '98FB98',
    'paleturquoise': 'AFEEEE',
    'palevioletred': 'DB7093',
    'papayawhip': 'FFEFD5',
    'peachpuff': 'FFDAB9',
    'peru': 'CD853F',
    'pink': 'FFC0CB',
    'plum': 'DDA0DD',
    'powderblue': 'B0E0E6',
    'purple': '800080',
    'rebeccapurple': '663399',
    'red': 'FF0000',
    'rosybrown': 'BC8F8F',
    'royalblue': '041690',
    'saddlebrown': '8B4513',
    'salmon': 'FA8072',
    'sandybrown': 'F4A460',
    'seagreen': '2E8B57',
    'seashell': 'FFF5EE',
    'sienna': 'A0522D',
    'silver': 'C0C0C0',
    'skyblue': '87CEEB',
    'slateblue': '6A5ACD',
    'slategray': '708090',
    'slategrey': '708090',
    'snow': 'FFFAFA',
    'springgreen': '00FF7F',
    'steelblue': '4682B4',
    'tan': 'D2B48C',
    'teal': '008080',
    'thistle': 'D8BFD8',
    'tomato': 'FF6347',
    'turquoise': '40E0D0',
    'violet': 'EE82EE',
    'wheat': 'F5DEB3',
    'white': 'FFFFFF',
    'whitesmoke': 'F5F5F5',
    'yellow': 'FFFF00',
    'yellowgreen': '9ACD32'
}


def extract_comment(line):
    pattern_comment = r';\s*/\*(.*)\*/'  # extract comment at line end
    match = re.search(pattern_comment, line)
    if match:
        cmt = match.group(1)
        cmt = cmt.strip()  # trim: left and right
        # remove: space*/space/*space
        cmt = re.sub(r'((\*/)|(/\*))\s*', '', cmt)
        return cmt
    return ""


def extract_hexa(line):
    pattern = r"#([a-fA-F0-9]{6})|#([a-fA-F0-9]{3})"
    match = ""

    matches = re.findall(pattern, line)
    if matches:
        match = matches[0][0] if matches[0][0] else matches[0][1]

    return match


def extract_hexa_list(line):
    pattern = r"#([a-fA-F0-9]{6})|#([a-fA-F0-9]{3})"  # code #ABCDEF ou #ABC
    r = []
    hexa = re.findall(pattern, line)
    for hex_value in hexa:
        if hex_value[0]:  # Check if first group matched
            r.append(hex_value[0])
        elif hex_value[1]:  # Check if second group matched
            r.append(hex_value[1])
    return np.array(r)


def color_name2rgb(color_name):
    res = " ".join(re.findall(r"..", IDlistNameColor[color_name.lower()]))
    rgb = [int(color, 16) for color in res.split(" ")]
    s_rgb = ' '.join(f'{value:03d}' for value in rgb)
    return s_rgb.strip()


def extract_color_named(line):
    rgb = []

    for color_name in IDlistNameColor.keys():
        if re.search(r':.*(?:\s*|,|:)\b({})\b.*;'.format(color_name), line, re.IGNORECASE):
            rgb.append(color_name2rgb(color_name))

    return rgb


def remainder(x, y):
    return x % y

'''
# Conversion valeur HSL à RGB
# param: ligne en cours ddu fichier CSS
# return: le format GPL de la couleur
# sourcing:
# + Converts HSL colorspace (Hue/Saturation/Value) to RGB colorspace.
#         Formula from http://www.easyrgb.com/math.php?MATH=M19#text19
# + un code source python ;)
'''
def hsl2Rgb(h, s, l):
    
    h = round(h / 360.0, 5)
    s = round(s / 100.0, 5)
    l = round(l / 100.0, 5)
#si s=0 alors
    r = g = b = l * 255.0

    if s != 0.0:
        var_2 = l * (1.0 + s) if l < 0.5 else (l + s) - (s * l)
        var_1 = 2.0 * l - var_2
        r = 255 * hue2rgb(var_1, var_2, h + (1.0 / 3.0))
        g = 255 * hue2rgb(var_1, var_2, h)
        b = 255 * hue2rgb(var_1, var_2, h - (1.0 / 3.0))

    sRgb = f"{r:.0f} {g:.0f} {b:.0f}"
    return sRgb.strip()

'''
# Sous-Routine de conversion valeur HSL à RGB appel de hsl2Rgb
# param: traitemet pour obtenir HUE
# return: valeur parametrée
# sourcing:
# + Converts HSL colorspace (Hue/Saturation/Value) to RGB colorspace.
#      (obsolete)   Formula from http://www.easyrgb.com/math.php?MATH=M19#text19
# + NEW! Formula from https://www.easyrgb.com/en/math.php
# + un code source python ;)
'''
def hue2rgb(var_1, var_2, h):
    if h < 0:
        h += 1
    if h > 1:
        h -= 1
    if 6 * h < 1:
        return var_1 + (var_2 - var_1) * 6 * h
    if 2 * h < 1:
        return var_2
    if 3 * h < 2:
        return var_1 + (var_2 - var_1) * (2.0 / 3.0 - h) * 6
    return var_1

'''
# Extrait du fichier CSS le format:
# RGB strict: rgb(R%, G%, B%) ou rgba(R%, G%, B%, A%)
# HSL strict: hsl(H~unitAngle, S%, L%) ou hsl(H~uAngle, S%, L%, A%)
# RGB|HSL: rgb(R[0..255], G[0..255], B[0..255])
#          rgba(R[0..255], G[0..255], B[0..255], A)
#          hsl(H, S%, L%)
#          hsla(H, S%, L%, A)
# param: ligne en cours du fichier CSS
# return: le format GPL de la couleur
'''
def extractRgbHsl(line):
    patternStrictRgb = r'(rgb)a?\(\s*(\d{1,3})%\s*,\s*(\d{1,3})%\s*,\s*(\d{1,3})%.*\)'
    patternStrictHsl = r'(?:hsl)a?\(\s*(\d*?\.?\d*)(deg|grad|rad|turn)\s*,\s*(\d{1,3})%\s*,\s*(\d{1,3})%.*\)'
    patternRgbHsl = r'(rgb|hsl)a?\(\s*(\d{1,3})\s*,\s*(\d{1,3})%?\s*,\s*(\d{1,3})%?.*\)'

    match = ""
    sRgb = ""
    sHsl = ""
    Rgb = []
    sCmt = ""  # commentaire

    # pattern strict Rgb avec % -> 0..255 arrondi
    if re.search(patternStrictRgb, line):
        t, r, g, b = re.findall(patternStrictRgb, line)[0]
        r, g, b = float(r) * 2.55, float(g) * 2.55, float(b) * 2.55
        sRgb = f"{r:3.0f} {g:3.0f} {b:3.0f}"  # arrondi float
        sRgb = sRgb.strip()
        return sRgb

    # pattern strict Hsl $u=$2:deg-grad-rad-turn -> deg
    if re.search(patternStrictHsl, line):
        h, u, s, l = re.findall(patternStrictHsl, line)[0]
        h = float(h)
        if u == 'deg':
            h = 360 * remainder(h, 360.0)
        elif u == 'grad':
            h = 360 * remainder(h * (180.0 / 200.0), 360)
        elif u == 'rad':
            h = 360 * remainder(h * 180.0 / math.pi, 360.0)
        elif u == 'turn':
            h = 360 * remainder(h * 360.0, 360)
        else:  # degré par defaut
            h = 360 * remainder(h, 360.0)
        sRgb = hsl2Rgb(h, s, l)
        sRgb = sRgb.strip()
        return sRgb

    if re.search(patternRgbHsl, line):
        t, r, g, b = re.findall(patternRgbHsl, line)[0]
        r, g, b = int(r), int(g), int(b)
        if t == 'rgb':
            sRgb = f"{r:3d} {g:3d} {b:3d}"
        elif t == 'hsl':  # les positions r g b correspond h s l
            sRgb = hsl2Rgb(r, g, b)
        sRgb = sRgb.strip()
        return sRgb
    else:
        return ""


if __name__ == "__main__":
    print(extract_comment("color:red; /* test */"))
