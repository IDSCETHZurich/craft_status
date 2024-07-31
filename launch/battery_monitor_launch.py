from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='craft_status',
            executable='bat_mon',
            name='battery_monitor',
            output='screen',
            parameters=[
                # Add parameters here if needed
            ]
        ),
    ])