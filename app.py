from flask import Flask, request
import json
import os
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Load the model
model = tf.keras.models.load_model(os.environ['MODEL_PATH'])

@app.route('/ping', methods=['GET'])
def ping():
    """Determine if the container is working and healthy."""
    return '', 200

@app.route('/invocations', methods=['POST'])
def invocations():
    """Do an inference on a single batch of data."""
    data = request.get_json(force=True)
    
    # Convert the input data to a numpy array and reshape it
    input_data = np.array(data['instances']).reshape(-1, 28, 28, 1)
    
    # Make a prediction
    predictions = model.predict(input_data)
    
    return json.dumps(predictions.tolist())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
