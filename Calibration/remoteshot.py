import signal
from xbox360controller import Xbox360Controller
import cv2
import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

class SaveImageNode(object):
    def __init__(self):
        self.image = None
        self.br = CvBridge()
        
        rospy.init_node('SubImageNode')

        rospy.Subscriber("/camera/camera_nodelet_manager", Image, self.callback)

    def callback(self, msg):
        print(type(msg))
    
        with Xbox360Controller() as controller:
            # Button A events
            if controller.button_a.when_pressed :
                self.image = self.br.imgmsg_to_cv2(msg)
                cv2.imwrite('./images/Calibrate.jpg', self.image)
            
            if controller.button_a.when_released :
                pass

SaveImageNode()
rospy.spin()
