# Setup
Make MNIST model
```sh
python3 mnist.py
```

Make MNIST inference image
```sh
docker build -t my-inference-image .
```

# Inference at local host
Start MNIST inference container
```sh
docker run -p 8080:8080 my-inference-image
```

Check MNIST inference server
```sh
curl http://localhost:8080/ping

# {"status":"ok"}
```

Make base64 encoded MNIST image and request.json
```sh
python3 img2base64.py
```

Inference
```sh
curl -X POST -H "Content-Type: application/json" \
    -d @request.json \
    http://localhost:8080/invocations

# {"prediction":7}
```

# Inference at AWS

Push MNIST inference image to ECR
```sh
account_id=$(aws sts get-caller-identity --query Account --output text)
region=$(aws configure get region)
aws ecr create-repository --repository-name my-inference-image
aws ecr get-login-password | docker login --username AWS --password-stdin ${account_id}.dkr.ecr.${region}.amazonaws.com
docker tag my-inference-image:latest ${account_id}.dkr.ecr.${region}.amazonaws.com/my-inference-image:latest
docker push ${account_id}.dkr.ecr.${region}.amazonaws.com/my-inference-image:latest
```
Mkake MNIST inference endpoint
```sh
python3 gen_endpoint.py
```

Inference
```sh
python3 request_inference.py

# {"prediction":7}
```