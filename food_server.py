import concurrent
from concurrent import futures
import grpc

import foods_pb2
import foods_pb2_grpc

class FoodService(foods_pb2_grpc.FoodServicer):
    def OrderFood(self,request,context):
        print("got something")
        response = foods_pb2.FoodResponse()
        response.message = f"Number of order : {request.order}, Selected Cuisine : {request.cuisines}"
        return response
def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))
    foods_pb2_grpc.add_FoodServicer_to_server(FoodService(),server)
    server.add_insecure_port("[::]:50051")
    print("Server started. Listening to port 50051")
    server.start()
    server.wait_for_termination()

main()