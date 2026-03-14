# from fastapi import FastAPI
# import joblib
# import numpy as np

# app = FastAPI()

# # load model
# model = joblib.load(r"C:\Users\chava\OneDrive\Desktop\TOPS\Exam\API2.joblib")

# @app.get("/")
# def request ():
#     return {"this pro is working"}

# @app.get("/pred")
# def request(age:float,income:float):
#     data = np.array([[age,income]])
#     pred = model.predict(data)
#     return {"Predict":float(pred[0])}


# this code is AI i dont know but he recomended me soo..
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # ← ADD THIS
import joblib
import numpy as np

app = FastAPI()

# ← ADD THIS BLOCK
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load(r"C:\Users\chava\OneDrive\Desktop\TOPS\Exam\API2.joblib")

@app.get("/")
def request():
    return {"this pro is working"}

@app.get("/pred")
def request(age: float, income: float):
    data = np.array([[age, income]])
    pred = model.predict(data)
    return {"Predict": float(pred[0])}
