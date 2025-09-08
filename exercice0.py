import fastapi
from pydantic import BaseModel
import joblib


app = fastapi.FastAPI()
model = joblib.load("regression.joblib")

class Item(BaseModel):
    size: float
    nb_rooms: float
    garden: int

@app.post("/predict")
def test(item: Item):
    X = [[item.size, item.nb_rooms, item.garden]]
    y_pred = model.predict(X)[0]
    return {"y_pred": y_pred}