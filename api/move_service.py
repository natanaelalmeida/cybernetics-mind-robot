import json

from flask import request
from flask_restful import Resource

from core.move_interface import MoveInterface
from factory.motion_detected_factory import MotionDetectedFactory


class MoveService(Resource):

    def __init__(self):
        self.__move_interface = MoveInterface()

    def post(self):
        scalar_acceleration, rotation, angle_acc, angle_disp = self._body()
        motion_detected = MotionDetectedFactory(scalar_acceleration,
                                                rotation,
                                                angle_acc, 
                                                angle_disp).create()

        self.__move_interface.go_to_joint(motion_detected)
        result = json.dumps({"State": 'Move'})
        return json.loads(result)

    @staticmethod
    def _body():
        body = json.loads(request.json)
        scalar_accelerations = body['scalar_accelerations']
        rotations = body['rotations']
        angle_acc = body['angle_acceleration']
        angle_disp = body['angle_displacement']
        return scalar_accelerations, rotations, angle_acc, angle_disp
