import dlib
import numpy as np
from utils.landmarks import mouth_aspect_ratio, MOUTH_START, MOUTH_END
import config

class SmileDetector:

    def __init__(self):

        self.predictor = dlib.shape_predictor(config.MODEL_PATH)

    def detect_smile(self, gray, face):

        shape = self.predictor(gray, face)

        coords = np.zeros((68, 2), dtype="int")

        for i in range(68):
            coords[i] = (shape.part(i).x, shape.part(i).y)

        mouth = coords[MOUTH_START:MOUTH_END]

        mar = mouth_aspect_ratio(mouth)

        smiling = mar > config.SMILE_THRESHOLD

        return smiling, mar, mouth