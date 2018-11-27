# A.1 2D 그래픽

# A.1.1 표준 라이브러리

import imghdr
imghdr.what('oreilly.png')
# 'png'


# A.1.2 PIL과 Pillow

from PIL import Image
img = Image.open('oreilly.png')
img.format
# 'PNG'
img.size
# (154, 141)
img.mode
# 'RGB'


img.show()


crop = (55, 70, 85, 100)
img2 = img.crop(crop)
img2.show()


img2.save('cropped.gif', 'GIF')
img3 = Image.open('cropped.gif')
img3.format
# 'GIF'
img3.size
# (30, 30)


mustache = Image.open('moustaches.png')
handlebar = mustache.crop( (316, 282, 394, 310) )
handlebar.size
# (78, 28)
img.paste(handlebar, (45, 90) )
img.show()


# A.1.3 ImageMagick

from wand.image import Image
from wand.display import display

img = Image(filename='oreilly.png')
img.size
# (154, 141)
img.format
# 'PNG'


display(img)
