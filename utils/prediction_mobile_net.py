import tensorflow as tf
from tensorflow.keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from io import BytesIO
import numpy as np
from PIL import Image
import json
import cv2

@st.cache_resource
def prediction_ml(img):
    #neural network parameters 
    params = {'batch_size': 64,
    'learningRate':0.001,
    'momentum':0.90,
    "num_classes": 3,
    'epoche':100}

    input_shape = (224, 224, 3)
    #optim_1 = optimizers.SGD(learning_rate=0.0001)
    n_classes=3
    mobile_conv = tf.keras.applications.mobilenet_v2.MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

    for layer in mobile_conv.layers:
        layer.trainable = False
         
    x=mobile_conv.output
    x = tf.keras.layers.Conv2D(512, (3, 3), strides=(1, 1), padding="same")(x)
    x = tf.keras.layers.BatchNormalization(axis=-1, momentum=0.9)(x)
    x = tf.keras.activations.relu(x)
    x = tf.keras.layers.Conv2D(params["num_classes"], (1, 1), strides=(1, 1), padding="same")(x)
    x = tf.keras.layers.BatchNormalization(axis=-1, momentum=0.9)(x)
    x = tf.keras.activations.relu(x)
    x= tf.keras.layers.GlobalAveragePooling2D()(x)
    x= tf.keras.layers.BatchNormalization()(x)
    outputs = tf.keras.activations.softmax(x)

    model = tf.keras.Model(inputs= mobile_conv.input, outputs=outputs)
    model.load_weights('models/Model628-0.001739.hdf5')

    mb_preds = model.predict(img)
    perc_brain=mb_preds.item(0)
    perc_thx=mb_preds.item(1)
    perc_cerx=mb_preds.item(2)
    json_str = json.dumps({'BRAIN': perc_brain,"THORAX":perc_thx, "CERVIX":perc_cerx})
    return json_str


def read_image(file) -> Image.Image:
    pil_image = Image.open(BytesIO(file))
    #print('print dentro da funcao --- ok ')
    return pil_image


def resize_imagefile(file: Image.Image):
      img = np.asarray(file.resize((224, 224)))[..., :3]
      x = image.img_to_array(img)
      x = np.expand_dims(x, axis=0)
      x = preprocess_input(x)
      return x

def check_color_img(img):
    #check color image
    if cv2.countNonZero(image) == 0:
        black="YES"
        return black
    else:
        black="NO"
        return black
