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
    #XYZ with the smaller steps
    x = []
    y = []
    z = []
    quat= []
    def read_file():
        points = open("poses.json")
        p = json.load(points)
        x_temp = []
        y_temp = []
        z_temp = []
        for i in p['xyz']:
            x_temp.append(torch.Tensor(i[0]))
            y_temp.append(torch.Tensor(i[1]))
            z_temp.append(torch.Tensor(i[2]))
        for j in p['quat']:
            quat.append(torch.Tensor(j))
        if len(x_temp) == len(y_temp) == len(z_temp):
            for i in range(len(x_temp)-2):
                x.append(np.linspace(start=x_temp[i], end=x_temp[i+1], num=25))
                y.append(np.linspace(start=y_temp[i], end=y_temp[i+1], num=25))
                z.append(np.linspace(start=z_temp[i], end=z_temp[i+1], num=25))
            count = len(x_temp)
            x.append(np.linspace(start=x_temp[count-2], end=x_temp[count-1], num=25))
            y.append(np.linspace(start=y_temp[count-2], end=y_temp[count-1], num=25))
            z.append(np.linspace(start=z_temp[count-2], end=z_temp[count-1], num=25))

    def move_robot():
        for i in x:
            state_log =  robot.move_to_ee_pose(
                    position=, orientation=ee_quat_desired, time_to_go=10
                )
            