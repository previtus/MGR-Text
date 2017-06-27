keys: experiment_runner, load_settings_from_file, load_dataset, prepare_folders, get_cnn_models, cook_features, get_top_models, save_visualizations, train_models, save_histories, graph_histories, save_report, save_models, send_mail_with_graph, save_metacentrum_report

def experiment_runner(settings_file=None, job_id):
    Settings = SettingsDefaults.load_settings_from_file(settings_file, job_id, verbose=False)

    # preparation
    datasets = ModelOI.load_dataset(Settings)
    Settings = ModelOI.prepare_folders(Settings, datasets, verbose=True)
    models = ModelGenerator.get_cnn_models(Settings)

    # building
    ModelTester.cook_features(models, datasets, Settings)
    models = ModelGenerator.get_top_models(models, datasets, Settings)

    ModelOI.save_visualizations(models, Settings)

    # training
    histories = ModelTester.train_models(models, datasets, Settings)

    # save and report results
    ModelOI.save_histories(histories, Settings) # to .npy files
    ModelOI.graph_histories(histories, Settings) # to png images

    ModelOI.save_report(Settings)
    ModelOI.save_models(models, Settings)

    ModelOI.send_mail_with_graph(Settings)
    ModelOI.save_metacentrum_report(Settings)
