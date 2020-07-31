#from abc import ABC


class Dimensions(object):
    def __init__(self, values):
        self.__values = values

    @property
    def axis_x(self):
        return self._get_axis(0)

    @property
    def axis_y(self):
        return self._get_axis(1)

    @property
    def axis_z(self):
        return self._get_axis(2)

    def _get_axis(self, index):
        return self.__values[index]
