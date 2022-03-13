# @author Christp
# @version 1.0
# @ClassName image_process
# @Description TODO
# @date 2022/3/8 13:04

import PIL.Image


def copy(im):
    im_new = PIL.Image.new(im.mode, im.size)
    width, height = im.size
    for i in range(0, width):
        for j in range(0, height):
            pix = im.getpixel((i, j))
            im_new.putpixel((i, j), pix)
    return im_new


if __name__ == '__main__':
    im = PIL.Image.open("c:/Users/sxy/Pictures/Saved Pictures/sample.jpg")
    copy(im).show()


