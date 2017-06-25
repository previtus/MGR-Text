image_generator = ImageDataGenerator(
	rotation_range = 0,  # randomly rotate images in the range (degrees, 0 to 180)
	width_shift_range = 0.1,  # randomly shift images horizontally (fraction of total width)
	height_shift_range = 0.1,  # randomly shift images vertically (fraction of total height)
	horizontal_flip = False,  # randomly flip images
	vertical_flip = True  # randomly flip images
)