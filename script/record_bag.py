#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import rosbag
from sensor_msgs.msg import Image, CompressedImage

class Camera():
    def __init__(self):
        self.image_subscriber = rospy.Subscriber("/image_raw", Image, self.image_callback)
        self.bag = rosbag.Bag('test.bag', 'w')

    def image_callback(self, data):
        self.bag.write("/image", data)

if __name__ == "__main__":
    rospy.init_node("record_camera")

    camera = Camera()

    rate = rospy.Rate(50)
    while not rospy.is_shutdown():
        rate.sleep()
    
    camera.bag.close()
    rospy.spin()