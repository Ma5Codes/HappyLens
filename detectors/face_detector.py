import cv2
import dlib

class FaceDetector:

    def __init__(self):
        self.detector = dlib.get_frontal_face_detector()

    def detect(self, gray_frame):

        faces = self.detector(gray_frame)

        return faces