Auto Tagging Support Tickets Using LLM
Objective

Automatically classify customer support tickets into relevant categories using a Large Language Model (LLM) and Prompt Engineering techniques.

Dataset

Customer Support Tickets Dataset

Categories
Billing inquiry
Cancellation request
Product inquiry
Refund request
Technical issue
Approach

1. Data Preprocessing
   Loaded support ticket dataset using Pandas
   Combined Ticket Subject and Ticket Description into a single text field
   Performed basic data inspection and validation
2. Zero-Shot Classification

Used a pre-trained Hugging Face model:

typeform/distilbert-base-uncased-mnli

The model predicts ticket categories without task-specific training.

3. Few-Shot Prompting

Provided descriptive category definitions to improve label understanding and compare results with the zero-shot approach.

4. Top-3 Tag Prediction

For each ticket, the model returns the three most probable categories along with confidence scores.

Evaluation

Metrics Used:

Accuracy
Precision
Recall
F1-Score
Results
Zero-shot classification was successfully implemented.
Top-3 tag prediction was generated for support tickets.
Few-shot prompting influenced category predictions.
Performance demonstrates the strengths and limitations of prompt-engineering-based classification without fine-tuning.
Technologies Used
Python
Pandas
Hugging Face Transformers
Scikit-learn
DistilBERT (MNLI)
Project Structure

Auto Tagging With LLM Task5/
│
├── Auto_Tagging_Support_Tickets.ipynb
├── customer_support_tickets.csv
└── README.md

Conclusion

This project demonstrates how Large Language Models can be used for automated support ticket tagging using zero-shot and few-shot prompting techniques.
