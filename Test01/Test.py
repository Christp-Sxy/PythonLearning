# @author Christp
# @version 1.0
# @ClassName Test
# @Description TODO
# @date 2022/3/8 12:42

import PIL
from PIL import Image

im = PIL.Image.open("c:/Users/sxy/Pictures/Saved Pictures/sample.jpg")
im.show()
print(im.format, im.size, im.mode)
