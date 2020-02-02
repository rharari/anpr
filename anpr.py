import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

import skimage.io as io
import skimage.color as color
from skimage.util import crop
from skimage.filters import (gaussian, threshold_otsu)
from skimage.segmentation import clear_border
from skimage.morphology import closing, square
from skimage.measure import regionprops, label

# plot image
def print_img(img):
    plt.imshow(img)
    plt.show()

# TODO: implement this fun
def apply_ocr(img):
    print("TODO: call ocr over image")


# load the image
img = io.imread('car1.png')
width, height, deep = img.shape
print_img(img)

# transform to greyscale colorspace
img_grey = color.rgb2grey(img)
print_img(img_grey)

# reduce noise
img_reduced = gaussian(img_grey, 5)
print_img(img_reduced)

# returns a single intensity threshold that separate pixels into two classes, foreground and background.
img_thresh = threshold_otsu(img_reduced)

# remove small dark spots and connect small bright cracks - “close” up dark gaps between bright features.
img_bw = closing(img_grey > img_thresh, square(5))
print_img(img_bw)

# clear objects connected to the label image border.
img_no_border = clear_border(img_bw)
print_img(img_no_border)

# label connected regions of an integer array.
# two pixels are connected when they are neighbors and have the same value
img_label = label(img_no_border)

# iterate each region
for region in regionprops(img_label):
    # filter for large areas - this depends on image resolution
    if region.area >= 1800:
        y1, x1, y2, x2 = region.bbox
        # get rectangle from original image
        img_crop = img[y1:y2, x1:x2]
        print_img(img_crop)
        # apply ocr to cropped image
        apply_ocr(img_crop)

