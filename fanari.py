from gpiozero import LED
from time import sleep

yellow=LED(17)
green=LED(27)
red=LED(22)
yellow.off()
green.off()
red.off()
while True:
  green.on()
  sleep(10)
  green.off()
  yellow.on()
  sleep(2)
  yellow.off()
  red.on()
  sleep(15)
  red.off()
