import json
from sagemaker.predictor import Predictor
from sagemaker.serializers import JSONSerializer
from sagemaker.deserializers import JSONDeserializer

def load_request_json(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    return data["input"]

if __name__ == "__main__":
    request_json_path = "request.json"
    
    # get endpoint name
    # aws sagemaker list-endpoints 
    endpoint_name = <repository-name>-<timestamp>

    predictor = Predictor(endpoint_name)

    predictor.serializer = JSONSerializer()
    predictor.deserializer = JSONDeserializer()

    input_data = load_request_json(request_json_path)

    response = predictor.predict({"input": input_data})

    print(response)
