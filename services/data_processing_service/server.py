from concurrent import futures
from io import BytesIO

import grpc
import numpy as np

import DataProcessing_pb2
import DataProcessing_pb2_grpc
from embeding import EmbedImage
from vector_database import VectorDatabase


class FaceDetectServer(DataProcessing_pb2_grpc.DataProcessingServicer):

    # ==========
    def __init__(self):
        self.embed_model = EmbedImage()
        self.vd = VectorDatabase()

    # ==========
    def getStream(self, request, context):

        np_bytes = BytesIO(request.images)
        images = np.load(np_bytes, allow_pickle=False)

        np_bytes = BytesIO(request.track_ids)
        track_ids = np.load(np_bytes, allow_pickle=False)

        if request.action == "search":
            find = []
            for idx, img in enumerate(images):

                if len(track_ids) > 0:
                    id = track_ids[idx]
                else:
                    id = -1

                score = self.vd.search(self.embed_model.embedd_image(img)[0])

                if score >= 0.86:
                    print("find: ", score)
                    find.append(1)
                    track_id = id
                    find_img = np.array(img)
                else:
                    find.append(0)

            if 1 in find:
                msg = 1

            else:
                msg = 0
                track_id = -1
                find_img = np.array(img)

            find_img_byte = BytesIO()
            np.save(find_img_byte, find_img, allow_pickle=False)
            return DataProcessing_pb2.Replyresult(msg=msg, track_id=track_id, image=find_img_byte.getvalue())

        elif request.action == "insert":
            print(request.name)
            for img in images:
                self.vd.insert(self.embed_model.embedd_image(img), name=request.name,
                               id=int(request.name.split("-")[-1]))
            find_img_byte = BytesIO()
            np.save(find_img_byte, np.array(img), allow_pickle=False)
            return DataProcessing_pb2.Replyresult(msg=2, track_id=-1, image=find_img_byte.getvalue())


def serve():
    print('server start')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    DataProcessing_pb2_grpc.add_DataProcessingServicer_to_server(FaceDetectServer(), server)

    server.add_insecure_port('[::]:50052')

    server.start()
    server.wait_for_termination()
