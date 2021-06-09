class Camera:
    counter = 0

    def __init__(self):
        print('New cam add')
        self._is_on = False
        self.counter += 1
        self.__working_time = 10

    def turn(self, is_on: str):
        self.is_on = is_on

    def sent_data(self):
        print('Data sent')


class Recognizer:
    def __init__(self, path):
        self.model = 'NN'
        print('Recognizer!!')

    def get_people_in_frame(self, frame=None):
        print('Someone detected!')


class HumanCamera(Camera, Recognizer):
    def recognize_drinkers(self):
        print('No one founded')
    def sent_data(self):
        print('Message: no one founded')

camera_Tverskaya_street = Camera()
camera_Pushk_street = HumanCamera()
camera_Lenina_street = HumanCamera()
# # print(camera_Tverskaya_street._is_on)
camera_Tverskaya_street.turn(True)
# # print(camera_Tverskaya_street._is_on)
# # print(Camera.counter)
# # print(camera_Tverskaya_street._Camera__working_time)
# camera_Pushk_street.sent_data()
# camera_Pushk_street.get_people_in_frame()