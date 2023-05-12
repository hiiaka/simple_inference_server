import base64
import json

def encode_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')

def create_request_json(encoded_image, output_file):
    data = {"input": encoded_image}
    with open(output_file, "w") as f:
        json.dump(data, f)

if __name__ == "__main__":
    sample_image_path = "sample_image.png"
    output_json_path = "request.json"
    
    encoded_image = encode_image(sample_image_path)
    create_request_json(encoded_image, output_json_path)
