import numpy as np

# Mouth landmark indexes
MOUTH_START = 48
MOUTH_END = 68

def mouth_aspect_ratio(mouth):

    # horizontal distance
    A = np.linalg.norm(mouth[0] - mouth[6])

    # vertical distances
    B = np.linalg.norm(mouth[2] - mouth[10])
    C = np.linalg.norm(mouth[4] - mouth[8])

    mar = A / (B + C)

    return mar