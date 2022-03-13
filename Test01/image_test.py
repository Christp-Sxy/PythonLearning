# @author Christp
# @version 1.0
# @ClassName image_test
# @Description TODO
# @date 2022/3/8 12:54

import PIL.Image
import PIL.ImageFilter

im = PIL.Image.open("c:/Users/sxy/Pictures/Saved Pictures/sample.jpg")
width, height = im.size

# 创建新图像，大小为原始图像的4倍
newIm = PIL.Image.new(im.mode, (2 * width, 2 * height))

# 左上角：原始图像
newIm.paste(im, (0, 0, width, height))

# 右上角：轮廓过滤
contour = im.filter(PIL.ImageFilter.CONTOUR)
newIm.paste(contour, (width, 0, 2 * width, height))

# 左下角：浮雕过滤
emboss = im.filter(PIL.ImageFilter.EMBOSS)
newIm.paste(emboss, (0, height, width, 2 * height))

# 右下角：边缘过滤
edges = im.filter(PIL.ImageFilter.FIND_EDGES)
newIm.paste(edges, (width, height, 2 * width, 2 * height))

# 显示结果图像
newIm.show()
