# SenseHatManager
This repository contains a Python script that uses the Sense Hat and the Philips Hue Bridge to control lights connected to the bridge. The script uses the Bridge class from the Bridge.py file to control the lights and the SenseHat class from the sense_hat library to interact with the Sense Hat.

## Hardware Setup
![image](https://user-images.githubusercontent.com/88910492/207051605-f3dbafa1-f166-432c-afb0-702207988a7b.png)

The hardware setup for this project involves using a `Raspberry Pi` with a `Sense HAT` attached to it. The Sense HAT is a small add-on board that allows the Raspberry Pi to sense the environment, including temperature, humidity, and air pressure.

## Getting Started
Make sure you have a Raspberry Pi with a Sense Hat and a Philips Hue Bridge set up and connected to the same network as the Raspberry Pi.
Replace BRIDGE_IP and USERNAME in the Bridge class with the IP address and username of your Philips Hue Bridge.
Run the script with python sense_hat_manager.py.

## Functionality
The script uses the Sense Hat joystick to control the lights connected to the Philips Hue Bridge.
The script can be used to change the brightness of the lights and change the color of the lights using the RGB color model.
The script uses the Bridge class to control the lights and the SenseHat class to interact with the Sense Hat.
The script allows to control 14 lights by default
The script uses the rgb_to_xy function to convert RGB colors to the xy colorspace used by the Philips Hue Bridge.

## Dependencies
- Bridge
- sense_hat

## Additional notes
The Bridge class is a subclass of the phue library's Bridge class and extends its functionality to include additional methods for controlling the lights.
The script uses the Sense Hat joystick to interact with the lights.
The script uses the rgb_to_xy function to convert RGB colors to the xy colorspace used by the Philips Hue Bridge.
The script uses the handle_event function to handle the joystick events and call the appropriate function to control the lights.
The script uses the display_light_number, increase_brightness, decrease_brightness and display_light_color functions to interact with the Sense Hat and display the current light number and color.
