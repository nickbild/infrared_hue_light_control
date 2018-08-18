import RPi.GPIO as GPIO
from time import sleep

RESOLUTION = 0.000040		# Resolution of pulse timings, in seconds
MAX_TIME = 1			# Maximum allowable time for a pulse, in seconds.
CAPTURE_LIMIT = 31		# Number of pulse pairs (high/low) to consider.

GPIO.setmode(GPIO.BCM)

def get_pulse_time(state, ir_pin):
	time = 0.0
	while (GPIO.input(ir_pin) == state):
		time += RESOLUTION
		sleep(RESOLUTION)

		if time >= MAX_TIME:
			break

	time = round(time, 4)
	return time
			

def capture_code(ir_pin):
	GPIO.setup(ir_pin, GPIO.IN)

	timings = []
	while True:
		high_time = get_pulse_time(1, ir_pin)
		low_time = get_pulse_time(0, ir_pin)

		if high_time != 0 and low_time != 0:
			timings.append([high_time, low_time])

		if len(timings) >= CAPTURE_LIMIT:
			break

	# The first timing is inaccurate, depending on when during the
	# initial high pulse the get_pulse_time function starts.
	return timings[1:]

