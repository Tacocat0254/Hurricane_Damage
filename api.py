from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import img_to_array
from PIL import Image
from tensorflow.keras import layers
import numpy as np
import io

app = Flask(__name__)

# Constants
model_path = "models/best_damage_classification_model.keras"

# Load model on server startup
try:
    model = load_model(model_path)
    print(f"Model loaded successfully from {model_path}")
except Exception as e:
    print(f"Failed to load model: {e}")
    model = None

@app.route('/summary', methods=['GET'])
def summary():
    return jsonify({
        "version": "v4",
        "model_name": "Alternate LeNet-5 CNN",
        "input_shape": f"({img_height}, {img_width}, 3)",
        "output_labels": ["damage", "no_damage"]
    })

@app.route('/inference', methods=['POST'])
def upload_file():
    if model is None:
        return jsonify({"error": "Model not loaded"}), 500

    # Check if image file is in request
    if 'image' not in request.files:
        return jsonify({
            "error": "Invalid request; pass a binary image file as a multi-part form under the `image` key."
        }), 400

    try:
        file = request.files['image']
        img = Image.open(file).resize((150, 150))
        img_array = np.array(img) / 255.0
        img_list = np.expand_dims(img_array, axis=0).tolist()
        # Perform inference using the pre-trained model
        prediction = model.predict(img_list)

        # Make prediction
        confidence = float(prediction[0][0])
        if confidence >= 0.5:
            label = "No_Damage"
        else:
            label = "Damage"

        return jsonify({
            "prediction": label,
            "confidence": confidence
        })

    except Exception as e:
        return jsonify({
            "error": f"Failed to process image; details: {str(e)}"
        }), 500

# Run the server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
