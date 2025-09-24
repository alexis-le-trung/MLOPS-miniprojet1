from transformers import AutoTokenizer, AutoModelForQuestionAnswering
from transformers import pipeline

# Path to your local model
local_model_path = "./bert_qa_model/"

# Load tokenizer and model from local folder
tokenizer = AutoTokenizer.from_pretrained(local_model_path)
model = AutoModelForQuestionAnswering.from_pretrained(local_model_path)

# Create QA pipeline
qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)

# Example
context = """
Hello Alexis,

Thank you for booking with Chez Gourmet. 
Your reservation is confirmed for 2025-09-12 at 19:30. 
Please let us know if you have any special requests.

Best regards,
Chez Gourmet Team
"""

# Question: what time is the reservation?
question = "What time is the reservation?"

result = qa_pipeline(question=question, context=context)
print("Answer:", result['answer'])