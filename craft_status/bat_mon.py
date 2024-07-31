import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class BatteryMonitor(Node):

    def __init__(self):
        super().__init__('bat_mon')
        self.publisher_ = self.create_publisher(Float32, 'battery_percentage', 10)
        self.publisher_1 = self.create_publisher(Float32, 'battery_measurement', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)  # Publish every second
        self.adc_path = '/sys/bus/i2c/drivers/ltc2471/1-0014/iio:device0/in_voltage_raw'
        self.adc_ref_voltage = 1.25
        self.voltage_divider_ratio = 20.231
        self.adc_max_value = 65535  # 16-bit ADC

    def timer_callback(self):
        try:
            # Read the raw ADC value
            with open(self.adc_path, 'r') as f:
                adc_value = int(f.read().strip())

            # Calculate the battery voltage
            battery_voltage = (self.adc_ref_voltage / self.adc_max_value) * self.voltage_divider_ratio * adc_value

            # Convert battery voltage to percentage (Example for a LiPo 6S1P battery with 25.2V full and 18.0V empty)
            max_voltage = 25.2
            min_voltage = 18.0
            battery_percentage = ((battery_voltage - min_voltage) / (max_voltage - min_voltage)) * 100
            battery_percentage = max(0, min(battery_percentage, 100))  # Clamp to [0, 100] range

            # Publish the battery percentage
            msg = Float32()
            msg1 = Float32()
            msg.data = float(battery_percentage)
            msg1.data = float(battery_voltage)
            self.publisher_.publish(msg)
            self.publisher_1.publish(msg1)
            self.get_logger().info(
                f'Battery Voltage: {battery_voltage:.2f}V, Battery Percentage: {battery_percentage:.2f}%')

        except Exception as e:
            self.get_logger().error(f'Error reading ADC value: {e}')


def main(args=None):
    rclpy.init(args=args)
    battery_monitor = BatteryMonitor()
    rclpy.spin(battery_monitor)
    battery_monitor.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
