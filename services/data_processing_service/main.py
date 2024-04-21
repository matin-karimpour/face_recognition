import grpc
import numpy as np
from concurrent import futures
import DataProcessing_pb2
import DataProcessing_pb2_grpc
from io import BytesIO
from imgbeddings import imgbeddings
from PIL import Image

# # loading the `imgbeddings`
def embedd_image(cropped_image):

    # calculating the embeddings
    embedding = embed_model.to_embeddings(cropped_image)[0]
    return embedding


				
                        
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
                print(embedd_image(Image.fromarray(img)))

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
    embed_model = imgbeddings()
    serve()


