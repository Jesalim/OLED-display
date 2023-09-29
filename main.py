from machine import Pin, SPI
from ssd1306 import SSD1306_SPI
import framebuf
import machine
import utime

sensor_temp = machine.ADC(28)
conversion_factor = 3.3 / (65535)

WIDTH = 128
HEIGHT = 64

spi = SPI(0, baudrate=10000000, sck=Pin(2), mosi=Pin(3))
print("SPI Configuration:", spi)

oled = SSD1306_SPI(WIDTH, HEIGHT, spi, dc=Pin(4), res=Pin(5), cs=Pin(6))

buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|?\x00\x01\x86@\x80\x01\x01\x80\x80\x01\x11\x88\x80\x01\x05\xa0\x80\x00\x83\xc1\x00\x00C\xe3\x00\x00~\xfc\x00\x00L'\x00\x00\x9c\x11\x00\x00\xbf\xfd\x00\x00\xe1\x87\x00\x01\xc1\x83\x80\x02A\x82@\x02A\x82@\x02\xc1\xc2@\x02\xf6>\xc0\x01\xfc=\x80\x01\x18\x18\x80\x01\x88\x10\x80\x00\x8c!\x00\x00\x87\xf1\x00\x00\x7f\xf6\x00\x008\x1c\x00\x00\x0c \x00\x00\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")

while True:
    reading = sensor_temp.read_u16() * conversion_factor

    fb = framebuf.FrameBuffer(buffer, 32, 32, framebuf.MONO_HLSB)

    oled.fill(0)

    oled.blit(fb, 96, 0)

    oled.text("ADC: ", 5, 8)
    oled.text(str(round(reading, 2)), 40, 8)

    oled.show()

