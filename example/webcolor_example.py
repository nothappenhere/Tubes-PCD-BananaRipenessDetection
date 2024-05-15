import matplotlib.pyplot as plt
import webcolors

def closest_color(rgb):
    differences = {}
    for color_hex, color_name in webcolors.CSS3_HEX_TO_NAMES.items():
        r, g, b = webcolors.hex_to_rgb(color_hex)
        differences[sum([(r - rgb[0]) ** 2,
                         (r - rgb[1]) ** 2,
                         (r - rgb[2]) ** 2])] = color_name
    return differences[min(differences.keys())]

color = (24, 181, 124)
try:
    cname = webcolors.rgb_to_name(color)
    print(f"Warna persis: {cname}")
except ValueError:
    cname = closest_color(color)
    print(f"Warna mendekati: {cname}")
    
plt.imshow([[color]])
plt.show()
