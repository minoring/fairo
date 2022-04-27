import pickle
import a0

class traj():
    imgs = []
    pose = []

def on_image(pkt):
    traj.imgs.append(pickle.loads(pkt.payload))

def on_pose(pkt):
    traj.pose.append(pickle.load(pkt.payload))

def stop_traj(pkt):
    imgs,pose,traj.imgs, traj.pose = traj.imgs, traj.pose, [], []
    ts = dict(pkt.headers)["a0_time_wall"]
    open(f"/tmp/traj.{ts}").write(pickle.dumps((imgs,pose)))

sub_img = a0.Subscriber("pictures", on_image)
sub_pose = a0.Subscriber("pose", on_pose)
sub_traj_complete = a0.Subscriber("trajectory", stop_traj)#topic for start and stop of traj!)
