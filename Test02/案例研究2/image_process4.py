# @author Christp
# @version 1.0
# @ClassName image_process4.py
# @Description TODO
# @date 2022/3/8 13:14
import PIL.Image

if __name__ == "__main__":
    im = PIL.Image.open("c:/Users/sxy/Pictures/Saved Pictures/sample.jpg")
    im.rotate(90).show()
    im.rotate(-90).show()
