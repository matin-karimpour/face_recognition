import grpc
import numpy as np
from concurrent import futures
import DataProcessing_pb2
import DataProcessing_pb2_grpc
from io import BytesIO

				
                        
class Greeter(DataProcessing_pb2_grpc.DataProcessingServicer):

    # ==========
    def __init__(self):
        pass

    # ==========
    def getStream(self, request_iterator, context):

        for req in request_iterator:

            np_bytes = BytesIO(req.images)
            images = np.load(np_bytes, allow_pickle=True)

            for img in images:
                print(img)

            yield DataProcessing_pb2.ReplyData(msg=1)


def serve():
    print('server start')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    DataProcessing_pb2_grpc.add_DataProcessingServicer_to_server(Greeter(), server)

    server.add_insecure_port('[::]:50052')

    server.start()
    server.wait_for_termination()


#============================================================
# main
#============================================================
if __name__ == '__main__':    
    serve()



