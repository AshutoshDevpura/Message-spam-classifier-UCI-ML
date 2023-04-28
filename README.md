# Message-spam-classifier-UCI-ML


## Problem Statement:
The goal of this code is to build a machine learning model to predict whether a given text message is spam or ham (not spam) based on its content. The dataset used in this code contains a collection of SMS messages that are already labeled as spam or ham.

## Definition:
The code begins by performing Exploratory Data Analysis (EDA) on the dataset to gain insights about the data. The df.head() function is used to display the first few rows of the dataset. The df['target'].value_counts() function is used to display the number of ham and spam messages in the dataset. The matplotlib.pyplot library is used to create a pie chart that shows the distribution of ham and spam messages.

The nltk library is used for Natural Language Processing (NLP) tasks such as tokenization, stemming, and removing stop words. The nltk.download() function is used to download the necessary resources for NLP. The df['num_characters'], df['num_words'], and df['num_sentences'] functions are used to add new columns to the dataset that contain the number of characters, words, and sentences in each message. These new columns are used to analyze the characteristics of spam and ham messages in the dataset.

The seaborn library is used to create visualizations of the data, such as histograms and pairplots. The sns.histplot function is used to create histograms of the number of characters and words in each message. The sns.pairplot function is used to create a pairplot that shows the correlation between the variables in the dataset.

The transform_text() function is defined to preprocess the text data in the dataset. This function converts the text to lowercase, tokenizes the text, removes stop words and punctuation, and stems the remaining words. The df['transformed_text'] function is used to create a new column in the dataset that contains the preprocessed text.

The WordCloud library is used to create word clouds that visualize the most common words in spam and ham messages. The sns.barplot function is used to create a bar plot that shows the frequency of the most common words in spam messages.

The dataset is then prepared for machine learning by using the CountVectorizer() and TfidfVectorizer() functions to create a Bag of Words representation of the preprocessed text data. The data is split into training and testing sets, and several machine learning algorithms such as Gaussian Naive Bayes, Multinomial Naive Bayes, and Bernoulli Naive Bayes are applied to the data. The performance of each algorithm is evaluated using metrics such as accuracy, confusion matrix, and precision score. Finally, a variety of machine learning algorithms including Logistic Regression, Support Vector Machine, Decision Tree, K-Nearest Neighbors, Random Forest, AdaBoost, Bagging, ExtraTrees, Gradient Boosting, and XGBoost are trained on the dataset, and their performance is compared.

## Data
The dataset used in this code is the ......
...........................................

## Files
-
-
-
-
-
-
-


## Technologies Used
.....



## Algorithms and Techniques
........




##  Data Collection and Preprocessing
........



## Run Locally

Clone the project

```bash
  git clone https://github.com/AshutoshDevpura..........
```

Go to the project directory

```bash
  cd 
```

Install dependencies

```bash
   pip install -r requirements.txt
```

Start the server

```bash
  streamlit run app.py
```


## Deployment
I saved the preprocessed dataframe and .............. and deployed the system using Streamlit.

## Conclusion
Overall, this project demonstrated how to build a  By preprocessing the data and using ..........., I was able to create a system that provides .............. based on user input.
