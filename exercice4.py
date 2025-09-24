import fastapi
from pydantic import BaseModel
import joblib
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
from transformers import pipeline


app = fastapi.FastAPI()
local_model_path = "./bert_qa_model/"

# Load tokenizer and model from local folder
tokenizer = AutoTokenizer.from_pretrained(local_model_path)
model = AutoModelForQuestionAnswering.from_pretrained(local_model_path)

# Create QA pipeline
qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)

class Item(BaseModel):
    context: str
    question: str

@app.post("/predict")
def test(item: Item):
    result = qa_pipeline(question=item.question, context=item.context)
    return {"result": result}

