from entities.dimensions import Dimensions


class MotionDetected(object):
    def __init__(self, scalar_acceleration, rotations, angle_acc, angle_displacement):
        self.__scalar_acceleration = scalar_acceleration
        self.__rotations = rotations
        self.__angle_acc = angle_acc
        self.__angle_displacement = angle_displacement

    @property
    def scalar_acceleration(self):
        return self.__scalar_acceleration

    @property
    def rotation(self):
        return self.__rotations

    @property
    def angle_acceleration(self):
        return self.__angle_acc

    @property
    def angle_displacement(self):
        return self.__angle_displacement
