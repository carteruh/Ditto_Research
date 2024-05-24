# Use ros_env by doing mamba activate ros_env (Reference from RoboStack)
import os

import cv2
import numpy
import rospy
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image

rospy.init_node('image_saver', anonymous=True)
bridge = CvBridge()

# Make sure to create the folders for saving images
color_images_dir = "/media/qil/DATA/DITTO_Carter/Ditto/data/ROS_Data/2024-03-25-16-27-40/color_images"
depth_images_dir = "/media/qil/DATA/DITTO_Carter/Ditto/data/ROS_Data/2024-03-25-16-27-40/depth_images"
os.makedirs(color_images_dir, exist_ok=True)
os.makedirs(depth_images_dir, exist_ok=True)

# Initialize counters
color_idx = 0
depth_idx = 0

def resize_image(image, target_width, target_height):
    return cv2.resize(image, (target_width, target_height), interpolation=cv2.INTER_AREA)

# Callback function for color image subscriber
def color_image_callback(data):
    global color_idx
    try:
        # Convert ROS image to OpenCV image
        cv_image = bridge.imgmsg_to_cv2(data, "mono8")
        cv_image = resize_image(cv_image, 848, 480)
        # Save OpenCV image as a .png file
        cv2.imwrite(os.path.join(color_images_dir, f"{color_idx}_bw.png"), cv_image)
        rospy.loginfo(f"Saved {color_idx}_bw.png")
        color_idx += 1
    except CvBridgeError as e:
        rospy.logerr(e)

# Callback function for depth image subscriber
def depth_image_callback(data):
    global depth_idx
    try:
        # Convert ROS image to OpenCV image
        cv_image = bridge.imgmsg_to_cv2(data, desired_encoding= "passthrough")
        print(f'min: {cv_image.min()}, max: {cv_image.max()}')
        # Normalize the depth image for representation
        # cv_image_normalized = cv2.normalize(cv_image, cv_image, 0, 1000, cv2.NORM_MINMAX)
        # Save OpenCV image as a .png file
        cv2.imwrite(os.path.join(depth_images_dir, f"{depth_idx}_depth.png"), cv_image)
        rospy.loginfo(f"Saved {depth_idx}_depth.png")
        depth_idx += 1
    except CvBridgeError as e:
        rospy.logerr(e)

# Define subscribers
color_sub = rospy.Subscriber('/camera/color/image_raw', Image, color_image_callback)
depth_sub = rospy.Subscriber('/camera/depth/image_rect_raw', Image, depth_image_callback)

# Keep the script alive
rospy.spin()
