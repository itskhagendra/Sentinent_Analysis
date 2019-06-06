import pickle
import numpy as np
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences

model = load_model("Sentiment-negative_bias.h5")
print("Model Loaded Successfully")

with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
print("Tokenizer loaded successfully")

txt = input("Enter Your Thoughts ")
twt = [txt]

twt = tokenizer.texts_to_sequences(twt)
twt = pad_sequences(twt, maxlen=40, dtype='int32', value=0)
sentiment = model.predict(twt, batch_size=1, verbose=0)[0]

if np.argmax(sentiment) == 0:
    print("Negative")
elif np.argmax(sentiment) == 1:
    print("Positive")
