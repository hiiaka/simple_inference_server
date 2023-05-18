import base64
import json
import numpy as np
import tensorflow as tf
from PIL import Image
from io import BytesIO
from flask import Flask, request, jsonify
import boto3

app = Flask(__name__)

# load the mnist model
model = tf.keras.models.load_model('mnist_model')

# Initialize the S3 client
s3_client = boto3.client('s3')

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'status': 'ok'})

@app.route('/invocations', methods=['POST'])
def invocations():

    # Download image from S3   
    bucket = 'your-bucket-name'
    key = 'sample_image.png' 
    image_obj = s3_client.get_object(Bucket=bucket, Key=key)
    image_data = image_obj['Body'].read() 

    # Load the image and preprocess it    
    image = Image.open(BytesIO(image_data)).convert('L')
    image = image.resize((28, 28))
    image = np.array(image) / 255.0
    image = image.reshape(1, 28, 28, 1)

    # inference
    prediction = model.predict(image)
    prediction = np.argmax(prediction, axis=1).item()

    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
