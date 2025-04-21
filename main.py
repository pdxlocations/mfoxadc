import time
import mudp

ADC_DIR = "/sys/bus/iio/devices/iio:device0"
TEMP_DIR = "/sys/class/thermal/thermal_zone0/temp"

from mudp import (
    conn,
    node,
    send_device_telemetry,
    send_environment_metrics
)

MCAST_GRP = "224.0.0.69"
MCAST_PORT = 4403

node.node_id = "!596ab32e"
node.channel = "MediumFast"
node.key = "AQ=="
conn.setup_multicast(MCAST_GRP, MCAST_PORT)

def read_adc_value(file_path):
    # Read the voltage value from the ADCs
    with open(file_path, "r") as file:
        return file.read().strip()
    
def read_cpu_temperature():
    # Read CPU temperature from the thermal zone
    with open(TEMP_DIR, 'r') as cpu_temp:
        return int(cpu_temp.read()) / 1000
    
OCV = [4190, 4050, 3990, 3890, 3800, 3720, 3630, 3530, 3420, 3300, 3100]
def show_percent(voltage):
    for i in range(len(OCV)):
        if OCV[i] <= voltage:
            if i == 0:
                return 100.0
            else:
                return 100.0 / (len(OCV) - 1) * (len(OCV) - 1 - i + (voltage - OCV[i]) / (OCV[i - 1] - OCV[i]))
    return 0

def main():
    print("Press Ctrl+C to quit")
    while True:
        scale_value = float(read_adc_value(f"{ADC_DIR}/in_voltage_scale"))
        IN0_raw_value = float(read_adc_value(f"{ADC_DIR}/in_voltage0_raw"))
        IN1_raw_value = float(read_adc_value(f"{ADC_DIR}/in_voltage1_raw"))

        IN0_voltage = round(IN0_raw_value * scale_value / 1000, 2)
        IN1_voltage = round(IN1_raw_value * scale_value / 1000, 2)
        temperature = float(read_cpu_temperature())

        print(f"IN0_Voltage: {str(IN0_voltage)} V, IN1_Voltage: {str(IN1_voltage)} V")
        print(f"CPU_Temp: {str(temperature)} °C")
        # r1 = 300
        # r2 = 100
        # voltage =  IN1_voltage * (r1 + r2) /r2

        voltage = round(IN1_voltage * (5.0 / 1.8), 2)
        battery_level = show_percent(voltage)
        
        send_device_telemetry(voltage=voltage, battery_level=battery_level)
        time.sleep(5)
        send_environment_metrics(temperature=temperature)

        time.sleep(10)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
