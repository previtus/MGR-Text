keys: get_data, compile, fit, train_model

def train_model(model, dataset, model_setting):
	[...] = dataset.get_data(...)
	model.compile(...)
	history = model.fit(...)

	return history