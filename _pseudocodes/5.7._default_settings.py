keys: append, Setup
DefaultSettings = {}
DefaultModel = {}
# . . . specifying default values
DefaultSettings[“models”] = []
DefaultSettings[“models”].append(DefaultModel)
# DefaultSetting contains settings applicable for the whole experiment
# Each item in list of DefaultSettings[“models”] contains specific setting for one individual model

# load Setup function from a file
Settings = Setup(DefaultSettings, DefaultModel)