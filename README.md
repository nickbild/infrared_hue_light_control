# Infrared Philips Hue Light Control

Control Philips Hue lights with any infrared remote control.

## Dependencies

Python 2.7  
https://github.com/nickbild/hue_light_control  
ConfigParser  
RPi.GPIO

## Usage

Configure the GPIO input pin number your IR decoder is attached to, and set the path to
your installation of `hue_light_control` in `params.cfg`.  Then run:

`python control_lights.py`

## Hardware

You'll need an IR sensor, such as TSOP38238.

Wire it up to your single board computer or microcontroller similar to the image below.

![wiring diagram](https://raw.githubusercontent.com/nickbild/infrared_hue_light_control/master/readme/ir_decoder.jpg)

## About the Author

https://nickbild79.firebaseapp.com/#!/

