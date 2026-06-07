# News Topic Classifier Using BERT

## Objective

Build a news classification model using BERT to categorize news articles into:

- World
- Sports
- Business
- Sci/Tech

## Dataset

AG News Dataset (Hugging Face)

## Technologies Used

- Python
- Pandas
- Hugging Face Transformers
- BERT (bert-base-uncased)
- Scikit-learn
- Matplotlib
- Seaborn

## Methodology

1. Loaded AG News dataset
2. Performed Exploratory Data Analysis (EDA)
3. Tokenized text using BERT Tokenizer
4. Fine-tuned BERT for text classification
5. Evaluated model using Accuracy, F1 Score, Classification Report and Confusion Matrix
6. Saved trained model for future predictions

## Results

- Accuracy: 90.7%
- F1 Score: 90.69%

## Key Findings

The fine-tuned BERT model achieved strong performance in classifying news articles across four categories and demonstrated the effectiveness of transformer-based NLP models for text classification tasks.

## Deployment

A simple Gradio web application was developed to allow users to classify news headlines interactively.
