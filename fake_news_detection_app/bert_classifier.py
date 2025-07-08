"""BERT Tokenizer converts text into tokens and these token ids - unique numbers from BERT vocab. This process is Tokenization"""
import pandas as pd
from sklearn.model_selection import train_test_split
from transformers import BertTokenizer
import torch
from transformers import BertForSequenceClassification, Trainer, TrainingArguments
import numpy as np
from sklearn.metrics import accuracy_score, precision_recall_fscore_support


# Load dataset
df_fake = pd.read_csv('python_projects/fake_news_detection_app/data/Fake.csv')
df_true = pd.read_csv('python_projects/fake_news_detection_app/data/True.csv')

#Add labels
df_fake['label'] = 0 #0 for fake
df_true['label'] = 1

df = pd.concat([df_fake, df_true])
df = df.sample(frac=1).reset_index(drop=True)  # Shuffle the dataset

df['content'] = df['title'] + " " + df['text']  # Combine title and text columns
df = df[['content', 'label']].dropna().head(1000)  # Keep only the first 10000 rows for simplicity and faster training

#Load BERT tokenizer
"""Loads the vocabulary abd special rules from the official BERT tokenizer."""
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased') #uncased : lowercase everything automatically
"""This splits the train data"""
X_train, X_test, y_train, y_test = train_test_split(df['content'], df['label'], test_size=0.2, random_state=42)

''''''
train_encodings = tokenizer(list(X_train), truncation= True, padding= True, max_length= 512, return_tensors='pt')
test_encodings = tokenizer(list(X_test), truncation= True, padding= True, max_length= 512, return_tensors='pt')

#tensor means multi-dimensional array or table of numbers or matrix

#Pytorch uses dataset and dataloader structure to handle daata. BERT expects input data in batches during training

class FakeNewsDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings  = encodings
        self.labels = labels
    
    def __len__(self):
        return len(self.labels)
    
    def __getitem__(self, idx):
        #returns one sample as dictionary
        item = {key:val[idx] for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx], dtype=torch.long)  # Convert label to tensor
        return item
    
#create dataset objects
train_dataset = FakeNewsDataset(train_encodings, y_train.tolist())
test_dataset = FakeNewsDataset(test_encodings, y_test.tolist())

#Load BERT model for sequence classification: Load the pretrained brain
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)


#Tell BERT how to learn(training arguements)
training_args = TrainingArguments(
output_dir='./results',  # Output directory for model predictions and checkpoints
    num_train_epochs=3,  # Number of training epochs
    per_device_train_batch_size=8,  # Batch size for training
    per_device_eval_batch_size=8,  # Batch size for evaluation
    eval_strategy='epoch',  # Evaluation strategy to use
    save_strategy='epoch',  # Save strategy to use
    logging_dir='./logs',  # Directory for storing logs
    logging_steps=10,  # Log every 10 steps
    load_best_model_at_end=True,  # Load the best model at the end of training
)


#Check BERT's homework(metrics)
def compute_metrics(pred):
    lables = pred.label_ids #Correct answer
    preds = np.argmax(pred.predictions, axis=1)  # Get the predicted labels
    precision, recall, f1, _ = precision_recall_fscore_support(lables, preds, average='binary')
    acc = accuracy_score(lables, preds)
    return {
        'accuracy': acc,
        'precision': precision,
        'recall': recall,
        'f1': f1
    }

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    compute_metrics=compute_metrics
)
#Train the model
trainer.train()