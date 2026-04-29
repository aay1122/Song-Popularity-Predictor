from flask import Flask, request, jsonify
from model import predict_popularity

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Backend running"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        features = {
            "tempo": float(data["tempo"]),
            "energy": float(data["energy"]),
            "danceability": float(data["danceability"])
        }

        result, score = predict_popularity(features)

        return jsonify({
            "prediction": result,
            "score": score,
            "input": features
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)