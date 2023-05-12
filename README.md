Make MNIST model
```sh
python3 mnist.py
```

Make MNIST inference image
```sh
docker build -t my-inference-image .
```

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