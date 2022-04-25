from ast import For
from logging import RootLogger
import numpy as np
import json
from scipy.spatial.transform import Rotation as R

from polymetis import RobotInterface



if __name__ == "__main__":
    # Initialize robot interface
    robot = RobotInterface(
        ip_address="172.16.0.1",
    )
    points = open("poses.json")
    p = json.load(points)
    robot.go_home()

    def getEEpose():
        ee_pos, ee_quat = robot.get_ee_pose()
        print(f"Current ee position: {ee_pos}")
        print(f"Current ee orientation: {ee_quat}  (xyzw)")

    def get_ee_b():
        ee_pos, ee_quat = robot.get_ee_pose()
        return ee_pos, ee_quat

    def get_c_ee():
        cam = open("calibrationEEcam.json")
        c = json.load(cam)
        c_ee_pos = []
        c_ee_quat = []
        for pos in c:
            for i in pos['camera_ee_pos']:
                c_ee_pos.append(i)

        for quat in c:
            for i in quat['camera_ee_ori_rotvec']:
                c_ee_quat.append(i)

        return c_ee_pos, c_ee_quat


    def liveloc():
        ee_b_pos, ee_b_quat = get_ee_b()
        c_ee_pos, c_ee_rotvec = get_c_ee()
        rot = R.from_rotvec(c_ee_rotvec)
        rot_matrix = rot.as_matrix()
        cam_pose = rot_matrix.dot(ee_b_pos) + c_ee_pos

        # cam_quat = ee_b_quat * c_ee_quat
        rot1 = R.from_quat(ee_b_quat).as_quat()
        rot2 = R.from_rotvec(c_ee_rotvec).as_quat()
        print(f"rot1: {rot1}, type - {type(rot1)}")
        print(f"rot1: {rot2}, type - {type(rot2)}")

        cam_quat = rot1 * rot2

        # quat_rot = R.from_rotvec(ee_b_quat)
        # quat_mat = quat_rot.as_matrix()
        # cam_quat = quat_mat.dot()

        print(f"Cam pose: {cam_pose}")
        print("------------------------------")
        print(f"Rot Quat: {cam_quat}")
getEEpose()
print("##################################################")
liveloc()