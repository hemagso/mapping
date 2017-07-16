from keras.models import Model
from keras.layers import Convolution2D, Dense, Dropout, MaxPooling2D, Input, Flatten, ZeroPadding2D
from keras.layers.advanced_activations import PReLU, LeakyReLU
from keras.regularizers import l2
from keras.optimizers import Adam, RMSprop

def architecture_01(verbose=False):
    inputs = Input(shape=(244,244,3))

    x = Convolution2D(64,(3,3), activation="relu", kernel_initializer="uniform")(inputs)
    x = Convolution2D(64,(3,3), activation="relu", kernel_initializer="uniform")(x)
    x = MaxPooling2D((2,2))(x)

    x = Convolution2D(64,(3,3), activation="relu", kernel_initializer="uniform")(x)
    x = Convolution2D(64,(3,3), activation="relu", kernel_initializer="uniform")(x)
    x = MaxPooling2D((2,2))(x)

    x = Convolution2D(128,(3,3), activation="relu", kernel_initializer="uniform")(x)
    x = Convolution2D(128,(3,3), activation="relu", kernel_initializer="uniform")(x)
    x = MaxPooling2D((2,2))(x)

    x = Convolution2D(128,(3,3), activation="relu", kernel_initializer="uniform")(x)
    x = Convolution2D(128,(3,3), activation="relu", kernel_initializer="uniform")(x)
    x = MaxPooling2D((2,2))(x)

    x = Convolution2D(256,(3,3), activation="relu", kernel_initializer="uniform")(x)
    x = Convolution2D(256,(3,3), activation="relu", kernel_initializer="uniform")(x)
    x = MaxPooling2D((2,2))(x)

    x = Convolution2D(512,(3,3), activation="relu", kernel_initializer="uniform")(x)

    x = Flatten()(x)
    x = Dense(1024, activation='relu', kernel_initializer="uniform")(x)
    x = Dropout(0.5)(x)
    x = Dense(1024, activation='relu', kernel_initializer="uniform")(x)
    x = Dropout(0.5)(x)
    outputs = Dense(1)(x)

    model = Model(inputs=inputs, outputs=outputs)

    optimizer = Adam(lr=0.0001)

    model.compile(optimizer=optimizer, loss="mean_absolute_error", metrics=["mse"])
    if verbose:
        model.summary()
    return model, 1

def architecture_02(verbose=False):
    inputs = Input(shape=(244,244,3))

    x = Convolution2D(64,(3,3), activation="relu", kernel_initializer="uniform")(inputs)
    x = Convolution2D(64,(3,3), activation="relu", kernel_initializer="uniform")(x)
    x = MaxPooling2D((2,2))(x)

    x = Convolution2D(128,(3,3), activation="relu", kernel_initializer="uniform")(x)
    x = Convolution2D(128,(3,3), activation="relu", kernel_initializer="uniform")(x)
    x = MaxPooling2D((2,2))(x)

    x = Convolution2D(256,(3,3), activation="relu", kernel_initializer="uniform")(x)
    x = Convolution2D(256,(3,3), activation="relu", kernel_initializer="uniform")(x)
    x = MaxPooling2D((2,2))(x)

    x = Convolution2D(256,(3,3), activation="relu", kernel_initializer="uniform")(x)
    x = Convolution2D(256,(3,3), activation="relu", kernel_initializer="uniform")(x)
    x = MaxPooling2D((2,2))(x)

    x = Convolution2D(512,(3,3), activation="relu", kernel_initializer="uniform")(x)
    x = Convolution2D(512,(3,3), activation="relu", kernel_initializer="uniform")(x)
    x = MaxPooling2D((2,2))(x)

    x = Convolution2D(512,(3,3), activation="relu", kernel_initializer="uniform")(x)

    x = Flatten()(x)
    x = Dense(1024, activation='relu', kernel_initializer="uniform")(x)
    x = Dropout(0.5)(x)
    x = Dense(1024, activation='relu', kernel_initializer="uniform")(x)
    x = Dropout(0.5)(x)
    outputs = Dense(1)(x)

    model = Model(inputs=inputs, outputs=outputs)

    optimizer = Adam(lr=0.0001)

    model.compile(optimizer=optimizer, loss="mean_absolute_error", metrics=["mse"])
    if verbose:
        model.summary()
    return model, 2

def architecture_03(verbose=False):
    inputs = Input(shape=(244,244,3))

    x = Convolution2D(16,(3,3), kernel_initializer="uniform")(inputs)
    x = PReLU()(x)
    x = Convolution2D(16,(3,3), kernel_initializer="uniform")(x)
    x = PReLU()(x)
    x = MaxPooling2D((2,2))(x)

    x = Convolution2D(32,(3,3), kernel_initializer="uniform")(x)
    x = PReLU()(x)
    x = Convolution2D(32,(3,3), kernel_initializer="uniform")(x)
    x = PReLU()(x)
    x = MaxPooling2D((2,2))(x)

    x = Convolution2D(64,(3,3), kernel_initializer="uniform")(x)
    x = PReLU()(x)
    x = Convolution2D(64,(3,3), kernel_initializer="uniform")(x)
    x = PReLU()(x)
    x = MaxPooling2D((2,2))(x)

    x = Convolution2D(128,(3,3), kernel_initializer="uniform")(x)
    x = PReLU()(x)
    x = Convolution2D(128,(3,3), kernel_initializer="uniform")(x)
    x = PReLU()(x)
    x = MaxPooling2D((2,2))(x)

    x = Convolution2D(128,(3,3), kernel_initializer="uniform")(x)
    x = PReLU()(x)
    x = Convolution2D(128,(3,3), kernel_initializer="uniform")(x)
    x = PReLU()(x)
    x = MaxPooling2D((2,2))(x)

    x = Convolution2D(512,(3,3), kernel_initializer="uniform")(x)
    x = PReLU()(x)

    x = Flatten()(x)
    x = Dense(1024, kernel_initializer="uniform")(x)
    x = PReLU()(x)
    x = Dropout(0.5)(x)
    x = Dense(1024, kernel_initializer="uniform")(x)
    x = PReLU()(x)
    x = Dropout(0.5)(x)
    outputs = Dense(1)(x)

    model = Model(inputs=inputs, outputs=outputs)

    optimizer = Adam(lr=0.0001)

    model.compile(optimizer=optimizer, loss="mean_absolute_error", metrics=["mse"])
    if verbose:
        model.summary()
    return model, 3

def architecture_04(verbose=False):
    inputs = Input(shape=(244,244,3))

    x = Convolution2D(64,(3,3), kernel_initializer="uniform")(inputs)
    x = PReLU()(x)
    x = Convolution2D(64,(3,3), kernel_initializer="uniform")(x)
    x = PReLU()(x)
    x = MaxPooling2D((2,2))(x)

    x = Convolution2D(128,(3,3), kernel_initializer="uniform")(x)
    x = PReLU()(x)
    x = Convolution2D(128,(3,3), kernel_initializer="uniform")(x)
    x = PReLU()(x)
    x = MaxPooling2D((2,2))(x)

    x = Convolution2D(256,(3,3), kernel_initializer="uniform")(x)
    x = PReLU()(x)
    x = Convolution2D(256,(3,3), kernel_initializer="uniform")(x)
    x = PReLU()(x)
    x = MaxPooling2D((2,2))(x)

    x = Convolution2D(256,(3,3), kernel_initializer="uniform")(x)
    x = PReLU()(x)
    x = Convolution2D(256,(3,3), kernel_initializer="uniform")(x)
    x = PReLU()(x)
    x = MaxPooling2D((2,2))(x)

    x = Convolution2D(512,(3,3), kernel_initializer="uniform")(x)
    x = PReLU()(x)
    x = Convolution2D(512,(3,3), kernel_initializer="uniform")(x)
    x = PReLU()(x)
    x = MaxPooling2D((2,2))(x)

    x = Convolution2D(512,(3,3), kernel_initializer="uniform")(x)
    x = PReLU()(x)

    x = Flatten()(x)
    x = Dense(1024, kernel_initializer="uniform")(x)
    x = PReLU()(x)
    x = Dropout(0.5)(x)
    x = Dense(1024, kernel_initializer="uniform")(x)
    x = PReLU()(x)
    x = Dropout(0.5)(x)
    outputs = Dense(1)(x)

    model = Model(inputs=inputs, outputs=outputs)

    optimizer = Adam(lr=0.001)

    model.compile(optimizer=optimizer, loss="mean_absolute_error", metrics=["mse"])
    if verbose:
        model.summary()
    return model, 4

def architecture_05(verbose=False):
    inputs = Input(shape=(244,244,3))

    x = Convolution2D(64,(3,3), kernel_initializer="uniform")(inputs)
    x = LeakyReLU(alpha=0.1)(x)
    x = Convolution2D(64,(3,3), kernel_initializer="uniform")(x)
    x = LeakyReLU(alpha=0.1)(x)
    x = MaxPooling2D((2,2))(x)

    x = Convolution2D(64,(3,3), kernel_initializer="uniform")(x)
    x = LeakyReLU(alpha=0.01)(x)
    x = Convolution2D(64,(3,3), kernel_initializer="uniform")(x)
    x = LeakyReLU(alpha=0.1)(x)
    x = MaxPooling2D((2,2))(x)

    x = Convolution2D(128,(3,3), kernel_initializer="uniform")(x)
    x = LeakyReLU(alpha=0.1)(x)
    x = Convolution2D(128,(3,3), kernel_initializer="uniform")(x)
    x = LeakyReLU(alpha=0.1)(x)
    x = MaxPooling2D((2,2))(x)

    x = Convolution2D(128,(3,3), kernel_initializer="uniform")(x)
    x = LeakyReLU(alpha=0.1)(x)
    x = Convolution2D(128,(3,3), kernel_initializer="uniform")(x)
    x = LeakyReLU(alpha=0.1)(x)
    x = MaxPooling2D((2,2))(x)

    x = Convolution2D(256,(3,3), kernel_initializer="uniform")(x)
    x = LeakyReLU(alpha=0.1)(x)
    x = Convolution2D(256,(3,3), kernel_initializer="uniform")(x)
    x = LeakyReLU(alpha=0.1)(x)
    x = MaxPooling2D((2,2))(x)

    x = Convolution2D(512,(3,3), kernel_initializer="uniform")(x)
    x = LeakyReLU(alpha=0.1)(x)

    x = Flatten()(x)
    x = Dense(1024, kernel_initializer="uniform")(x)
    x = LeakyReLU(alpha=0.1)(x)
    x = Dropout(0.5)(x)
    x = Dense(1024, kernel_initializer="uniform")(x)
    x = LeakyReLU(alpha=0.1)(x)
    x = Dropout(0.5)(x)
    outputs = Dense(1)(x)

    model = Model(inputs=inputs, outputs=outputs)

    optimizer = Adam(lr=0.0001)

    model.compile(optimizer=optimizer, loss="mean_absolute_error", metrics=["mse"])
    if verbose:
        model.summary()
    return model, 5

def architecture_06(verbose=False):
    inputs = Input(shape=(244,244,3))

    x = Convolution2D(64,(3,3), kernel_initializer="uniform")(inputs)
    x = LeakyReLU(alpha=0.2)(x)
    x = Convolution2D(64,(3,3), kernel_initializer="uniform")(x)
    x = LeakyReLU(alpha=0.2)(x)
    x = MaxPooling2D((2,2))(x)

    x = Convolution2D(64,(3,3), kernel_initializer="uniform")(x)
    x = LeakyReLU(alpha=0.2)(x)
    x = Convolution2D(64,(3,3), kernel_initializer="uniform")(x)
    x = LeakyReLU(alpha=0.2)(x)
    x = MaxPooling2D((2,2))(x)

    x = Convolution2D(128,(3,3), kernel_initializer="uniform")(x)
    x = LeakyReLU(alpha=0.2)(x)
    x = Convolution2D(128,(3,3), kernel_initializer="uniform")(x)
    x = LeakyReLU(alpha=0.2)(x)
    x = MaxPooling2D((2,2))(x)

    x = Convolution2D(128,(3,3), kernel_initializer="uniform")(x)
    x = LeakyReLU(alpha=0.2)(x)
    x = Convolution2D(128,(3,3), kernel_initializer="uniform")(x)
    x = LeakyReLU(alpha=0.2)(x)
    x = MaxPooling2D((2,2))(x)

    x = Convolution2D(256,(3,3), kernel_initializer="uniform")(x)
    x = LeakyReLU(alpha=0.2)(x)
    x = Convolution2D(256,(3,3), kernel_initializer="uniform")(x)
    x = LeakyReLU(alpha=0.2)(x)
    x = MaxPooling2D((2,2))(x)

    x = Convolution2D(512,(3,3), kernel_initializer="uniform")(x)
    x = LeakyReLU(alpha=0.2)(x)

    x = Flatten()(x)
    x = Dense(1024, kernel_initializer="uniform")(x)
    x = LeakyReLU(alpha=0.2)(x)
    x = Dropout(0.5)(x)
    x = Dense(1024, kernel_initializer="uniform")(x)
    x = LeakyReLU(alpha=0.2)(x)
    x = Dropout(0.5)(x)
    outputs = Dense(1)(x)

    model = Model(inputs=inputs, outputs=outputs)

    optimizer = Adam(lr=0.0001)

    model.compile(optimizer=optimizer, loss="mean_absolute_error", metrics=["mse"])
    if verbose:
        model.summary()
    return model, 6

def architecture_07(verbose=False):
    inputs = Input(shape=(512,512,3))

    x = ZeroPadding2D((1,1))(inputs)
    x = Convolution2D(64,(3,3), kernel_initializer="glorot_uniform", activation="relu")(x)
    x = ZeroPadding2D((1,1))(x)
    x = Convolution2D(64,(3,3), kernel_initializer="glorot_uniform", activation="relu")(x)
    x = MaxPooling2D((2,2),strides=(2,2))(x)

    x = ZeroPadding2D((1,1))(x)
    x = Convolution2D(64,(3,3), kernel_initializer="glorot_uniform", activation="relu")(x)
    x = ZeroPadding2D((1,1))(x)
    x = Convolution2D(64,(3,3), kernel_initializer="glorot_uniform", activation="relu")(x)
    x = MaxPooling2D((2,2),strides=(2,2))(x)

    x = ZeroPadding2D((1,1))(x)
    x = Convolution2D(64,(3,3), kernel_initializer="glorot_uniform", activation="relu")(x)
    x = ZeroPadding2D((1,1))(x)
    x = Convolution2D(64,(3,3), kernel_initializer="glorot_uniform", activation="relu")(x)
    x = MaxPooling2D((2,2),strides=(2,2))(x)

    x = ZeroPadding2D((1,1))(x)
    x = Convolution2D(128,(3,3), kernel_initializer="glorot_uniform", activation="relu")(x)
    x = ZeroPadding2D((1,1))(x)
    x = Convolution2D(128,(3,3), kernel_initializer="glorot_uniform", activation="relu")(x)
    x = MaxPooling2D((2,2),strides=(2,2))(x)

    x = ZeroPadding2D((1,1))(x)
    x = Convolution2D(128,(3,3), kernel_initializer="glorot_uniform", activation="relu")(x)
    x = ZeroPadding2D((1,1))(x)
    x = Convolution2D(128,(3,3), kernel_initializer="glorot_uniform", activation="relu")(x)
    x = MaxPooling2D((2,2),strides=(2,2))(x)

    x = ZeroPadding2D((1,1))(x)
    x = Convolution2D(128,(3,3), kernel_initializer="glorot_uniform", activation="relu")(x)
    x = ZeroPadding2D((1,1))(x)
    x = Convolution2D(128,(3,3), kernel_initializer="glorot_uniform", activation="relu")(x)
    x = MaxPooling2D((2,2),strides=(2,2))(x)

    x = ZeroPadding2D((1,1))(x)
    x = Convolution2D(256,(3,3), kernel_initializer="glorot_uniform", activation="relu")(x)
    x = ZeroPadding2D((1,1))(x)
    x = Convolution2D(256,(3,3), kernel_initializer="glorot_uniform", activation="relu")(x)
    x = MaxPooling2D((2,2),strides=(2,2))(x)

    x = ZeroPadding2D((1,1))(x)
    x = Convolution2D(256,(3,3), kernel_initializer="glorot_uniform", activation="relu")(x)
    x = ZeroPadding2D((1,1))(x)
    x = Convolution2D(256,(3,3), kernel_initializer="glorot_uniform", activation="relu")(x)
    x = MaxPooling2D((2,2),strides=(2,2))(x)

    x = ZeroPadding2D((1,1))(x)
    x = Convolution2D(256,(3,3), kernel_initializer="glorot_uniform", activation="relu")(x)
    x = ZeroPadding2D((1,1))(x)
    x = Convolution2D(256,(3,3), kernel_initializer="glorot_uniform", activation="relu")(x)
    x = MaxPooling2D((2,2),strides=(2,2))(x)

    x = Flatten()(x)
    x = Dense(1024, kernel_initializer="glorot_uniform", activation="relu")(x)
    x = Dropout(0.5)(x)
    x = Dense(1024, kernel_initializer="glorot_uniform", activation="relu")(x)
    x = Dropout(0.5)(x)
    outputs = Dense(1)(x)

    model = Model(inputs=inputs, outputs=outputs)

    optimizer = Adam(lr=0.0001)

    model.compile(optimizer=optimizer, loss="mean_absolute_error", metrics=["mse"])
    if verbose:
        model.summary()
    return model, 7

    