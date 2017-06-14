keys: load_dataset, get_imgs_with_labels, get_input_shape, build_generic_model, save_history, visualize_history


def run_generic_experiment():
	dataset = DatasetHandler.load_dataset(path_to_segments_file)
	[images, score, images_val, score_val] = dataset.get_imgs_with_labels(...)
	
	input_shape = dataset.get_input_shape()
	model = ModelHandler.build_generic_model(input_shape)

	model.compile(optimizer, loss, metrics)
	# optimizer, loss, metrics,
	# epochs, batch_size are loaded from Settings

	history = model.fit(images, score, epochs, batch_size,
			validation_data=(images_val, score_val))

	ModelOI.save_history( history )
	ModelOI.visualize_history( history )