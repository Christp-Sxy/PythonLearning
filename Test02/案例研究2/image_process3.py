# @author Christp
# @version 1.0
# @ClassName image_process3.py
# @Description TODO
# @date 2022/3/8 13:13
import PIL.Image


def flip(im, orient='H'):
    width, height = im.size
    im_new = PIL.Image.new(im.mode, im.size)
    for i in range(0, width):
        for j in range(0, height):
            pix = im.getpixel((i, j))
            if orient == 'H':
                im_new.putpixel((width-1-i, j), pix)
            else:
                im_new.putpixel((i, height-1-j), pix)
    return im_new

im = PIL.Image.open("c:/Users/sxy/Pictures/Saved Pictures/sample.jpg")
flip(im, 'H').show()
flip(im, 'V').show()