## NOTICE 
- Visit the website: https://ashutoshdevpura-message-spam-classifier-uci-ml-app-ltp3nl.streamlit.app/
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
- Output
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

## Output
- ### SPAM 
<img width="1512" alt="Screenshot 2023-04-28 at 3 13 48 PM" src="https://user-images.githubusercontent.com/46817661/235234053-51f18380-a3e7-433b-a44c-45a270cb3f79.png">

<img width="1510" alt="Screenshot 2023-04-28 at 3 14 11 PM" src="https://user-images.githubusercontent.com/46817661/235234082-f27db14d-e652-4e5d-a6ee-bfd4c59e9041.png">

- ### NOT A SPAM
<img width="1510" alt="Screenshot 2023-04-28 at 3 14 38 PM" src="https://user-images.githubusercontent.com/46817661/235234116-7b95480f-f4c7-4d4a-b57d-6e2c1d3ebb01.png">

<img width="1512" alt="Screenshot 2023-04-28 at 3 15 04 PM" src="https://user-images.githubusercontent.com/46817661/235234144-78953951-2e86-435e-b029-7dfb29513da7.png">


## Conclusion
I was able to build a Naive Bayes classifier that can accurately predict whether an SMS message is spam or ham with an accuracy of approximately 98%. The model can be further improved by using more advanced natural language processing techniques and trying out other classification algorithms.
