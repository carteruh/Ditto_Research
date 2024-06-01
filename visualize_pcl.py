import cv2
import matplotlib.pyplot as plt
import numpy as np
import open3d as o3d
from PIL import Image


def resize_image(image, target_width, target_height):
    return cv2.resize(image, (target_width, target_height), interpolation=cv2.INTER_LINEAR)

def read_depth(RGB_path, depth_path):
    # # Read images using PIL and convert to numpy arrays
    # RGB_img = np.array(Image.open(RGB_path))
    # depth_img = np.array(Image.open(depth_path)).astype(np.float32) * .001


    # # # Ensure RGB image is in uint8 format
    # RGB_img = RGB_img.astype(np.float32)


    RGB_img = o3d.io.read_image(RGB_path)
    depth_img = o3d.io.read_image(depth_path)


    # Create RGBD image
    rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
        o3d.geometry.Image(RGB_img),
        o3d.geometry.Image(depth_img),
        depth_scale=1000,  # Conversion scale if original depth is in meters
        depth_trunc=0.7,  # Maximum truncation in meters
        # convert_rgb_to_intensity=True
    )
    print(rgbd_image)
    return rgbd_image

def read_depth_laptop(depth_path):
    depth_img = np.array(Image.open(depth_path))
    depth_img = depth_img.astype(np.float32) * 0.001

    # depth_scale_factor = 1.0 / 255  # Adjust the 10.0 to your actual max depth in meters
    # depth_img *= depth_scale_factor


    rgbd = o3d.geometry.RGBDImage.create_from_color_and_depth(
        o3d.geometry.Image(np.empty_like(depth_img)),
        o3d.geometry.Image(depth_img),
        depth_scale=1.0,
        depth_trunc=0.7,
        convert_rgb_to_intensity=False,
    )
    return rgbd

if __name__ == '__main__':
    pinhole_camera_intrinsic = o3d.camera.PinholeCameraIntrinsic(
        width=848,
        height=480,
        fx=429.85,
        fy=429.85,
        cx=426.88,
        cy=239.45
    )

    # pinhole_camera_intrinsic = o3d.camera.PinholeCameraIntrinsic(
    #     width=848,
    #     height=480,
    #     fx=645.59,
    #     fy=644.68,
    #     cx=645.07,
    #     cy=364.29
    # )

    intrinsics = o3d.camera.PinholeCameraIntrinsic(
    width=640,
    height=480,
    fx=635.647,
    fy=635.647,
    cx=320.300,
    cy=241.436,
)

#     intrinsics = o3d.camera.PinholeCameraIntrinsic(
#    o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault
# )


    rgbd_laptop = read_depth_laptop('/media/qil/DATA/DITTO_Carter/Ditto/data/ROS_Data/2024-03-25-16-26-56/depth_images/177_depth.png')
    rgbd = read_depth('/media/qil/DATA/DITTO_Carter/Ditto/data/ROS_Data/2024-03-25-16-26-56/color_images/177_bw.png', '/media/qil/DATA/DITTO_Carter/Ditto/data/ROS_Data/2024-03-25-16-26-56/depth_images/177_depth.png')


    pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd, pinhole_camera_intrinsic)

    print(pcd)

    img = Image.open('/media/qil/DATA/DITTO_Carter/Ditto/data/ROS_Data/2024-03-25-16-26-56/color_images/177_bw.png')
    depth = Image.open('/media/qil/DATA/DITTO_Carter/Ditto/data/ROS_Data/2024-03-25-16-26-56/depth_images/177_depth.png')

    # flip the orientation, so it looks upright, not upside-down
    pcd.transform([[1,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,1]])

    o3d.visualization.draw_geometries([pcd])

    # plot images
    plt.gray()
    plt.subplot(1,2, 1)
    plt.title('Grayscale')
    plt.imshow(img, cmap='gray', vmin=0, vmax= 255)
    plt.subplot(1,2, 2)
    plt.title('depth')
    plt.imshow(depth, cmap='gray', vmin=0, vmax= 255)
    plt.show()
