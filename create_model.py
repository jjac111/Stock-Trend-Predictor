from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint, Callback
from keras.models import Model
from keras.layers import Dense, Input, Dropout, Activation

input_dim = 11
d1 = 2*input_dim
d2 = round(input_dim/2)
d3 = 1
activation = 'sigmoid'
dropout = 0.4
epochs = 10000
lr = 0.01
batch = 100
	
def create_model(t, n1, n2):
    input_dim = 11
    d1 = 2*input_dim
    d2 = round(input_dim/2)
    d3 = 1
    activation = 'sigmoid'
    dropout = 0.4
    epochs = 10000
    lr = 0.01
    batch = 100
    
    input_layer = Input(name='the_input', shape=(input_dim,), batch_shape=(None, input_dim))
    # Add dense layers
    dense_1 = Dense(d1, activation=activation)(input_layer)
    drop_1 = Dropout(dropout)(dense_1)
    dense_2 = Dense(d2, activation=activation)(drop_1)
    drop_2 = Dropout(dropout)(dense_2)
    dense_3 = Dense(d3, activation=activation)(drop_2)

    # Add sigmoid activation layer
    y_pred = Activation('sigmoid', name='sigmoid')(dense_3)

    # Specify the model
    model = Model(inputs=input_layer, outputs=y_pred, name=f'{t}-{n1}-{n2}')
    model.output_length = lambda x: x
    
    return model