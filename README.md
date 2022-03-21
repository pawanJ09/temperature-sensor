# Thermostat Sensor

This is my small DIY home project for creating a Home Temperature and Humidity Sensor using 
Raspberry Pi Pico and Micropython. The DHT11 device will sense the temperature and humidity of 
the room and display it on the LCD. This is also integrated with a PIR motion sensor so the LCD 
will display the current room temperature when the device senses you coming near it 
to see the temperature on the LCD.


## Requirements

- [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/)
- DHT11 Temperature Humidity sensor
- 16x2 I2C LCD
- Jumper cables with M-M and M-F connectors
- Breadboard
- PIR Motion Sensor
- 3V Buzzer
- 3V LED
- 330 ohms resistor


## Pin Diagram

<img src="temperature-sensor-pin-diagram.png">


## Running the application locally

Follow the pin diagram and complete the setup. After completing your setup connect your 
Raspberry Pi Pico to your laptop/computer using a USB-C cable and run the main.py program.


## Shutdown constantly running program

When you plugin your Raspberry Pi Pico to a power source main.py will start running. To stop 
this program from continuously running press the BOOTSEL button and plugin the USB-C so that the 
Raspberry Pi Pico appears as a drive. Now go to the drive and copy the flash_nuke.uf2 file to 
clear old contents.

[Flash Nuke UF2 File](https://datasheets.raspberrypi.com/soft/flash_nuke.uf2)





