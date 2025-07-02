# Blog-Generation-using-Llama-3.2-HuggingFace

This project leverages the powerful **LLaMA 3.2 model** via HuggingFace Transformers to **generate blog posts** from user-defined prompts. It provides an efficient interface for automated long-form content creation with advanced control over output style and tone.

---

## 🧱 Tech Stack

- **Python 3.9+**
- **Transformers (HuggingFace)**
- **LLaMA 3.2 model** (from HuggingFace Hub)
- **Streamlit** for UI

---

## 🛠️ Setup Instructions

### 1. 📂 Clone the Repository

```bash
git clone https://github.com/Shaan2522/Blog-Generation-using-Llama-3.2-HuggingFace.git
cd Blog-Generation-using-Llama-3.2-HuggingFace
```

### 2. 🐍 Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

###4. 📥 Download or Load LLaMA 3.2 Model

You can use the model via HuggingFace hub:
```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3-8B")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Meta-Llama-3-8B")
```
