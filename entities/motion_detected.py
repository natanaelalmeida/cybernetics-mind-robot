from entities.dimensions import Dimensions


class MotionDetected(object):
    def __init__(self, scalar_acceleration: Dimensions, rotations: Dimensions):
        self.__scalar_acceleration = scalar_acceleration
        self.__rotations = rotations

    @property
    def scalar_acceleration(self) -> Dimensions:
        return self.__scalar_acceleration

    @property
    def rotation(self) -> Dimensions:
        return self.__rotations
