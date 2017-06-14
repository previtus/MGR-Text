keys: ResNet50, VGG16, VGG19, InceptionV3, Xception

# Keras Applications, deep CNN models with weights trained on ImageNet

model = ResNet50(weights='imagenet', include_top=False, input_shape=input_shape)

model = VGG16(weights='imagenet', include_top=False, input_shape=input_shape)

model = VGG19(weights='imagenet', include_top=False, input_shape=input_shape)

model = InceptionV3(weights='imagenet', include_top=False, input_shape=input_shape)

model = Xception(weights='imagenet', include_top=False, input_shape=input_shape)