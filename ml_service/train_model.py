import pandas as pd
import xgboost as xgb
import shap
import joblib
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

df = pd.read_excel("credit_default.xls", header = 1) #excel load into a dataframe

#Renaming target column
df.rename(columns={"default payment next month":"default"}, inplace=True)

#Feature column selection and labelling
X = df.drop(columns=["ID", "default"])
y = df["default"]

#Split the data for train and test
X_train, X_test, y_train, y_test = train_test_split(X,y, stratify = y, test_size = 0.15, random_state=42)

#Train XGBoost ( justification regarding choice of model as a note)
model = xgb.XGBClassifier(use_label_encoder = False, eval_metric = "logloss")
model.fit(X_train, y_train)

#Predict
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

#SHAP for transperancy
explainer = shap.Explainer(model, X_train)

#make the models and explainer as jobs
joblib.dump(model, "credit_model.pkl")
joblib.dump(explainer, "credit_explainer.pkl")

print("Credit model successfully trained and saved in job pipeline")






