from fastapi import FastAPI, HTTPException
import pandas as pd
import joblib
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)
model = joblib.load("credit_model.pkl")
explainer = joblib.load("credit_explainer.pkl")

@app.post("/predict")
def predict(input: dict):
    try:
        df = pd.DataFrame([input])
        prob = float(model.predict_proba(df)[0][1])
        shap_values = explainer(df)
        contribs = dict(zip(df.columns, shap_values[0].values))
        top_features = dict(sorted(contribs.items(), key = lambda x: abs(x[1]), reverse = True)[:3])
        return {"score": prob, "explanation": top_features}
    except Exception as e:
        raise HTTPException(status_code=500, detail = str(e))