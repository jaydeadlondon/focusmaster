import cv2
import mediapipe as mp
import numpy as np
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from ultralytics import YOLO
from loguru import logger


class ErgonomicsMaster:
    def __init__(self, model_path="pose_landmarker_heavy.task"):
        base_options = python.BaseOptions(model_asset_path=model_path)
        options = vision.PoseLandmarkerOptions(
            base_options=base_options, running_mode=vision.RunningMode.VIDEO
        )
        self.landmarker = vision.PoseLandmarker.create_from_options(options)

        self.yolo_model = YOLO("yolo11n.pt")

        self.cap = cv2.VideoCapture(0)
        logger.info("Система готова. Нажми 'q' для выхода.")

    def process_frame(self):
        while self.cap.isOpened():
            success, frame = self.cap.read()
            if not success:
                break

            timestamp_ms = int(self.cap.get(cv2.CAP_PROP_POS_MSEC))
            if timestamp_ms == 0:
                timestamp_ms = int(cv2.getTickCount() * 1000 / cv2.getTickFrequency())

            yolo_results = self.yolo_model(frame, stream=True, conf=0.5, verbose=False)
            for r in yolo_results:
                for box in r.boxes:
                    if self.yolo_model.names[int(box.cls[0])] == "cell phone":
                        cv2.putText(
                            frame,
                            "NO PHONE!",
                            (50, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            (0, 0, 255),
                            3,
                        )

            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
            pose_result = self.landmarker.detect_for_video(mp_image, timestamp_ms)

            if pose_result.pose_landmarks:
                landmarks = pose_result.pose_landmarks[0]

                left_shoulder_y = landmarks[11].y
                right_shoulder_y = landmarks[12].y
                avg_shoulder_y = (left_shoulder_y + right_shoulder_y) / 2

                if avg_shoulder_y > 0.6:
                    cv2.putText(
                        frame,
                        "FIX POSTURE!",
                        (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 255, 255),
                        3,
                    )

            cv2.imshow("VisionGuard 2026", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    try:
        app = ErgonomicsMaster()
        app.process_frame()
    except Exception as e:
        logger.error(f"Ошибка запуска: {e}")
        print(
            "\nПодсказка: Проверь, лежит ли файл 'pose_landmarker_heavy.task' в папке с проектом."
        )
