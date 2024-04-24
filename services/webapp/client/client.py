import grpc
import numpy as np
import cv2
import videoinput_pb2
import videoinput_pb2_grpc
import FaceDetection_pb2
import FaceDetection_pb2_grpc
import DataProcessing_pb2
import DataProcessing_pb2_grpc
import DataForwarding_pb2
import DataForwarding_pb2_grpc

from io import BytesIO
def get_faces(frame):
     faces = FaceDetection_pb2.RequestData(frame=frame)
     print(faces)
     yield  faces

def run(msg, action):
    channel = grpc.insecure_channel('127.0.0.1:50051')
    videoinput_stub = videoinput_pb2_grpc.VideoInputStub(channel)
    FaceDetection_channel = grpc.insecure_channel('127.0.0.1:50053')
    FaceDetection_stub = FaceDetection_pb2_grpc.FaceDetectionStub(FaceDetection_channel)

    DataProcessing_channel = grpc.insecure_channel('127.0.0.1:50052')
    DataProcessing_stub = DataProcessing_pb2_grpc.DataProcessingStub(DataProcessing_channel)

    DataForwarding_channel = grpc.insecure_channel('127.0.0.1:50054')
    DataForwarding_stub = DataForwarding_pb2_grpc.DataForwardingStub(DataForwarding_channel)


    try:
        message = []
        message.append(videoinput_pb2.Request(msg=msg))
        responses = videoinput_stub.getStream(iter(message))
        init = True
        for index, res in enumerate(responses):
            dBuf = np.frombuffer(res.datas, dtype=np.uint8)

            frame = cv2.imdecode(dBuf, cv2.IMREAD_COLOR)
            request_face = FaceDetection_pb2.RequestData(frame=res.datas)
            response_face = FaceDetection_stub.getStream(request_face)
            np_bytes = BytesIO(response_face.ids)
            ids = np.load(np_bytes, allow_pickle=False)
                    
            
            response_data = DataProcessing_pb2.RequestFace(images=response_face.faces,
                                                           action=action, 
                                                           name=msg.split("/")[-1].split(".")[0],
                                                           track_ids=response_face.ids,
                                                           frame_index=index)
            message_data = DataProcessing_stub.getStream(response_data)
            if message_data.msg == 1:
                RequestForward = DataForwarding_pb2.RequestForward(frame_index=index, 
                                                  track_ids=message_data.track_id,
                                                  images=message_data.image)
                DataForwarding_stub.getStream(RequestForward)
                print(message_data.track_id)
                yield f"<br> POI found in {index/25}s Please Check log directory"
            else: 
                if init:
                    init = False
                    yield "Searching... <br> If POI found We will notify you"
                else:
                    yield ""
            

    except grpc.RpcError as e:
        print(e)
        # break

if __name__ == "__main__":

    for i in run('/service/files/face-3.jpg', "insert"):
        pass
    for i in run('/service/files/task-video.mp4', "search"):
        print(i)