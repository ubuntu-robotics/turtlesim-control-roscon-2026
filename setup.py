from setuptools import setup

package_name = 'turtlesim_control_roscon_2026'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Guillaume beuzeboc',
    maintainer_email='guillaume.beuzeboc@canonical.com',
    description='Simple ROS 2 Jazzy Python node that drives turtlesim in a square.',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'draw_square = turtlesim_control_roscon_2026.draw_square:main',
        ],
    },
)
