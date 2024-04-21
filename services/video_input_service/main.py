# importing the cv2 library
import cv2
import time
import grpc
from concurrent import futures
import videoinput_pb2
import videoinput_pb2_grpc

captureBuffer = None
path: str = "../../files/task-video.mp4"


class Greeter(videoinput_pb2_grpc.VideoInputServicer):

    # ==========
    def __init__(self):
        pass

    # ==========
    def getStream(self, request_iterator, context):
        video_capture = cv2.VideoCapture(path)

        for req in request_iterator:

            # リクエストメッセージを表示
            print("request message = ", req.msg)

            while True:
                ret, frame = video_capture.read()
                ret, buf = cv2.imencode('.jpg', frame)
                if ret != 1:
                    print("encode Error")
                    return

                yield videoinput_pb2.Reply(datas=buf.tobytes())

                # 60FPS
                time.sleep(1 / 60)


def serve(path: str = "../files/task-video.mp4"):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    videoinput_pb2_grpc.add_VideoInputServicer_to_server(Greeter(), server)

    server.add_insecure_port('[::]:50051')

    server.start()
    server.wait_for_termination()

    print('server start')


#============================================================
# main
#============================================================
if __name__ == '__main__':
    serve()
