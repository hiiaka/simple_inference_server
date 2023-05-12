import base64
import json
import numpy as np
import tensorflow as tf
from PIL import Image
from io import BytesIO
from flask import Flask, request, jsonify

app = Flask(__name__)

# load the mnist model
model = tf.keras.models.load_model('mnist_model')

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'status': 'ok'})

@app.route('/invocations', methods=['POST'])
def invocations():
    # input image
    input_data = json.loads(request.data)['input']
    image = base64.b64decode(input_data)
    image = Image.open(BytesIO(image)).convert('L')
    image = image.resize((28, 28))
    image = np.array(image) / 255.0
    image = image.reshape(1, 28, 28, 1)

    # inference
    prediction = model.predict(image)
    prediction = np.argmax(prediction, axis=1).item()

    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
