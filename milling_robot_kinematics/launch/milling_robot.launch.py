from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    ld = LaunchDescription()

    ld.add_action(Node(
        package="milling_robot_kinematics",
        executable="control_node",
    ))

    ld.add_action(IncludeLaunchDescription(
        PathJoinSubstitution([FindPackageShare('milling_robot_description'), 'launch', 'display.launch.py']),
        launch_arguments={
            'gui': 'false'}.items()
    ))

    return ld