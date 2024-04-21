import cv2
import grpc
import numpy as np
import videoinput_pb2
import videoinput_pb2_grpc

def run():
    channel = grpc.insecure_channel('127.0.0.1:50051')
    videoinput_stub = videoinput_pb2_grpc.VideoInputStub(channel)

    try:
        message = []
        message.append(videoinput_pb2.Request(msg='give me the stream!!'))
        responses = videoinput_stub.getStream(iter(message))

        for res in responses:
            dBuf = np.frombuffer(res.datas, dtype=np.uint8)

            frame = cv2.imdecode(dBuf, cv2.IMREAD_COLOR)


            # Display the annotated frame
            cv2.imshow("frame", frame)

            k = cv2.waitKey(1)
            if k == 27:
                break

    except grpc.RpcError as e:
        print(e)
    # break


if __name__ == '__main__':
    run()
