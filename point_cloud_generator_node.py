#!/usr/bin/env python

import rospy
from sensor_msgs.msg import PointCloud2, PointField
import sensor_msgs.point_cloud2 as pc2
from rospy.exceptions import ROSInterruptException

def create_and_publish_point_cloud(points, topic_name='/point_cloud', publish_rate=1.0):
    # Initialize the ROS node
    rospy.init_node('point_cloud_node', anonymous=True)
    
    # Create a publisher for the point cloud topic
    pub = rospy.Publisher(topic_name, PointCloud2, queue_size=10)
    
    # Set the publish rate
    rate = rospy.Rate(publish_rate)
    
    while not rospy.is_shutdown():
        # Define the message fields
        fields = [PointField('x', 0, PointField.FLOAT32, 1),
                  PointField('y', 4, PointField.FLOAT32, 1),
                  PointField('z', 8, PointField.FLOAT32, 1)]
        
        # Create the point cloud message
        point_cloud_msg = pc2.create_cloud(header=rospy.Header(frame_id='map'), fields=fields, points=points)
        
        # Publish the PointCloud2 message on the topic
        pub.publish(point_cloud_msg)
        
        rospy.loginfo(f"Published a point cloud message with {len(points)} points on topic '{topic_name}'")
        
        # Sleep for the specified time
        rate.sleep()

if __name__ == '__main__':
    try:
        # Call the function with three example points and a publish rate of 1 Hz
        points = [  [3.0, 1.0, 0.0], [3.0,5.0, 1.0], [9, 1, 2.0], [9,1,-1], [9,0.5,0]
        #[0.0, 0.0, 1.0] , [9.0, 0.0, 1.0], [9.0,9.0,1.0],
        ]
        create_and_publish_point_cloud(points, publish_rate=10.0)
    except ROSInterruptException:
        pass
