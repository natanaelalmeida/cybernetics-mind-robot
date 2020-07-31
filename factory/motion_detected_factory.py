from entities.dimensions import Dimensions
from entities.motion_detected import MotionDetected


class MotionDetectedFactory(object):
    def __init__(self, scalar_acceleration: list, rotations: list):
        self.__scalar_acceleration = scalar_acceleration
        self.__rotations = rotations

    def create(self) -> MotionDetected:
        scalar_acceleration = Dimensions(values=self.__scalar_acceleration)
        rotation = Dimensions(values=self.__rotations)

        return MotionDetected(scalar_acceleration=scalar_acceleration,
                              rotations=rotation)

