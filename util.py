from colorthief import ColorThief
import numpy as np
import cv2

def normalize_image(image):
    """Normalizes the image by setting the minimum pixel value to 0 and the maximum pixel value to 1."""
    # Find the minimum and maximum pixel values
    min_val = np.min(image)
    max_val = np.max(image)

    # Normalize the image
    normalized_image = (image - min_val) / (max_val - min_val) * 255
    return normalized_image.astype(np.uint8)

def gaussian_filter(image):
    gaussian_kernel = (1.0 / 345) * np.array([
                                            [1, 5,  7,  5,  1],
                                            [5, 20, 33, 20, 5],
                                            [7, 33, 55, 33, 7],
                                            [5, 20, 33, 20, 5],
                                            [1, 5,  7,  5,  1]
                                            ])
    result = cv2.filter2D(image, -1, gaussian_kernel)
    return result

def noise_reduction(image):
    # Mendefinisikan kernel kustom
    box_filter_kernel = np.array([
                            [1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]]) / 9  # Normalisasi agar total kernel menjadi 1
    # Menerapkan konvolusi dengan kernel kustom
    smoothed_image = cv2.filter2D(image, -1, box_filter_kernel)
    return smoothed_image

def sharpening_image(image):
    laplacian_kernel = np.array([
                                [0, -1, 0],
                                [-1, 5, -1],
                                [0, -1, 0]
                                ])
    result = cv2.filter2D(image, -1, laplacian_kernel)
    return result

def opening_image(binary_img, strel):
    try:
        # MORPH_OPEN (erosi diikuti dilasi)
        opening_img = cv2.morphologyEx(binary_img, cv2.MORPH_OPEN, strel)
        return opening_img
    except Exception as e:
        print("Error in opening_image:", e)
        return None

def closing_image(binary_img, strel):
    try:
        # MORPH_CLOSE (dilasi diikuti erosi)
        closing_img = cv2.morphologyEx(binary_img, cv2.MORPH_CLOSE, strel)
        return closing_img
    except Exception as e:
        print("Error in closing_image:", e)
        return None

def dominant_color(image):
    ct = ColorThief(image)
    palette = ct.get_palette(color_count=5)
    return palette

'''
# def opening_image(image, strel):
#     try:
#         # Konversi ke grayscale
#         gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
#         # Thresholding
#         _, binary_img = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
        
#         # MORPH_OPEN (erosi diikuti dilasi)
#         opening_image = cv2.morphologyEx(binary_img, cv2.MORPH_OPEN, strel)
#     except:
#         erosi_image = cv2.erode(image, strel, iterations=1)
#         dilasi_image = cv2.dilate(erosi_image, strel, iterations=1)
#         return dilasi_image

# def closing_image(image, strel):
#     try:
#         # Konversi ke grayscale
#         gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#         # Thresholding
#         _, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
        
#         # MORPH_CLOSE (dilasi diikuti erosi)
#         closing_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, strel)
#     except:
#         dilasi_image = cv2.dilate(image, strel, iterations=1)
#         erosi_image = cv2.erode(dilasi_image, strel, iterations=1)
#         return erosi_image
'''

'''
# def get_limits(color):
#     c = np.uint8([[color]])  # BGR values
#     hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

#     hue = hsvC[0][0][0]  # Get the hue value

#     # Handle red hue wrap-around
#     if hue >= 165:  # Upper limit for divided red hue
#         lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
#         upperLimit = np.array([180, 255, 255], dtype=np.uint8)
#     elif hue <= 15:  # Lower limit for divided red hue
#         lowerLimit = np.array([0, 100, 100], dtype=np.uint8)
#         upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)
#     else:
#         lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
#         upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)

#     return lowerLimit, upperLimit
'''
