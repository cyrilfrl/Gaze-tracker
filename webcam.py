import os
import cv2

class Webcam:
    def __init__(self):
        self.directory = ""
        self.cap = cv2.VideoCapture(0)

    def capture(self, id):
        """Take picture with the webcam and save the image under the directory stored in the attributes of the class with the passed id.

        Args:
            id (int): id of the picture
        """
        ret, frame = self.cap.read()

        if ret:
            filename = os.path.join(self.directory, f"{id}.jpg")
            cv2.imwrite(filename, frame)

    def release(self):
        """Release the webcam and destroy all windows."""
        self.cap.release()
        cv2.destroyAllWindows()