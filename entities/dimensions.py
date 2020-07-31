from abc import ABC


class Dimensions(ABC):
    def __init__(self, values: list):
        self.__values = values

    @property
    def axis_x(self) -> float:
        return self._get_axis(0)

    @property
    def axis_y(self) -> float:
        return self._get_axis(1)

    @property
    def axis_z(self) -> float:
        return self._get_axis(2)

    def _get_axis(self, index):
        return self.__values[index]
