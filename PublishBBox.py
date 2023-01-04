import rospy
from darknet_ros_msgs.msg import BoundingBoxes
from std_msgs.msg import String
from GetObjFunc import BoundingBoxClass

def callback(data):

    obj = BoundingBoxClass.get_Object(data.bounding_boxes)
    print(type(obj))
    pub.publish(obj)


rospy.init_node('PublishBBoxNode')

sub = rospy.Subscriber("/darknet_ros/bounding_boxes", BoundingBoxes, callback)
pub = rospy.Publisher("/PublishBBoxNode/bbox", String, queue_size=10)
rate = rospy.Rate(2)


rospy.spin()
