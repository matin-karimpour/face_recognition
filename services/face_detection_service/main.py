import cv2
import grpc
import numpy as np
import videoinput_pb2
import videoinput_pb2_grpc
from ultralytics import YOLO
import DataProcessing_pb2
import DataProcessing_pb2_grpc
from io import BytesIO


# Load the YOLOv8 model
model = YOLO('yolov8n-face.pt')


def track_faces(model, frame):
    results = model.track(frame, persist=True)

    return results


def get_crop_imeges(frame, boxes):
    crop_images = []
    if boxes is not None:
        for box in boxes:

            crop_obj = frame[int(box[1]):int(box[3]), int(box[0]):int(box[2])]
            crop_obj= cv2.resize(crop_obj, (100,100))
            crop_images.append(crop_obj)
    
    crop_images_array = np.array(crop_images)
    crop_images_bytes = BytesIO()
    np.save(crop_images_bytes, crop_images_array, allow_pickle=False)

    yield DataProcessing_pb2.RequestData(images=crop_images_bytes.getvalue())


def run():
    channel = grpc.insecure_channel('127.0.0.1:50051')
    videoinput_stub = videoinput_pb2_grpc.VideoInputStub(channel)

    DataProcessing_channel = grpc.insecure_channel('127.0.0.1:50052')
    DataProcessing_stub = DataProcessing_pb2_grpc.DataProcessingStub(DataProcessing_channel)


    try:
        message = []
        message.append(videoinput_pb2.Request(msg='give me the stream!!'))
        responses = videoinput_stub.getStream(iter(message))

        for res in responses:
            dBuf = np.frombuffer(res.datas, dtype=np.uint8)

            frame = cv2.imdecode(dBuf, cv2.IMREAD_COLOR)
            results = track_faces(model, frame)
            annotated_frame = results[0].plot()
            track_ids = np.array(results[0].boxes.id.int().cpu().tolist())

            boxes = results[0].boxes.xyxy.cpu().tolist()
            
            ress = DataProcessing_stub.getStream(get_crop_imeges(frame, boxes))
            for res1 in ress:
                print(res1)


            # Display the annotated frame
            cv2.imshow("YOLOv8 Tracking", annotated_frame)

            k = cv2.waitKey(1)
            if k == 27:
                break

    except grpc.RpcError as e:
        print(e)
    # break


if __name__ == '__main__':
    run()
