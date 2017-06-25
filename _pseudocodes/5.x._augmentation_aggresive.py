image_generator = ImageDataGenerator(
	rotation_range = 10.0,    # randomly rotate images
	width_shift_range = 0.2,  # randomly shift images horizontally (fraction of total width)
	height_shift_range = 0.2, # randomly shift images vertically (fraction of total height)
	horizontal_flip = False,  # randomly flip images
	vertical_flip = True,     # randomly flip images
	shear_range=0.2,          # randomly apply shear transformation with this intensity
	zoom_range=0.2,           # range for random zoom
)