import numpy as np
import pandas as pd
import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical


MAX_SEQUENCE_LENGTH = 5000
MAX_NUM_WORDS = 25000
EMBEDDING_DIM = 300
TEST_SPLIT = 0.2

tokenizer = Tokenizer(num_words=MAX_NUM_WORDS)
model = tf.keras.models.load_model("trainedModel.h5")

# text_input needs to be an array of one element, which contains the text of the article
def predict(text_input):
	tokenizer.fit_on_texts([text_input[0]])
	sequences = tokenizer.texts_to_sequences([text_input[0]])

	word_index = tokenizer.word_index
	num_words = min(MAX_NUM_WORDS, len(word_index)) + 1
	data = pad_sequences(sequences, 
	                     maxlen=MAX_SEQUENCE_LENGTH, 
	                     padding='pre', 
	                 truncating='pre')
	integervalue = int(np.rint(model.predict( np.array( [data[0],] )  ))[0][0])
	if integervalue == 0:
		return "fake"
	return "real"


print(predict(["The coronavirus isn't really a big deal."]))














