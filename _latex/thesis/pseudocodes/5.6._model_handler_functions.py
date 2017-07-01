def get_top_models():
	models = []

	for model_setting in Settings["models"]:
		model_type = model_setting["model_type"]
		model = build_img_model / build_osm_model / build_mix_model
		
		models.append( model )
	return models


def train_models():
	histories = []

	for model_setting in Settings["models"]:
		model <- models
		dataset <- datasets

		history = train_model(model, dataset, model_setting)
		histories.append( history )
	return histories