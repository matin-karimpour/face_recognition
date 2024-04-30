import cv2
from ultralytics import YOLO


class FaceDetectionModel():
    def __init__(self) -> None:
        # Load the YOLOv8 model
        self.model = YOLO('yolov8n-face.pt')

    def track_faces(self, frame):
        results = self.model.track(frame, persist=True, verbose=False)
        return results

    def get_crop_imeges(self, frame, boxes):
        crop_images = []
        if boxes is not None:
            for box in boxes:
                crop_obj = frame[int(box[1]):int(box[3]), int(box[0]):int(box[2])]
                crop_obj = cv2.resize(crop_obj, (100, 100))
                crop_images.append(crop_obj)

        return crop_images
