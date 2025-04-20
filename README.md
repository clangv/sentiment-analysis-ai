# 🧠 Sentiment Analysis AI

This project is a basic sentiment analysis app built using the Hugging Face `transformers` library. It uses the **FinBERT** model (`ProsusAI/finbert`) to analyze financial sentiment in text and classify it as **positive**, **negative**, or **neutral**.

---

## 📌 Features

- Uses pre-trained transformer model for sentiment classification
- Supports financial or investment-related text
- Clean and minimal Python implementation
- Easy to expand for real-world applications or APIs

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/sentiment-analysis-ai.git
cd sentiment-analysis-ai
```
### 2. Set up virtual environment
```bash
python -m venv .venv
```
### 3. Activate virtual environment
Windows (CMD):
```bash
.venv\Scripts\activate
```
PowerShell:
```bash
.venv\Scripts\Activate.ps1
```
macOS/Linux:
```bash
source .venv/bin/activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## 📄 Usage
Run the app:
```bash
python app.py
```
Then input any sentence like:
```bash
"The market is doing great this week!"
```
Expected output:
```bash
[{'label': 'positive', 'score': 0.981}]
```

## 📄 Model Used
ProsusAI/finbert – a version of BERT fine-tuned on financial text for sentiment classification.
