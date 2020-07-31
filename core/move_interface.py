import numpy as np
import sys
import copy
import rospy
import moveit_commander as commander
import moveit_msgs.msg
import geometry_msgs.msg

from entities.motion_detected import MotionDetected


class MoveInterface(object):
    def __init__(self):
        commander.roscpp_initialize(sys.argv)

        self.__robot = commander.RobotCommander()
        self.__scene = commander.PlanningSceneInterface()

        self.__group_name = "panda_arm"
        self.__move_group = commander.MoveGroupCommander(self.__group_name)

        self.__display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                              moveit_msgs.msg.DisplayTrajectory,
                                                              queue_size=20)

        self.__planning_frame = self.__move_group.get_planning_frame()
        self.__eef_link = self.__move_group.get_end_effector_link()
        self.__group_names = self.__robot.get_group_names()

    def go_to_joint(self, motion_detected: MotionDetected):
        joint_goal = self.__move_group.get_current_joint_values()
        joint_goal[0] = 0
        joint_goal[1] = -np.pi/4
        joint_goal[2] = 0
        joint_goal[3] = -np.pi/2
        joint_goal[4] = 0
        joint_goal[5] = motion_detected.rotation.axis_y
        joint_goal[6] = 0

        self.__move_group.set_max_acceleration_scaling_factor(
            motion_detected.scalar_acceleration.axis_y)

        self.__move_group.go(joint_goal, wait=True)
        self.__move_group.stop()
