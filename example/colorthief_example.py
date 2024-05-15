from colorthief import ColorThief
import matplotlib.pyplot as plt
import colorsys

def dominant_color():
    ct = ColorThief("img/cavendish/1373px-Cavendish_banana1.jpg")
    
    pallete = ct.get_palette(color_count=5)
    plt.imshow([[pallete[i] for i in range(5)]])

    for color in pallete:
        print(f"RGB COLOR: {color}")
        print(f"HEX COLOR: #{color[0]:02x}{color[1]:02x}{color[2]:02x}")
        print(f"HSV COLOR: {colorsys.rgb_to_hsv(*color)}")
        print(f"HLS COLOR: {colorsys.rgb_to_hls(*color)}\n")

    # plt.imshow([[dominant_color]])
    plt.show()

dominant_color()

