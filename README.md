<H3>Docker Image Name:</H3>
```
el32859/ml-housing-api`
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

