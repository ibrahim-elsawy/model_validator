from keras import backend as K


def balanced_recall(y_true, y_pred):
	"""This function calculates the balanced recall metric
	recall = TP / (TP + FN)
	"""
	recall_by_class = 0
	# iterate over each predicted class to get class-specific metric
	for i in range(y_pred.shape[1]):
		y_pred_class = y_pred[:, i]
		y_true_class = y_true[:, i]
		true_positives = K.sum(
		K.round(K.clip(y_true_class * y_pred_class, 0, 1)))
		possible_positives = K.sum(K.round(K.clip(y_true_class, 0, 1)))
		recall = true_positives / (possible_positives + K.epsilon())
		recall_by_class = recall_by_class + recall
	return recall_by_class / y_pred.shape[1]


def balanced_precision(y_true, y_pred):
	"""This function calculates the balanced precision metric
	precision = TP / (TP + FP)
	"""
	precision_by_class = 0
	# iterate over each predicted class to get class-specific metric
	for i in range(y_pred.shape[1]):
		y_pred_class = y_pred[:, i]
		y_true_class = y_true[:, i]
		true_positives = K.sum(
		K.round(K.clip(y_true_class * y_pred_class, 0, 1)))
		predicted_positives = K.sum(K.round(K.clip(y_pred_class, 0, 1)))
		precision = true_positives / (predicted_positives + K.epsilon())
		precision_by_class = precision_by_class + precision
	# return average balanced metric for each class
	return precision_by_class / y_pred.shape[1]


def balanced_f1_score(y_true, y_pred):
	"""This function calculates the F1 score metric"""
	precision = balanced_precision(y_true, y_pred)
	recall = balanced_recall(y_true, y_pred)
	return 2 * ((precision * recall) / (precision + recall + K.epsilon()))
