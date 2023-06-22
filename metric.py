from collections import Counter

import numpy as np
from sklearn.metrics import accuracy_score

class Metric:
    def __init__(self):
        self.acc = []
        self.frames = 0

    def calculate_metric(self, el, track_data_length):
        frame_id = el['frame_id']
        track_id_list = []
        cb_id_list = []

        for i in el['data']:
            track_id = i['track_id']
            cb_id = i['cb_id']

            if not track_id:
                track_id = -1

            track_id_list.append(track_id)
            cb_id_list.append(cb_id)

        self.acc.append(accuracy_score(cb_id_list, track_id_list))

        self.frames += 1

        if track_data_length == self.frames:
            print(f"Mean accuracy : {np.mean(np.array(self.acc))}")

    def clean(self):
        self.frames = 0
        self.acc = []
