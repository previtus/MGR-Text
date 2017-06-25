image_generator = ImageDataGenerator(
	rotation_range = 10.0,
	width_shift_range = 0.2,
	height_shift_range = 0.2,
	horizontal_flip = False,
	vertical_flip = True,
	shear_range=0.2,
	zoom_range=0.2,   
)
