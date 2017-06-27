from PIL import Image
import numpy as np
# from matplotlib import pyplot as plt
from scipy import misc

img = Image.open('D:/test2.jpg')
img2_url = 'D:/test31.jpg'

print(img.size)
print(img.mode)
print(img.format)


# img.show()

'''
img = img.convert("L")
data = img.getdata()
data = np.matrix(data)
data = np.reshape(data, img.size)
new_img = Image.fromarray(data)


print(new_img.size)
print(new_img.mode)
print(new_img.format)

new_img.show()

new_img = np.array(img)
'''
img = img.resize((200, 200))
for i in range(1):
    img.save(img2_url, quality=8)
img2 = Image.open(img2_url)
new_img = np.array(img2)
print(img2.size[0]*img2.size[1])
rows, cols, channels = new_img.shape
print(rows, cols, channels)
set_number = 0.4
set_for = 20
for i in range(set_for):
    for r in range(rows):
        for c in range(cols):
            # R = new_img.item(r, c, 0)
            # G = new_img.item(r, c, 1)
            # B = new_img.item(r, c, 2)
            #
            # Y = (77*R + 150*G + 29*B) >> 8
            # U = (-43*R - 85*G + 128*B) >> 8 - 1
            # V = (128*R - 107*G - 21*B) >> 8 - 1
            #
            # R = (65536*Y + 91881*V) >> 16
            # G = (65536*Y - 22553*U - 46802*V) >> 16
            # B = (65536*Y + 116130*U) >> 16

            R = new_img.item(r, c, 0)
            G = new_img.item(r, c, 1)
            B = new_img.item(r, c, 2)

            Y = 0.299*R + 0.587*G + 0.114*B
            U = -0.147*R - 0.289*G + 0.436*B - set_number
            V = 0.615*R - 0.515*G - 0.100*B - set_number

            R = Y + 1.14*V
            G = Y - 0.39*U - 0.58*V
            B = Y + 2.03*U

            new_img.itemset((r, c, 0), R)
            new_img.itemset((r, c, 1), G)
            new_img.itemset((r, c, 2), B)
'''
new = np.reshape(new_img, (rows, cols))
'''
# plt.imshow(new_img)
# # plt.show()
#
# plt.axis('off')
# plt.savefig(img2_url)
# img3 = Image.open(img2_url)
#
# img3.crop(((img3.size[0]-img.size[0])/2, (img3.size[1]-img.size[1])/2, img.size[0], img.size[1])).save(img2_url)

misc.imsave(img2_url, new_img)
