# utils/llm_utils.py

from transformers import pipeline

# Load once and reuse
summarizer = pipeline("summarization", model="Falconsai/text_summarization")

def summarize_medical_text(raw_text):
    """
    Use Hugging Face model to summarize or explain extracted medical text
    """
    if not raw_text.strip():
        return "No text provided."
    
    chunks = [raw_text[i:i+1000] for i in range(0, len(raw_text), 1000)]
    summaries = []

    for chunk in chunks:
        summary = summarizer(chunk, max_length=200, min_length=30, do_sample=False)[0]['summary_text']
        summaries.append(summary)

    return "\n\n".join(summaries)
