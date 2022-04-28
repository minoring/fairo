# Copyright (c) Facebook, Inc. and its affiliates.

# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
from ast import For
from logging import RootLogger
import numpy as np
import json
import torch
from scipy.spatial.transform import Rotation as R
from polymetis import RobotInterface
from realsense_wrapper import RealsenseAPI
import cv2
import os

if __name__ == "__main__":
    # Initialize robot interface
    robot = RobotInterface(
        ip_address="172.16.0.1",
    )
    robot.go_home()

    cwd = os.getcwd()
    rs = RealsenseAPI()
    def take_picture():
        imgs = rs.get_rgbd()
        return imgs
        # for i, img in enumerate(imgs):
        #     rgb = img[:,:,:3]
        #     img_path = f'{cwd}/debug/{count}_cam{i}.jpg'
        #     cv2.imwrite(img_path, rgb[:,:,::-1])
        #     img_path_depth = f'{cwd}/debug/{count}_depthCam{i}.jpg'
        #     dimg = img[:,:,3]
        #     cv2.imwrite(img_path_depth, dimg.astype(np.uint8))

    def getEEpose():
        ee_pos, ee_quat = robot.get_ee_pose()
        print(f"Current ee position: {ee_pos}")
        print(f"Current ee orientation: {ee_quat}  (xyzw)")


    #Location of the EE to base
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
        #print(f"rot1: {rot1}, type - {type(rot1)}")
        #print(f"rot1: {rot2}, type - {type(rot2)}")

        cam_quat = rot1 * rot2

        # quat_rot = R.from_rotvec(ee_b_quat)
        # quat_mat = quat_rot.as_matrix()
        # cam_quat = quat_mat.dot()

        return cam_pose, cam_quat


    # def robot_move():
    #     points = open("poses.json")
    #     for i in p['xyz']:
    #         ee_pos_desired = torch.Tensor(i)
    #         for j in p['quat']:
    #             ee_quat_desired = torch.Tensor(j)
    #             state_log = robot.move_to_ee_pose(
    #                 position=ee_pos_desired, orientation=ee_quat_desired, time_to_go=10
    #             )
    # getEEpose()
    # print()

    for i in range(50):
        imgs = take_picture()
        pose_quat = liveloc()
        path = f"/mnt/tmp_nfs_clientshare/jaydv/isdf_data/img_pose_{i}.npy"
        np.save(path, [imgs, pose_quat])
        input("press enter...")


