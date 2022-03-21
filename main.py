import utime as time
from lib.dht import DHT11
from lib.pico_i2c_lcd import I2cLcd
from machine import I2C, Pin

time.sleep(2)  # Waiting for the sensor to start sending pulses
i2c = I2C(id=0, scl=Pin(1), sda=Pin(0), freq=100000)
lcd = I2cLcd(i2c, 0x27, 2, 16)
dhtPIN = 15
dhtSensor = DHT11(Pin(dhtPIN, Pin.OUT, Pin.PULL_DOWN))
led = Pin(17, Pin.OUT)
led.low()
buzzer = Pin(16, Pin.OUT)
buzzer.low()
motion_sensor = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    if motion_sensor.value():
        led.high()
        buzzer.high()
        time.sleep(0.2)
        led.low()
        buzzer.low()
        lcd.display_on()
        fahrenheit = dhtSensor.temperature * 1.8 + 32
        temperature = "Temp: {0:.2f}F".format(fahrenheit)
        humidity = "Hum: {0:.2%}".format(dhtSensor.humidity/100)
        print(temperature, " | ", humidity)
        lcd.move_to(0, 0)
        lcd.putstr(temperature)
        lcd.move_to(0, 1)
        lcd.putstr(humidity)
        time.sleep(5)
        lcd.display_off()
    else:
        print("Waiting for motion...")
        time.sleep(0.2)

