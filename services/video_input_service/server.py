import cv2
import time
import grpc
from concurrent import futures
import videoinput_pb2
import videoinput_pb2_grpc


class Greeter(videoinput_pb2_grpc.VideoInputServicer):

    # ==========
    def __init__(self):
        pass

    # ==========
    def getStream(self, request_iterator, context):
        

        for req in request_iterator:

            # リクエストメッセージを表示
            print("request message = ", req.msg)
            print(req.msg.split(".")[-1])
            if req.msg.split(".")[-1] == "mp4":
                video_capture = cv2.VideoCapture(req.msg)

                while True:
                    ret, frame = video_capture.read()
                    frame = cv2.resize(frame, (1280, 720))
                    ret, buf = cv2.imencode('.jpg', frame)
                    if ret != 1:
                        print("encode Error")
                        return

                    yield videoinput_pb2.Reply(datas=buf.tobytes())
            
            else:
                frame = cv2.imread(req.msg)
                frame = cv2.resize(frame, (1280, 720))
                ret, buf = cv2.imencode('.jpg', frame)

                yield videoinput_pb2.Reply(datas=buf.tobytes())


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    videoinput_pb2_grpc.add_VideoInputServicer_to_server(Greeter(), server)

    server.add_insecure_port('[::]:50051')

    server.start()
    server.wait_for_termination()

    print('server start')