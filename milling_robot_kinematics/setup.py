import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'milling_robot_kinematics'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kousheek',
    maintainer_email='kousheekc@gmail.com',
    description='Package contains the robot FK, IK models and stick figure visualizations with plotly.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'execute_trajectory_node = milling_robot_kinematics.execute_trajectory_node:main',
            'trajectory_generation_node = milling_robot_kinematics.trajectory_generation_node:main',
        ],
    },
)