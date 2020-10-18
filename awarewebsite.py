from flask import Flask, render_template, request
from forms import VerifyForm
import numpy as np
import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
import sys
app = Flask(__name__)
app.config['SECRET_KEY'] = "rheaandarjun"


@app.route('/', methods=['GET','POST'])
def result():
	form = VerifyForm()
	realorfake = ""
	if form.is_submitted():
		result = request.form
		realorfake = predict([result['articletext']])
	return render_template('index.html', form=form, realorfake=realorfake)

def predict(text_input):
	MAX_SEQUENCE_LENGTH = 5000
	MAX_NUM_WORDS = 25000
	EMBEDDING_DIM = 300
	TEST_SPLIT = 0.2

	tokenizer = Tokenizer(num_words=MAX_NUM_WORDS)
	model = tf.keras.models.load_model("trainedModel.h5")

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

@app.route('/about', methods=['GET', 'POST'])
def about():
	form = VerifyForm()
	if form.is_submitted():
		result = request.form
		print(result['articletext'])
	return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run()