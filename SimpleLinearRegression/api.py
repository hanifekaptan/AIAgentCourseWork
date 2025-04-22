from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import uvicorn

class PredictionInput(BaseModel):
    YearsExperience: float = Field(
        ...,
        description="The number of years of work experience.",
        json_schema_extra={"example": 5.0},
    )

class PredictionOutput(BaseModel):
    prediction: float = Field(
        ...,
        description="The predicted salary, rounded to two decimal places.",
        json_schema_extra={"example": 70000.0},
    )

app = FastAPI(
    title="Salary Prediction API",
    description="A simple API to predict salary based on years of work experience using a pre-trained model.",
    version="1.0.0"
)

try:
    model = joblib.load("model.pkl")
except FileNotFoundError:
    print("Error: model.pkl not found. Please ensure the model file exists.")
    model = None

@app.post(
    "/predict",
    response_model=PredictionOutput,
    tags=["Predictions"]
)
async def predict(input_data: PredictionInput):
    """
    Predicts salary based on years of experience.

    Takes the number of years of experience and returns the predicted salary.
    """
    if model is None:
         raise HTTPException(status_code=503, detail="Model is not loaded. Server configuration error.")

    try:
        years_experience = input_data.YearsExperience
        result = round(model.predict([[years_experience]])[0], 2)

        return PredictionOutput(prediction = result)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An internal error occurred during prediction: {str(e)}")


if __name__ == "__main__":
    if model is None:
        print("Application will not start because the model could not be loaded.")
    else:
        uvicorn.run(app, host="127.0.0.1", port=8000)
