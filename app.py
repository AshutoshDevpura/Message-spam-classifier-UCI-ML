
# Author : Ashutosh Devpura
# Email: ashutoshdevpura@gmail.com


import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords') 
ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

tfidf = pickle.load(open('artifacts/vectorizer.pkl','rb'))
model = pickle.load(open('artifacts/model.pkl','rb'))

st.set_page_config(page_title="Email/SMS Spam Classifier", page_icon=":email:")

st.title("Email/SMS Spam Classifier")

st.markdown(
"""
<style>
body {
    background-color: #F5F5F5;
}
header {
    color: #483D8B;
    font-size: 36px;
    font-weight: bold;
    text-align: center;
    padding: 30px 0px;
    margin-bottom: 30px;
    border-bottom: 3px solid #483D8B;
}
p {
    font-size: 18px;
    margin-bottom: 20px;
}
.spam {
    color: red;
    font-weight: bold;
    font-size: 24px;
}
.not-spam {
    color: green;
    font-weight: bold;
    font-size: 24px;
}
</style>
""", unsafe_allow_html=True)

input_sms = st.text_area("Enter the message you want to check for spam")

if st.button('Check for spam'):

    # 1. preprocess
    transformed_sms = transform_text(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.header(":warning: This message is a SPAM! :warning:")
    else:
        st.header(":white_check_mark: This message is NOT a spam! :white_check_mark:")

# Add footer text
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')

st.markdown(
"""
<div style='text-align: center'>
<p>Made with ❤️ by Ashutosh Devpura</p>
</div>
""", unsafe_allow_html=True)

