from PIL import Image

algebra_campus_photo = Image.open('photo/Algebra_campus.jpg')

# print(algebra_campus_photo.size)
# algebra_campus_photo.show()

# algebra_campus_photo_transpose = algebra_campus_photo.transpose(Image.ROTATE_270)
# algebra_campus_photo_transpose.show()

# algebra_campus_photo_convert= algebra_campus_photo_transpose.convert(mode='L')
# algebra_campus_photo_convert.show()

r, g, b, = algebra_campus_photo.split()
algebra_campus_photo= Image.merge("RGB", (b, g, r))
algebra_campus_photo.show()