import scipy.misc
import PIL.Image

mat = scipy.misc.imread('images/jp.jpg')
print('shape: {}'.format(mat.shape))

# 分解通道
im = PIL.Image.open('images/jp.jpg')
print(im)
r, g, b = im.split()

r.show()
g.show()
b.show()

# 交换通道
im = PIL.Image.merge('RGB', (b, g, r))
im.show()

# 传入自定义通道分量
r = PIL.Image.new('L', (480, 270), color=255)

im = PIL.Image.merge('RGB', (r, g, b))
im.show()
