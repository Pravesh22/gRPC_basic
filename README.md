# grpc_basic
Basic of how gRPC works



## create foods_pb2 and foods_grpc_pb2 file using foods proto file
run python -m grpc_tools.protoc -I. /protofile_path --python_out=. /path _to_save_pb2_grpcpb2 --grpc_python_out=. /protofile_path

After running this command foods_pb2.py and foods_grpc_pb2.py file will be generated in given path



## To run code
Run food_server.py
$ python /food_server_dir_path/food_server.py

then run food_clients.py
$ python /food_clients_dir_path/food_clients.py



## Output
message: "Number of order : 2, Selected Cuisine : Nepali"


