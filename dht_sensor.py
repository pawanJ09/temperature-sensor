from machine import Pin
import utime as time
from dht import DHT11, InvalidChecksum
from pico_i2c_lcd import I2cLcd
from machine import I2C, Pin

i2c = I2C(id=0, scl=Pin(1), sda=Pin(0), freq=100000)
lcd = I2cLcd(i2c, 0x27, 2, 16)
dhtPIN = 15
dhtSensor = DHT11(Pin(dhtPIN, Pin.OUT, Pin.PULL_DOWN))

while True:
    fahrenheit = dhtSensor.temperature * 1.8 + 32
    temperature = "Temp: {0:.2f}°F".format(fahrenheit)
    humidity = "Hum: {0:.2%}".format(dhtSensor.humidity/100)
    print(temperature, " | ", humidity)
    lcd.move_to(0, 0)
    lcd.putstr(temperature)
    lcd.move_to(0, 1)
    lcd.putstr(humidity)
    time.sleep(1.1)
    lcd.clear()
