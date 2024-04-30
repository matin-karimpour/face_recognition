import json
import os
from concurrent import futures
from datetime import datetime
from io import BytesIO

import cv2
import grpc
import numpy as np

import DataForwarding_pb2
import DataForwarding_pb2_grpc


class FaceDetectServer(DataForwarding_pb2_grpc.DataForwardingServicer):

    # ==========
    def __init__(self):
        self.log_dir = "./log/"
        self.image_log_dir = os.path.join(self.log_dir, "images/")
        print(self.image_log_dir)
        os.makedirs(os.path.dirname(self.image_log_dir), exist_ok=True)
        self.log_path = os.path.join(self.log_dir, "log.json")
        if not os.path.exists(self.log_path):
            os.mknod(self.log_path)

    # ==========
    def getStream(self, request, context):

        with open(self.log_path, "r") as outfile:
            try:
                log = json.load(outfile)
            except:
                log = {}

        np_bytes = BytesIO(request.images)
        images = np.load(np_bytes, allow_pickle=False)
        iamge_path = self.save_image(img=images, track_id=request.track_ids)

        log_id = log.get(str(request.track_ids), {"frames": [], "images": []})
        log_id["frames"].append(str(request.frame_index / 25) + " s")

        log_id["images"].append(str(iamge_path))
        log_id["images"] = list(set(log_id["images"]))
        log[str(request.track_ids)] = log_id

        with open(self.log_path, "w") as outfile:
            json.dump(log, outfile)

        return DataForwarding_pb2.ReplyForward(msg=1)

    def save_image(self, img, track_id):
        dir_time = datetime.now().strftime("%m_%d_%Y")
        output_dir_path = os.path.join(self.image_log_dir, dir_time)
        dir_time = datetime.now().strftime("%H_%M_%S")
        path = os.path.join(output_dir_path, dir_time)
        os.makedirs(path, exist_ok=True)
        path = os.path.join(path, f"{track_id}.jpg")

        if os.path.exists(path):
            return path
        else:
            print("saved")
            cv2.imwrite(path, img=img)
            return path


def serve():
    print('server start')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    DataForwarding_pb2_grpc.add_DataForwardingServicer_to_server(FaceDetectServer(), server)

    server.add_insecure_port('[::]:50054')

    server.start()
    server.wait_for_termination()
