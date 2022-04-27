import pickle
from realsense_wrapper import RealsenseAPI
import a0


p = a0.Publisher("pictures")
rs = RealsenseAPI()
while True:
    imgs = rs.get_rgbd()
    p.pub(pickle.dump(imgs))


        # for i, img in enumerate(imgs):
        #     rgb = img[:,:,:3]
        #     img_path = f'{cwd}/debug/{count}_cam{i}.jpg'
        #     cv2.imwrite(img_path, rgb[:,:,::-1])
        #     img_path_depth = f'{cwd}/debug/{count}_depthCam{i}.jpg'
        #     dimg = img[:,:,3]
        #     cv2.imwrite(img_path_depth, dimg.astype(np.uint16))