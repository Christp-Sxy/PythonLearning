# @author Christp
# @version 1.0
# @ClassName image_process2.py
# @Description TODO
# @date 2022/3/8 13:13
import PIL.Image


def crop(im, box):
    x1, y1, x2, y2 = box
    width, height = x2 - x1, y2 - y1
    im_new = PIL.Image.new(im.mode, (width, height))
    for i in range(0, width-1):
        for j in range(0, height-1):
            pix = im.getpixel((x1 + i, y1 + j))
            im_new.putpixel((i, j), pix)
    return im_new


im = PIL.Image.open("c:/Users/sxy/Pictures/Saved Pictures/sample.jpg")
box = (800, 600, 850, 700)
crop(im, box).show()

