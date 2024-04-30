from concurrent import futures
from io import BytesIO

import cv2
import grpc
import numpy as np

import FaceDetection_pb2
import FaceDetection_pb2_grpc
from facedetecction_model import FaceDetectionModel


class FaceDetectioServer(FaceDetection_pb2_grpc.FaceDetectionServicer):

    # ==========
    def __init__(self):
        self.model = FaceDetectionModel()

    # ==========
    def getStream(self, req, context):

        try:

            dBuf = np.frombuffer(req.frame, dtype=np.uint8)
            # print(type(dBuf))
            frame = cv2.imdecode(dBuf, cv2.IMREAD_COLOR)
            results = self.model.track_faces(frame)
            if results[0].boxes.id != None:
                track_ids = np.array(results[0].boxes.id.int().cpu().tolist(), dtype=np.uint8)
            else:
                track_ids = np.array([])

            boxes = results[0].boxes.xyxy.cpu().tolist()

            track_ids_bytes = BytesIO()
            np.save(track_ids_bytes, track_ids, allow_pickle=False)

            return FaceDetection_pb2.ReplyData(faces=self.get_crop_imeges(frame, boxes), ids=track_ids_bytes.getvalue())

        except grpc.RpcError as e:
            print(e)

        # break

    def get_crop_imeges(self, frame, boxes):
        crop_images = self.model.get_crop_imeges(frame, boxes)

        crop_images_array = np.array(crop_images)
        crop_images_bytes = BytesIO()
        np.save(crop_images_bytes, crop_images_array, allow_pickle=False)

        return crop_images_bytes.getvalue()


def serve():
    print("server is started!")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    FaceDetection_pb2_grpc.add_FaceDetectionServicer_to_server(FaceDetectioServer(), server)

    server.add_insecure_port('[::]:50053')

    server.start()
    server.wait_for_termination()

    print('server start')
