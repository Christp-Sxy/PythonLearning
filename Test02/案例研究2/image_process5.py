# @author Christp
# @version 1.0
# @ClassName image_process5.py
# @Description TODO
# @date 2022/3/8 13:14

import PIL.Image


def smooth(im):
    width, height = im.size
    im_new = PIL.Image.new(im.mode, im.size)
    for i in range(1, width - 1):
        for j in range(1, height - 1):
            pix_R = 0
            pix_G = 0
            pix_B = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    pix_R += im.getpixel((i + x, j + y))[0] / 9
                    pix_G += im.getpixel((i + x, j + y))[1] / 9
                    pix_B += im.getpixel((i + x, j + y))[2] / 9
            im_new.putpixel((i, j), (int(pix_R), int(pix_G), int(pix_B)))
    return im_new


im = PIL.Image.open("c:/Users/sxy/Pictures/Saved Pictures/sample.jpg")
smooth(im).show()
