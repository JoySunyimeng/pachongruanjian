from PIL import Image, ImageFilter

Im = Image.open(r'img.jpeg')
# 应用模糊滤镜:
im2 = Im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')

Im.rotate(90).save('rotate90.png')

#'''逆时针旋转180度的新Image图像'''
Im.rotate(180).save('rotate180.png')

#'''逆时针旋转270度的新Image图像'''
Im.rotate(270).save('rotate270.png')
