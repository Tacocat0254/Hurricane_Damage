<H1>Hurricane Damage Classification</H1>
This project uses machine learning to classify images of buildings into "Damage" or "No Damage" categories based on images taken after a hurricane. The code processes and splits the dataset, builds multiple neural network architectures, and trains the models for classification.

<H2>Model Architectures</H2>

Three different neural network architectures are implemented to classify images of buildings as either damaged or not damaged.

### **1. Artificial Neural Network (ANN)**

A fully connected feed-forward neural network with the following architecture:

- **Input Layer**: Flattened 150x150x3 images
- **Hidden Layers**: 512 and 256 units with ReLU activation
- **Output Layer**: 1 unit with a sigmoid activation function for binary classification

### **2. LeNet-5 CNN**

A Convolutional Neural Network (CNN) based on the classic LeNet-5 architecture with:

- **Convolutional Layers**: 6 filters (5x5), 16 filters (5x5)
- **Max Pooling Layers**: Pool size of (2, 2)
- **Dense Layers**: 120 and 84 units with ReLU activation
- **Output Layer**: 1 unit with sigmoid activation

### **3. Alternate LeNet-5 CNN**

A more complex CNN with additional convolutional layers and dropout for regularization:

- **Convolutional Layers**: 32 filters (3x3), 64 filters (3x3), 128 filters (3x3), and another 128 filters (3x3)
- **Max Pooling Layers**: Pool size of (2, 2)
- **Flatten Layer**: To convert the 2D feature maps to 1D
- **Dropout Layer**: With a 50% rate to prevent overfitting
- **Dense Layer**: 512 units with ReLU activation and L2 regularization
- **Output Layer**: 1 unit with sigmoid activation

<H3>Docker Image Name:</H3>

```
el32859/ml-housing-api
```

<H3>Docker Build:</H3>
Make sure to be in models directory.

```
docker build -t el32859/ml-housing-api .
```

<H3>Docker Run:</H3>

```
docker run -it --rm -p 5000:5000 el32859/ml-housing-api
```
or

```
docker compose up
```

<H3>How to use model:</H3>
Model File: Stored at models/best_damage_classification_model.keras

Input: A JPEG/PNG image of a building after a hurricane.

Output: A prediction of "Damage" or "No_Damage" with a confidence score between 0 and 1

<H3>Running the Server:</H3>
To start the Flask server, simply run: python3 api.py
This will start the API at http://localhost:5000.

<H3>API Endpoints:</H3>
Provides basic model information: curl http://localhost:5000/summary
Response should look like this:

```
{
  "version": "v4",
  "model_name": "Alternate LeNet-5 CNN",
  "input_shape": "(150, 150, 3)",
  "output_labels": ["damage", "no_damage"]
}
```

Accepts an image and returns a prediction: 
```
curl -X POST http://localhost:5000/inference \
  -F "image=@no_damage.jpeg"
```

Response should look like this:

```
{
  "prediction": "Damage",
  "confidence": 0.123456
}
```

