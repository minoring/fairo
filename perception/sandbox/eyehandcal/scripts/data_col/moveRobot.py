from ipaddress import ip_address
import json
import torch
from polymetis import RobotInterface

def robot_move():
    robot = RobotInterface(ip_address = "172.16.0.1")
    p = a0.Publisher("trajectory")
    points = open("poses.json")
    p = json.load(points)
    for i in p['xyz']:
        ee_pos_desired = torch.Tensor(i)
        for j in p['quat']:
            ee_quat_desired = torch.Tensor(j)
            state_log = robot.move_to_ee_pose(
                position=ee_pos_desired, orientation=ee_quat_desired, time_to_go=10
            )
    
    p.pub("done")