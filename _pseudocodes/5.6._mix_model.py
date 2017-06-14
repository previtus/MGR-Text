keys: ResNet50, Model, Input, Dense, Dropout, Flatten, concatenate

from keras.models import Model
from keras.layers import Input, Dense, Dropout, Flatten, concatenate
from keras.applications.resnet50 import ResNet50

def build_full_mixed_model(input_shape_img, input_shape_osm, number_of_repeats):
	model_cnn = ResNet50(input_tensor=input_shape_img, weights='imagenet', include_top=False)
	img_features = Flatten()(model_cnn.output)

	osm_features_input = Input(shape=input_shape_osm)
	osm_features = Dense(256, activation='relu')(osm_features_input)
	osm_features = Dropout(0.5)(osm_features)

	top = concatenate([osm_features, img_features])
	for i in range(0,number_of_repeats):
		top = Dense(256, activation='relu')(top)
		top = Dropout(0.5)(top)
	top = Dense(1, activation='sigmoid')(top)

	model = Model(inputs=[model_cnn.input, osm_features_input], outputs=top)
	return model