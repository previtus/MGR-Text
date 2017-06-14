keys: Input, Dense, Dropout, Model, build_osm_only_model

from keras.models import Model
from keras.layers import Input, Dense, Dropout

def build_osm_only_model(input_shape, model_depth, model_width=256):
    osm_features_input = Input(shape=input_shape)
    top = Dense(model_width, activation='relu')(osm_features_input)
    top = Dropout(0.5)(top)
    for i in range(0,model_depth-1):
        top = Dense(model_width, activation='relu')(top)
        top = Dropout(0.5)(top)
    output = Dense(1, activation='sigmoid')(top)

    model = Model(inputs=osm_features_input, outputs=output)
    return model
