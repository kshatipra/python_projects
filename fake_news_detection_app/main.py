import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import string
import re

# Load dataset
df_fake = pd.read_csv('python_projects/fake_news_detection_app/data/Fake.csv')
df_true = pd.read_csv('python_projects/fake_news_detection_app/data/True.csv')

#Add labels
df_fake['label'] = 'FAKE'
df_true['label'] = 'REAL'

#print(df_fake.head())

# Combine datasets
df = pd.concat([df_fake, df_true])
#print(df)
df = df.sample(frac=1).reset_index(drop=True)  # Shuffle the dataset
#print(df)

#check class distribution
print(df['label'].value_counts()) #shows the number of fake and real news articles

def clean_text(text):
    text = text.lower() # Convert to lowercase
    text = re.sub(r'\[.*?\]','', text) # Remove text in square brackets
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text) # Remove punctuation
    text = re.sub(r'\w*\d\w*', '', text) # Remove words containing numbers
    text = re.sub(r'\n', ' ', text) # Remove newlines
    return text

df['content'] = df['title']+" "+df['text'] #Combime title and text columns
df['content'] = df['content'].apply(clean_text)
#print(df['content'])

#define stop words
stop_words = stopwords.words('english')

#split into train/test
X_train, X_test, y_train, y_test = train_test_split(df['content'], df['label'], test_size=0.2, random_state=42)

#TF-IDF Vectorizer
vectorizer = TfidfVectorizer(stop_words=stop_words, max_df  =0.7)

#Fit and transform the training data
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

#Train logistic regression model
model = LogisticRegression()
model.fit(X_train_vec, y_train)

#Predict 
y_pred = model.predict(X_test_vec)

#Evaluate the model
print("\nClassification Report:\n", classification_report(y_test, y_pred))

#Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['FAKE', 'REAL'], yticklabels=['FAKE', 'REAL'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()