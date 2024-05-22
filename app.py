from flask import Flask, request, jsonify
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
import os
import pandas as pd

app = Flask(__name__)

# Simulate a directory to store models
MODEL_DIR = "./models"
if not os.path.exists(MODEL_DIR):
    os.makedirs(MODEL_DIR)

# In-memory storage for loaded models
loaded_models = {}


def list_models():
    return [f.split(".")[0] for f in os.listdir(MODEL_DIR) if f.endswith(".pkl")]


@app.route("/models", methods=["GET"])
def get_models():
    return jsonify(list_models())


@app.route("/models", methods=["POST"])
def load_model():
    model_name = request.json.get("model_name")
    if model_name in loaded_models:
        return jsonify({"message": f"Model {model_name} is already loaded"}), 400

    model_path = os.path.join(MODEL_DIR, f"{model_name}.pkl")
    if not os.path.exists(model_path):
        return jsonify({"error": "Model not found"}), 404

    loaded_models[model_name] = joblib.load(model_path)
    return jsonify({"message": f"Model {model_name} loaded successfully"}), 200


@app.route("/models/<model_name>", methods=["DELETE"])
def unload_model(model_name):
    if model_name not in loaded_models:
        return jsonify({"error": "Model not loaded"}), 404

    del loaded_models[model_name]
    return jsonify({"message": f"Model {model_name} unloaded successfully"}), 200


@app.route("/models/<model_name>/predict", methods=["POST"])
def predict(model_name):
    if model_name not in loaded_models:
        return jsonify({"error": "Model not loaded"}), 404

    data = request.json.get("data")
    if data is None:
        return jsonify({"error": "No data provided"}), 400

    model = loaded_models[model_name]
    predictions = model.predict(pd.DataFrame([data]))
    return jsonify({"predictions": predictions.tolist()})


@app.route("/models/<model_name>/predict_csv", methods=["POST"])
def predict_csv(model_name):
    if model_name not in loaded_models:
        return jsonify({"error": "Model not loaded"}), 404

    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    if not file.filename.endswith(".csv"):
        return jsonify({"error": "Invalid file type, only CSV is allowed"}), 400

    df = pd.read_csv(file)
    if df.empty:
        return jsonify({"error": "Empty CSV file"}), 400

    model = loaded_models[model_name]
    predictions = model.predict(df.values)
    return jsonify({"predictions": predictions.tolist()})


@app.route("/models/train", methods=["POST"])
def train_model():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    if not file.filename.endswith(".csv"):
        return jsonify({"error": "Invalid file type, only CSV is allowed"}), 400

    df = pd.read_csv(file)
    if df.empty:
        return jsonify({"error": "Empty CSV file"}), 400

    model_name = request.form.get("model_name")
    if not model_name:
        return jsonify({"error": "Model name is required"}), 400

    target_column = request.form.get("target_column")
    if not target_column:
        return jsonify({"error": "Target column name is required"}), 400

    if target_column not in df.columns:
        return (
            jsonify({"error": f"Target column {target_column} not found in CSV"}),
            400,
        )

    X = df.drop(columns=[target_column])
    y = df[target_column]

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train a new RandomForest model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Predict on the test set
    y_pred = model.predict(X_test)

    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average="weighted")
    recall = recall_score(y_test, y_pred, average="weighted")
    f1 = f1_score(y_test, y_pred, average="weighted")

    # Save the model
    model_path = os.path.join(MODEL_DIR, f"{model_name}.pkl")
    joblib.dump(model, model_path)

    return (
        jsonify(
            {
                "message": f"Model {model_name} trained and saved successfully",
                "accuracy": accuracy,
                "precision": precision,
                "recall": recall,
                "f1_score": f1,
            }
        ),
        201,
    )


if __name__ == "__main__":
    app.run(debug=True)
