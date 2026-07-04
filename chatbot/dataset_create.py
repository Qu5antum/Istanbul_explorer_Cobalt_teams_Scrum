from datasets import Dataset
from data.istanbul_documents import ISTANBUL_DOCS

documents = []

for key, value in ISTANBUL_DOCS.items():
    documents.append({
        "text": value,
        "kaynak": key
    })

dataset = Dataset.from_list(documents)
dataset.save_to_disk("rag_data/istanbul_dataset")