from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'craft_status'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Aswin',
    maintainer_email='aramachandra@ethz.ch',
    description='Package that monitors and publishes all the status information',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'bat_mon = craft_status.bat_mon:main'
        ],
    },
)
