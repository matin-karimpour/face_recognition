import grpc
import numpy as np
from concurrent import futures
import DataProcessing_pb2
import DataProcessing_pb2_grpc
from io import BytesIO
from vector_database import VectorDatabase
from embeding import EmbedImage

class FaceDetectServer(DataProcessing_pb2_grpc.DataProcessingServicer):

    # ==========
    def __init__(self):
        self.embed_model = EmbedImage()
        self.vd = VectorDatabase()
        
        

    # ==========
    def getStream(self, request, context):

        

        np_bytes = BytesIO(request.images)
        images = np.load(np_bytes, allow_pickle=False)
        if request.action == "search":
            find = []
            for img in images:
                score = self.vd.search(self.embed_model.embedd_image(img)[0])

                if score >= 0.86:
                    print("find: ", score)
                    find.append(1)
                else:
                    find.append(0)

                if 1 in find:
                    msg = 1
                else :
                    msg = 0
            return DataProcessing_pb2.Replyresult(msg=msg)
        
        elif request.action == "insert":
            print(request.name)
            for img in images:
                self.vd.insert(self.embed_model.embedd_image(img), name=request.name, id=int(request.name.split("-")[-1]))
            return DataProcessing_pb2.Replyresult(msg=2)




def serve():
    print('server start')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    DataProcessing_pb2_grpc.add_DataProcessingServicer_to_server(FaceDetectServer(), server)

    server.add_insecure_port('[::]:50052')

    server.start()
    server.wait_for_termination()