import numpy
import cv2
from djitellopy import Tello
import string
import random


class Drone():
    def __init__(self):
        self.drone = Tello()
        self.drone.connect()
    
    def make_picture(self):
        self.drone.streamoff()
        self.drone.streamon()
        
        try:
            length = 10
            letters = string.ascii_lowercase
            rand_string = ''.join(random.choice(letters) for i in range(length))

            cv2.imwrite(f'media/{rand_string}' + '.jpg', self.drone.get_frame_read().frame)
            self.drone.streamoff()

            return print(f'image {rand_string}.jpg saved')
        except:
            return print('get image error')
    
    def get_video(self):
        self.drone.streamoff()
        self.drone.streamon()

        length = 10
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(length))

        fourcc = cv2.VideoWriter_fourcc(*'MP4V')
        out = cv2.VideoWriter(f'media/{rand_string}.mp4',fourcc, 20.0, (640,480))

        while True:
            frame_read = self.drone.get_frame_read()
            main_frame = frame_read.frame
            cv2.imshow('Main Video', main_frame)
            ch = cv2.waitKey(5)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        out.release()

        self.drone.streamoff()
        cv2.destroyAllWindows()

        return print('video stream ended')
