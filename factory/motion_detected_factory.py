from entities.dimensions import Dimensions
from entities.motion_detected import MotionDetected


class MotionDetectedFactory(object):
    def __init__(self, scalar_acceleration, rotations, angle_acc, angle_displacement):
        self.__scalar_acceleration = scalar_acceleration
        self.__rotations = rotations
        self.__angle_acc = angle_acc
        self.__angle_displacement = angle_displacement

    def create(self):
        scalar_acceleration = Dimensions(values=self.__scalar_acceleration)
        rotation = Dimensions(values=self.__rotations)

        return MotionDetected(scalar_acceleration=scalar_acceleration,
                              rotations=rotation,
                              angle_acc=self.__angle_acc,
                              angle_displacement=self.__angle_displacement)

