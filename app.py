from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from uvicorn import run as app_run

from src.constants import APP_HOST, APP_PORT
from src.pipeline.prediction_pipeline import VehicleData, VehicleDataClassifier
from src.pipeline.training_pipeline import TrainPipeline

# -----------------------------
# Initialize App
# -----------------------------
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# -----------------------------
# CORS
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Form Handler
# -----------------------------
class DataForm:
    def __init__(self, request: Request):
        self.request = request

    async def get_data(self):
        form = await self.request.form()

        return {
            "Gender": int(form.get("Gender") or 0),
            "Age": int(form.get("Age") or 0),
            "Driving_License": int(form.get("Driving_License") or 0),
            "Region_Code": float(form.get("Region_Code") or 0),
            "Previously_Insured": int(form.get("Previously_Insured") or 0),
            "Annual_Premium": float(form.get("Annual_Premium") or 0),
            "Policy_Sales_Channel": float(form.get("Policy_Sales_Channel") or 0),
            "Vintage": int(form.get("Vintage") or 0),
            "Vehicle_Age_lt_1_Year": int(form.get("Vehicle_Age_lt_1_Year") or 0),
            "Vehicle_Age_gt_2_Years": int(form.get("Vehicle_Age_gt_2_Years") or 0),
            "Vehicle_Damage_Yes": int(form.get("Vehicle_Damage_Yes") or 0),
        }

# -----------------------------
# Routes
# -----------------------------

# Home Page (FIXED)
@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="vehicledata.html",
        context={"context": "Fill the form"}
    )

# Train Model
@app.get("/train")
async def train():
    try:
        pipeline = TrainPipeline()
        pipeline.run_pipeline()
        return Response("Training Successful!")

    except Exception as e:
        return Response(f"Training Error: {e}")

# Prediction (FIXED)
@app.post("/")
async def predict(request: Request):
    try:
        form = DataForm(request)
        data = await form.get_data()

        vehicle_data = VehicleData(**data)
        df = vehicle_data.get_vehicle_input_data_frame()

        model = VehicleDataClassifier()
        prediction = model.predict(df)

        if prediction is None or len(prediction) == 0:
            raise Exception("Empty prediction from model")

        result = "Response-Yes" if prediction[0] == 1 else "Response-No"

        return templates.TemplateResponse(
            request=request,
            name="vehicledata.html",
            context={"context": result}
        )

    except Exception as e:
        return templates.TemplateResponse(
            request=request,
            name="vehicledata.html",
            context={"context": f"Error: {str(e)}"}
        )

# -----------------------------
# Run Server
# -----------------------------
if __name__ == "__main__":
    # app_run(app, host=APP_HOST, port=APP_PORT)
    # app_run(app)
    # app_run(app, host=APP_HOST, port=APP_PORT)
    pass