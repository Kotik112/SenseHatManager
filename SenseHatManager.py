from Bridge import Bridge
from sense_hat import SenseHat

INCREMENTS = 25


class SenseHatManager:
    def __init__(self, bridge):
        self.bridge = bridge
        self.current_light = 1  # initialize current_light to 1
        self.num_lights = len(self.bridge.lights)  # get number of lights
        print("Number of lights = {}".format(self.num_lights))
        self.sense = SenseHat()
        self.sense.clear()  # clear LED matrix
        self.color_list = [
            (255, 0, 0),  # Red
            (0, 255, 0),  # Green
            (0, 0, 255),  # Blue
            (255, 255, 0),  # Yellow
            (255, 0, 255),  # Magenta
            (0, 255, 255)  # Cyan
        ]
        self.current_color = 0

    def handle_event(self, event):
        if event.action == "pressed":
            if event.direction == "left":
                self.current_light = (self.current_light - 1) % 14
                if self.current_light == 0:
                    self.current_light = 14
                print(f"Pressed left. Current light = {self.current_light}")
                self.display_light_number()
            elif event.direction == "right":
                self.current_light = (self.current_light + 1) % 14
                if self.current_light == 0:
                    self.current_light = 14
                print(f"Pressed right. Current light = {self.current_light}")
                self.display_light_number()
            elif event.direction == "up":
                print(f"Pressed up. Current light = {self.current_light}")
                self.increase_brightness()
            elif event.direction == "down":
                print(f"Pressed down. Current light = {self.current_light}")
                self.decrease_brightness()
            elif event.direction == "middle":
                self.current_color = (self.current_color + 1) % len(self.color_list)
                print(f"Pressed middle. Current color = {self.color_list[self.current_color]}")
                self.display_light_color()

    def display_light_number(self):
        self.sense.clear()
        if self.current_light <= 9:
            self.sense.show_letter(str(self.current_light))
        else:
            self.sense.show_message(str(self.current_light))

    def increase_brightness(self):
        brightness = self.bridge.get_brightness(self.current_light)
        # print(brightness)
        if brightness < 256 - INCREMENTS:
            self.bridge.set_brightness(self.current_light, brightness + INCREMENTS)

    def decrease_brightness(self):
        brightness = self.bridge.get_brightness(self.current_light)
        # print(brightness)
        if brightness > INCREMENTS:
            self.bridge.set_brightness(self.current_light, brightness - INCREMENTS)

    def rgb_to_xy(self, red, green, blue):
        """ conversion of RGB colors to CIE1931 XY colors
        Formulas implemented from: https://gist.github.com/popcorn245/30afa0f98eea1c2fd34d
        """

        # gamma correction
        red = pow((red + 0.055) / (1.0 + 0.055), 2.4) if red > 0.04045 else (red / 12.92)
        green = pow((green + 0.055) / (1.0 + 0.055), 2.4) if green > 0.04045 else (green / 12.92)
        blue = pow((blue + 0.055) / (1.0 + 0.055), 2.4) if blue > 0.04045 else (blue / 12.92)

        # convert rgb to xyz
        x = red * 0.649926 + green * 0.103455 + blue * 0.197109
        y = red * 0.234327 + green * 0.743075 + blue * 0.022598
        z = green * 0.053077 + blue * 1.035763

        # convert xyz to xy
        x = x / (x + y + z)
        y = y / (x + y + z)

        return [x, y]

    def display_light_color(self):
        color = self.color_list[self.current_color]
        # Convert RGB values to XY Values accepted by the Bridge
        cie_color = self.rgb_to_xy(color[0], color[1], color[2])
        print(cie_color)
        self.sense.clear(color)
        self.bridge.set_color(self.current_light, cie_color)


def main():
    sense = SenseHat()
    bridge = Bridge()  # initialize Bridge object
    manager = SenseHatManager(bridge)  # initialize SenseHatManager object
    manager.display_light_number()
    while True:
        for event in sense.stick.get_events():
            manager.handle_event(event)  # handle events from joystick


if __name__ == "__main__":
    main()