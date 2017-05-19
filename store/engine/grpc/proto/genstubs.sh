#!/bin/bash -x
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./store_api.proto 
mv store_api_pb2.py ../client
mv store_api_pb2_grpc.py ../server
echo "Done"
