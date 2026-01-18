from datetime import datetime
import os
import numpy as np
import re
import math
'''
from gi.repository import GLib
from gi.repository import GimpUi
from gi.repository import Gimp
'''
import sys
'''
import gi
gi.require_version('Gimp', '3.0')
gi.require_version('GimpUi', '3.0')
'''


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

'''
# extract comment at line end and trim left and right
'''
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
# param: ligne en cours du fichier CSS
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
# si s=0 alors
    r = g = b = l * 255.0

    if s != 0.0:
        var_2 = l * (1.0 + s) if l < 0.5 else (l + s) - (s * l)
        # q = l * (1 + s) if l < 0.5 else l + s - l * s
        var_1 = 2.0 * l - var_2
        # p = 2 * l - q
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
    h = h % 1
    while h < 0.0:
        h += 1.0
    while h > 1.0:
        h -= 1.0
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
    # en CSS4 la virgule est facultative par exemple: rgb(R% G% B% / A)
    patternStrictRgb = r'(rgb)a?\(\s*(\d{1,3})%\s*,?\s*(\d{1,3})%\s*,?\s*(\d{1,3})%.*\)'
    # ajout de ? apres deg|grad|rad|turn car cette unité est optionnelle
    patternStrictHsl = r'(?:hsl)a?\(\s*(\d*?\.?\d*)(deg|grad|rad|turn)?\s*,\s*(\d{1,3})%\s*,\s*(\d{1,3})%.*\)'
    # admet un nombre decimal pour le hsl comme 0.5 ou .5 ou 100.0 et les nombres entiers
    patternRgbHsl = r'(rgb|hsl)a?\(\s*(\d{0,3}(?:\.\d*)?)\s*,\s*(\d{1,3})%?\s*,\s*(\d{1,3})%?.*\)'
    # ancienne version:
    # patternRgbHsl = r'(rgb|hsl)a?\(\s*(\d{1,3})\s*,\s*(\d{1,3})%?\s*,\s*(\d{1,3})%?.*\)'
    match = ""
    sRgb = ""
    sHsl = ""
    Rgb = []
    sCmt = ""  # commentaire

    # pattern strict Rgb avec % sur tout les composants meme 0% -> 0..255 arrondi
    if re.search(patternStrictRgb, line):
        t, r, g, b = re.findall(patternStrictRgb, line)[0]
        r, g, b = float(r) * 2.55, float(g) * 2.55, float(b) * 2.55
        sRgb = f"{r:3.0f} {g:3.0f} {b:3.0f}"  # arrondi float
        sRgb = sRgb.strip()
        return sRgb

    # pattern strict Hsl $u=$2:deg-grad-rad-turn -> deg
    if re.search(patternStrictHsl, line):
        h, u, s, l = re.findall(patternStrictHsl, line)[0]
        h, s, l = float(h), float(s), float(l)
        if u == 'deg':
            # h = 360 * remainder(h, 360.0)
            h = h % 360.0
        elif u == 'grad':
            # h = 360 * remainder(h * (180.0 / 200.0), 360)
            h = h * (180.0 / 200.0) % 360.0
        elif u == 'rad':
            # h = 360 * remainder(h * 180.0 / math.pi, 360.0)
            h = h * (180.0 / math.pi) % 360.0
        elif u == 'turn':
            # h = 360 * remainder(h * 360.0, 360)
            h = h * 360.0 % 360
        else:  # degré par defaut
            # h = 360 * remainder(h, 360.0)
            h = h % 360.0
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

'''
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
# Conversion valeurs hexadecimales to RGB
# param: code hexadecimal de la couleur
# return: le format GPL de la couleur
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''
def hexa2rgb(hexa):
    rgb = []
    sRgb = ""
    if len(hexa) == 6:
        rgb.extend([hexa[i:i+2] for i in range(0, 6, 2)])
    elif len(hexa) == 3:
        rgb.extend([hexa[i] * 2 for i in range(3)])
    else:
        return sRgb

    for value in rgb:
        sRgb += f"{int(value, 16):03d} "

    sRgb = sRgb.strip()
    return sRgb
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
# Converti le rgb format gpl en hexa pour l'inclure dans le commentaire
# param: le color rgb 255 255 255 format gpl
# return: en format hexa ABCDEF
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


def rgb2hexa(rgb):
    # Remove leading zeros from each component
    rgb = re.sub(r'(?:0{0,2})(\d+)', r'\1', rgb)
    r, g, b = map(int, rgb.split())
    hexa = f"{r:02X}{g:02X}{b:02X}"  # Format as 2-digit hexadecimal
    return hexa

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
# Converti rgb en hsv (HSV Hue Saturation Value ou  TSV Teinte Saturation Valeur)
# Pour faire un tri sur h,s ou v
# param: le color rgb 255 255 255 format gpl
# return: une liste (h,s,v)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


def rgb2hsv(rgb):
    red, green, blue = rgb
    rgbs = sorted([red, green, blue])
    minc, maxc = rgbs[0], rgbs[-1]
    v = maxc / 255.0
    if minc == maxc:
        return (0.0, 0.0, round(v * 100, 1))
    deltac = maxc - minc
    s = deltac / maxc
    # Calcul de la teinte (Hue)
    if deltac == 0:
        h = 0  # Teinte indéfinie pour les couleurs grises (delta=0)
    elif maxc == red:
        h = 60 * (((green - blue) / deltac) % 6)
    elif maxc == green:
        h = 60 * (((blue - red) / deltac) + 2)
    else:  # c_max == blue
        h = 60 * (((red - green) / deltac) + 4)

    if h < 0:
        h += 360
    h = round(h, 1)
    s = round(s * 100, 1)
    v = round(v * 100, 1)
    return (h, s, v)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
# Ouvre en lecture le fichier CSS à analyser
# param: nom du fichier
# return:
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# A TESTER attendre GIMP 3.0


def loadfilecss(f):
    if f is not None:
        print(f"\nsearching file : {os.path.basename(f)}\n")
        try:
            with open(f, "r") as fcss:
                print(f"open file {f}\n")
                """ gimp_message(f) # debug """
        except IOError as e:
            raise Exception(
                f"failed to open file {f}: {e}")
    else:
        raise Exception("file name css unknown.")

'''
class css2gplPlugin(Gimp.Plugin):
    def run(self, procedure, run_mode, image, drawables, config, run_data):
        # some coding ... LeKiwiDeBx [°}< Couak !!!
        return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, GLib.Error())

Gimp.main(css2gplPlugin.__gtype__, sys.argv)
'''

# if __name__ == "__main__":
#     print(extract_comment("color:red; /* test */"))

# Write a class named css2gpl to call in CLI with one prameter
# the parameter is the css file path

class css2gpl:

    def __init__(self, css_file):
        self.css_file = css_file
    def doLineGPL(self, color, comment):
            # Step 1: Remove leading zeros from numbers (e.g., "000 255 080" -> " 0 255 80")
            # The regex (?:0{0,2})(\d+) matches 0, 1, or 2 zeros followed by digits.
            # We replace it with a space followed by the captured digits ($1).
            # re.sub is used with the pattern and replacement string.
        color = re.sub(r'(?:0{0,2})(\d+)\s*', r' \1', color)
            # Step 2: Remove leading and trailing whitespace
            # .strip() is the Python equivalent of s/^\s+|\s+$//g
        color = color.strip()
            # Check if the color key does not exist in the dictionary
        if color not in ColorComment:
            # If it doesn't exist, create a new entry with the hex value and comment
            ColorComment[color] = rgb2hexa(color) + " " + comment
        else:
            # If it exists, append the new comment to the existing value
            ColorComment[color] += " " + comment
        # Split the color string by whitespace to get r, g, b values
        r, g, b = color.split()

        # Reverse the IDlistNameColor dictionary to map hex codes to color names
        # Note: This assumes IDlistNameColor is defined elsewhere in the code
        rIDlistNameColor = {v: k for k, v in IDlistNameColor.items()}

        # Convert the current color to hex format
        hex_color = rgb2hexa(color)

        # Check if the hex color exists in the reversed dictionary (i.e., is a named color)
        if hex_color in rIDlistNameColor:
            # Retrieve the existing comment for this color
            comment_data = ColorComment[color]
            
            # Extract the hex code and the rest of the comment using regex
            # Pattern: 6 hex digits followed by space and any characters
            match = re.match(r'([0-9A-Fa-f]{6})\s(.*)', comment_data)
            
            if match:
                extracted_hex = match.group(1)
                extracted_comment = match.group(2)
                color_name = rIDlistNameColor[hex_color]
                
                # Format the line: "R   G   B HEX NAME COMMENT"
                # %-20s left-aligns the name in a 20-char field
                # %-48.48s left-aligns and truncates the comment to 48 chars
                line_gpl = "%3d %3d %3d %s %-20s %-48.48s" % (
                    int(r), int(g), int(b), 
                    extracted_hex, 
                    color_name, 
                    extracted_comment
                )
                return line_gpl
        else:
            # If it's not a named color, format the line: "R   G   B HEX COMMENT"
            return "%3d %3d %3d %s" % (int(r), int(g), int(b), ColorComment[color])

        return
        

    def process(self):
        try:
            with open(self.css_file, "r") as fcss:
                print(f"Processing file: {self.css_file}\n")
                
                for line in fcss:
                    hexa = extract_hexa_list(line)
                    if hexa:
                        rgb = hexa2rgb(hexa)
                        print(f"Hex: #{hexa} -> RGB: {rgb}")
                        # write doLineGPL equivalent 
                    if extractRgbHsl(line) != '':
                        rgb_hsl = extractRgbHsl(line)
                        print(f"Extracted RGB/HSL to RGB: {rgb_hsl}")
                    color_names = extract_color_named(line)
                    if color_names:
                        for color_name in color_names:
                            print(f"Extracted color name: {color_name}")
                            rgb = color_name2rgb(color_name)
                            print(f"Color name: {color_name} -> RGB: {rgb}")
                       
        except IOError as e:
            print(f"failed to open file {self.css_file}: {e}")

 #   End of css2gpl class
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python css2gpl.py <css_file>")
        sys.exit(1)

    css_file = sys.argv[1]
    converter = css2gpl(css_file)
    converter.process()

