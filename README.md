
# Craft Status - ROS2 Package

`craft_status` is a ROS2 package designed to monitor the battery status of a robotic system. It includes a node, `bat_mon`, that reads ADC values, calculates battery voltage, and publishes the battery percentage.

## Features

- Reads ADC values from a specified file path.
- Converts ADC values to battery voltage.
- Calculates the battery percentage based on the voltage range of the connected battery.
- Publishes battery status as a ROS2 message.

## Requirements

- ROS2 (Foxy, Galactic, or later)
- Python 3.6 or later

## Installation

1. **Clone the Repository**

   ```bash
   cd ~/ros2_ws/src
   git clone https://github.com/yourusername/craft_status.git
 
