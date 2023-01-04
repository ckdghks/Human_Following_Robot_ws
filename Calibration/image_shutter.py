#! /usr/bin/python3
# Copyright (c) 2015, Rethink Robotics, Inc.

# Using this CvBridge Tutorial for converting
# ROS images to OpenCV2 images
# http://wiki.ros.org/cv_bridge/Tutorials/ConvertingBetweenROSImagesAndOpenCVImagesPython

# Using this OpenCV2 tutorial for saving Images:
# http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html

# rospy for the subscriber
import rospy
# ROS Image message
from sensor_msgs.msg import Image
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2

import os
from sensor_msgs.msg import Joy

# Instantiate CvBridge
bridge = CvBridge()



shutter = 0
image_cout = 0
def file_name(image_cout):
    number = len(str(image_cout))
    zero_number = 4 - number
    result = ""
    for i in range(0,zero_number):
        result = result + '0'
    result = result + str(image_cout)
    return result
    
print("Ready to press joystic R1!")
def image_callback(msg):
    global shutter
    #key = cv2.waitKey() 
    try:
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    except (CvBridgeError, e):
        print(e)
    else:
        time = msg.header.stamp 
        if shutter == 1: 
            path = "/home/ros/catkin_ws/src/sensor_pkg/src/image_shutter/intrinsic_data/lwir/1_1"
            
            # ROS TIME
            #cv2.imwrite(os.path.join(path,''+str(time)+'.jpg'), cv2_img)
            
            # cout
            number_str = file_name(image_cout)
            cv2.imwrite(os.path.join(path, number_str+'.jpg'), cv2_img)
            
            print("image saved!!!! number : %s "%number_str);
            shutter = 0


t = 0
def joy_callback(msg):
    global t, shutter, image_cout
    if t == 0 and msg.buttons[5] == 1:
        t = 1
    if t == 1 and msg.buttons[5] == 0:
        image_cout = image_cout + 1
        shutter = 1
        t = 0
    #print("t:%d  b:%d" %(t,msg.buttons[7]))


def main():
    rospy.init_node('image_shutter')
    # Define your image topic
    image_topic = "/lwir1/image_raw"
    # Set up your subscriber and define its callback
    rospy.Subscriber('joy', Joy, joy_callback)
    rospy.Subscriber(image_topic, Image, image_callback)
    # Spin until ctrl + c
    rospy.spin()


if __name__ == '__main__':
    main()
