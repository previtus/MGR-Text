keys: Setup
def Setup(Settings,DefaultModel):
	# minimal_model.py
	Settings["experiment_name"] = "minimalExperiment"
	# specifies the name of this experiment as well as folder name where the results will be stored 
	Settings["models"][0]["dataset_name"] = "5556x_reslen30_640px"
	# specifies the folder name of dataset we want to use
	Settings["models"][0]["epochs"] = 50
	# the number of epochs we want to train our model for. Default value is 150
	return Settings