from ir_capture import capture_code
from ir_decode_sanyo import decode
from time import sleep
import subprocess
import sys
import os
import ConfigParser

config = ConfigParser.ConfigParser()
config.read(os.path.abspath(os.path.dirname(sys.argv[0])) + '/params.cfg')
ir_sensor_pin = int(config.get('general', 'ir_sensor_pin'))
hue_light_control_dir = config.get('general', 'hue_light_control_dir')

print "Starting IR light control server."
while True:
	print "Waiting for IR signal..."
	timings = capture_code(ir_sensor_pin)
	light_id = decode(timings)

	status = subprocess.check_output("python " + hue_light_control_dir + "light_control.py list", shell=True)
	print "Current status of lights:\n" + status

	lights = {}
	for light in status.split("\n"):
		lightAry = light.split(":")
		if len(lightAry) == 4:
			lights[int(lightAry[0])] = lightAry[1]

	if lights[light_id] == "True":
		print "Turning light off."
		print subprocess.check_output(["python", hue_light_control_dir + "light_control.py", "state", str(light_id), "off"])
	elif lights[light_id] == "False":
		print "Turning light on."
		print subprocess.check_output(["python", hue_light_control_dir + "light_control.py", "state", str(light_id), "on"])

	# Make sure previous IR signal isn't bleeding over into next capture.
	sleep(0.2)

