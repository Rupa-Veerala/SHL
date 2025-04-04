import pandas as pd
import json

def load_assessments():
    """Load assessments from SHL's catalog."""
    with open("data/assessments.json", "r") as file:
        data = json.load(file)
    return pd.DataFrame(data)

def preprocess_text(text):
    """Simple text preprocessing for better matching."""
    return text.lower().strip()
