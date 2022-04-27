import pickle
#from polymetis import RobotInterface
import a0
from time import sleep
from move_robot_collect_data import liveloc


p = a0.Publisher("pose")
#r = RobotInterface("172.16.0.1")
while True:
    #imgs = rs.get_rgbd()
    pose_quat = liveloc()
    p.pub(pickle.dump(pose_quat))
    sleep(1/30)