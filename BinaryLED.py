import RPi.GPIO as GPIO
import time

led_pin = [0 for col in range(4)]
led_pin[0] = 18
led_pin[1] = 17 
led_pin[2] = 24
led_pin[3] = 22

GPIO.setmode(GPIO.BCM)

for x in range(len(led_pin)):
	GPIO.setup(led_pin[x], GPIO.OUT)
	print led_pin[x]

char_num = '0123456789'

x = 0
result = ''
while True:
	
	for z in range(len(led_pin)):
		GPIO.output(led_pin[z], False)

	result = ''
	num = int(raw_input("input 0-15: "))
	while num > 0:
		result = char_num[num%2] + result
		num = num/2


	while len(result) != 4:
		result = '0' + result
	print result	
	for pin_num in range(len(result)):
		print result[pin_num]
		if result[pin_num] == '1':
			print led_pin[pin_num]
			GPIO.output(led_pin[pin_num], True)
	time.sleep(1)
