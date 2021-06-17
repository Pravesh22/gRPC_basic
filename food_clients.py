import grpc
import foods_pb2
import foods_pb2_grpc

def main():
    channel = grpc.insecure_channel('localhost:50051')
    client = foods_pb2_grpc.FoodStub(channel=channel)
    request = foods_pb2.FoodRequest(order=2,cuisines="Nepali")
    response = client.OrderFood(request)
    print(response)

main()
