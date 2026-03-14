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
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware  # ← ADD THIS
# import joblib
# import numpy as np

# app = FastAPI()

# # ← ADD THIS BLOCK
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# model = joblib.load(r"API2.joblib")

# @app.get("/")
# def request():
#     return {"this pro is working"}

# @app.get("/pred")
from fastapi.responses import FileResponse

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import joblib
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("API2.joblib")

@app.get("/")
def home():
    return FileResponse("index.html")

@app.get("/pred")
def predict(age: float, income: float):
    data = np.array([[age, income]])
    pred = model.predict(data)
    return {"Predict": float(pred[0])}
def request(age: float, income: float):
    data = np.array([[age, income]])
    pred = model.predict(data)
    return {"Predict": float(pred[0])}
