'''Trains a simple deep NN on the MNIST dataset.

Gets to 98.40% test accuracy after 20 epochs
(there is *a lot* of margin for parameter tuning).
2 seconds per epoch on a K520 GPU.
'''

from __future__ import print_function
import numpy as np
np.random.seed(1337)  # for reproducibility

from keras.datasets import mnist
from keras.layers import Input, Dense, Activation, Dropout

from keras.models import Model
from keras.utils import np_utils

# /*class NewLayer(Layer):
#     def __init__(selfself, output_dim, **kwargs):
#         self.output_dim = output_dim
#         super(MyLayer, self).__init__(**kwargs)
#
#     def build(self, input_shape):
#         self.W = self.add_wight (shape=(input_shape[1], self.output_dim),
#                                  initializer='random_unifrom')

batch_size = 128
nb_classes = 10
nb_epoch = 20

# the data, shuffled and split between train and test sets
(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(60000, 784)
X_test = X_test.reshape(10000, 784)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255
print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
Y_train = np_utils.to_categorical(y_train, nb_classes)
Y_test = np_utils.to_categorical(y_test, nb_classes)

inputs = Input(shape=(784,))
x = inputs


n_hidden_layers=input("Enter number of units:")
for i in (1,n_hidden_layers):
    x = Dense(128)(x)
    x = Activation('elu')(x)
    x = Dropout(0.3)(x)





predictions = Dense(nb_classes, activation='softmax')(x)
    
model = Model(input=inputs, output=predictions)
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.summary()



history = model.fit(X_train, Y_train,
                    batch_size=batch_size, nb_epoch=nb_epoch,
                    verbose=1, validation_data=(X_test, Y_test))
score = model.evaluate(X_test, Y_test, verbose=0)

print('Test score:', score)
print('Test accuracy:', score)