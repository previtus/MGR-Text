def train_model(model, dataset, model_setting):
	[...] = dataset.get_data(...)
	model.compile(optimizer, loss, metrics)
	history = model.fit(...)

	return history