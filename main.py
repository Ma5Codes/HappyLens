import cv2
import config

from detectors.face_detector import FaceDetector
from detectors.smile_detector import SmileDetector
from utils.fps import FPS

def main():

    cap = cv2.VideoCapture(config.CAMERA_INDEX)

    face_detector = FaceDetector()
    smile_detector = SmileDetector()

    fps = FPS()
    fps.start()

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_detector.detect(gray)

        for face in faces:

            x1 = face.left()
            y1 = face.top()
            x2 = face.right()
            y2 = face.bottom()

            smiling, ratio, mouth = smile_detector.detect_smile(gray, face)

            color = (0,255,0) if smiling else (0,0,255)

            cv2.rectangle(frame,(x1,y1),(x2,y2),color,2)

            text = "Smiling" if smiling else "Neutral"

            cv2.putText(
                frame,
                f"{text} | Ratio:{ratio:.2f}",
                (x1,y1-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                color,
                2
            )

        fps.update()

        cv2.putText(
            frame,
            f"FPS: {fps.get_fps():.2f}",
            (20,30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255,255,0),
            2
        )

        cv2.imshow("Smile Detection System", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()