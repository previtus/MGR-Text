keys: load_dataset, get_imgs_with_labels, get_input_shape, ResNet50, predict, build_simple_top_model, compile, fit

def img_model_with_feature_cooking():
	dataset = DatasetHandler.load_dataset(path_to_segments_file)
	[images, score, images_val, score_val] = dataset.get_imgs_with_labels(...)

	input_shape = dataset.get_input_shape()
	model_base = ResNet50(weights='imagenet', include_top=False, input_shape=input_shape)

	training_features = model_base.predict(images)
	validation_features = model_base.predict(images_val)

	# here it's possible to split the computation
	# save the training_features, validation_features
	# and load them repeatedly after

	model_top = build_simple_top_model( input_shape=training_features.shape[1:] )
	model_top.compile(...)

	history = model_top.fit(training_features, score, ...
			validation_data=(validation_features, score_val))
