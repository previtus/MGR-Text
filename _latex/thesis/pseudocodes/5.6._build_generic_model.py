from keras.models import Model
from keras.layers import Input, Dense, Dropout

def build_generic_model(input_shape):
# part of ModelHandler
	input = Input(shape=input_shape)
	x = Dense(256, activation='relu')(input)
	x = Dropout(0.5)(x)
	... # more layers defined

	output = Dense(1, activation='sigmoid')(x)
	model = Model(inputs=input, outputs=output)
	return model