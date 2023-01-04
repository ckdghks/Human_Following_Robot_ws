import rospy
import numpy as np
from std_msgs import String
from CalibrationClass import CalibrateImage

def callback(data):

    mtx = CalibrateImage.Calibrate(data)
    print(type(mtx))
    pub.publish(mtx)


rospy.init_node('PubIntrinsicMatrixNode')

sub = rospy.Subscriber("/darknet_ros/bounding_boxes", String, callback)
pub = rospy.Publisher("/PublishIntrinsicMatrixNode/bbox", String, queue_size=10)
rate = rospy.Rate(2)


rospy.spin()
