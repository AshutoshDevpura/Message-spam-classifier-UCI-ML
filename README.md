## NOTICE 
- Visit the website https://ashutoshdevpura-message-spam-classifier-uci-ml-app-ltp3nl.streamlit.app/
- Enter the message you want to classify as spam or not.
- Click on the "Check for Spam" button button to get the result.
- You can also use the examples from the "Messages.txt" file by copying and pasting them into the message input field.

# Message-spam-classifier-UCI-ML
This project involves building a spam classifier using the Naive Bayes algorithm. The dataset used is a set of SMS messages labeled as spam or ham.

## Table of Contents
- Technologies Used
- Dataset Description
- Project Description
- Data Cleaning and EDA
- Data Preprocessing
- Model Building
- Conclusion

## Technologies Used
- Python 3.9.7
- pandas 1.3.3
- scikit-learn 0.24.2
- matplotlib 3.4.3
- seaborn 0.11.2
- nltk 3.6.3

## Dataset Description
The dataset used is a collection of SMS messages that are labeled as spam or ham.

## Project Description
The main goal of this project is to build a Naive Bayes classifier that can accurately predict whether an SMS message is spam or ham.

## Data Cleaning and EDA
The first step in the project involved cleaning the dataset by dropping unnecessary columns and renaming columns for better readability. I also checked for missing values and duplicate values, and removed any duplicates found.
Exploratory data analysis was done to understand the distribution of spam and ham messages in the dataset. I used various visualization techniques such as a pie chart and histograms to visualize the distribution of the number of characters, words, and sentences in spam and ham messages.

## Data Preprocessing
The next step involved preprocessing the text data to convert it into a format that can be fed into a machine learning model. I performed text normalization techniques such as converting all text to lowercase, removing stopwords and punctuation, and stemming the text.
I also created a word cloud to visualize the most common words in spam and ham messages.

## Model Building
Finally, I built a Naive Bayes classifier using the CountVectorizer and TfidfVectorizer to convert text into numerical features. I split the dataset into training and testing sets and evaluated the performance of the model using accuracy, confusion matrix, and precision.
I used three types of Naive Bayes models: GaussianNB, MultinomialNB, and BernoulliNB. I found that MultinomialNB provided the highest accuracy and precision.

## Conclusion
I were able to build a Naive Bayes classifier that can accurately predict whether an SMS message is spam or ham with an accuracy of approximately 98%. The model can be further improved by using more advanced natural language processing techniques and trying out other classification algorithms.
