from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture

import cv2
from cv2 import aruco
import numpy as np
from tuya_connector import *
import pandas as pd
import datetime
import random
import time


class ArucoDetectorApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.image_widget = Image()
        self.layout.add_widget(self.image_widget)

        # Inicialize a captura de vídeo usando a webcam (ou outro dispositivo de vídeo)
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 600)
        self.cap.set(4, 500)
        Clock.schedule_interval(self.update, 1.0 / 30.0)  # Atualiza a cada 1/30 de segundo

        return self.layout

    def update(self, dt):
        ret, frame = self.cap.read()

        marker_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
        param_markers = aruco.DetectorParameters_create()

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners, ids, rejected = aruco.detectMarkers(gray_frame, marker_dict, parameters=param_markers)

        if ids is not None and len(ids) > 0:
            aruco.drawDetectedMarkers(frame, corners)

            c1 = (corners[0][0][0][0], corners[0][0][0][1])
            c2 = (corners[0][0][1][0], corners[0][0][1][1])
            c3 = (corners[0][0][2][0], corners[0][0][2][1])
            c4 = (corners[0][0][3][0], corners[0][0][3][1])

            image = cv2.imread('amor.png')
            shape_image = image.shape

            marker_aruco = np.array([c1, c2, c3, c4])
            marker_image = np.array([
                [0, 0],
                [shape_image[1] - 1, 0],
                [shape_image[1] - 1, shape_image[0] - 1],
                [0, shape_image[0] - 1]
            ], dtype=float)

            h, _ = cv2.findHomography(marker_image, marker_aruco)

            perspectiva = cv2.warpPerspective(image, h, (frame.shape[1], frame.shape[0]))
            cv2.fillConvexPoly(frame, marker_aruco.astype(int), 0, 16)
            frame = frame + perspectiva


        frame = cv2.flip(frame, 0)
        buffer = frame.tobytes()
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.image_widget.texture = texture


    def on_stop(self):
        # Libere os recursos (webcam, etc.) ao fechar o aplicativo
        self.cap.release()


if __name__ == '__main__':
    ArucoDetectorApp().run()
