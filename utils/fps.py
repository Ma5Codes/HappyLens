import time

class FPS:
    def __init__(self):
        self.start_time = None
        self.frame_count = 0

    def start(self):
        self.start_time = time.time()

    def update(self):
        self.frame_count += 1

    def get_fps(self):
        elapsed = time.time() - self.start_time
        return self.frame_count / elapsed if elapsed > 0 else 0