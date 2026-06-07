import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import gradio as gr

model_path = "./saved_bert_news_model"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

label_map = {
    0: "World",
    1: "Sports",
    2: "Business",
    3: "Sci/Tech"
}

def classify_news(text):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    with torch.no_grad():
        outputs = model(**inputs)

    prediction = torch.argmax(outputs.logits, dim=1).item()

    return label_map[prediction]

demo = gr.Interface(
    fn=classify_news,
    inputs="textbox",
    outputs="text",
    title="News Topic Classifier using BERT"
)

demo.launch()