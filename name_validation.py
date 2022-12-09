from tensorflow import keras
import tensorflow as tf
import numpy as np
from configparser import ConfigParser
import tensorflow_text as text

from utils.metrics import balanced_f1_score, balanced_precision, balanced_recall



config = ConfigParser()
config.read('config.ini')
model_path = config['model']['dir']



model = keras.models.load_model(model_path, custom_objects={ 
	'accuracy':tf.keras.metrics.CategoricalAccuracy(name="accuracy"),
	'balanced_recall': balanced_recall,
	'balanced_precision':balanced_precision,
	'balanced_f1_score':balanced_f1_score})


def predict_class(names): 
	'''predict class of input text
	Args:
	- reviews (list of strings)
	Output:
	- class (list of int)
	'''
	return [np.argmax(pred) for pred in model.predict(names)]


def is_valid_name(name:str) -> bool:
	'''
	Args:
		- name (string)
	Output:
		- is_valid_name (bool)
	'''
	names = []
	names.append(name)
	pred = predict_class(names)

	return True if pred[0] == 1 else False