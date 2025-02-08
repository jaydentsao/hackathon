import pygame

class ControllerMapping:
    def __init__(self, joystick_id=None, keyboard_mappings=None, joystick_button_mappings=None):
        """
        Initialize the ControllerMapping.

        :param joystick_id: The ID of the joystick (optional, None if not using joystick).
        :param keyboard_mappings: Dictionary mapping keys to actions (e.g., {pygame.K_q: "action1"}).
        :param joystick_button_mappings: Dictionary mapping joystick buttons to actions (e.g., {0: "action1"}).
        """
        self.joystick = None
        if joystick_id is not None:
            try:
                self.joystick = pygame.joystick.Joystick(joystick_id)
                self.joystick.init()
            except pygame.error as e:
                print(f"Joystick {joystick_id} could not be initialized: {e}")

        self.keyboard_mappings = keyboard_mappings or {}
        self.joystick_button_mappings = joystick_button_mappings or {}

    def get_direction(self, keys):
        """
        Get directional input from joystick or keyboard.

        :param keys: Currently pressed keys (from pygame.key.get_pressed()).
        :return: Tuple (x, y) where x and y are -1, 0, or 1.
        """
        x, y = 0, 0

        # Keyboard input for directions
        for key, action in self.keyboard_mappings.items():
            if keys[key]:
                if action == "left":
                    x = -1
                elif action == "right":
                    x = 1
                elif action == "up":
                    y = -1
                elif action == "down":
                    y = 1

        # Joystick fallback only if no keyboard input detected
        if x == 0 and y == 0 and self.joystick:
            x = self.joystick.get_axis(0)  # Horizontal axis
            y = self.joystick.get_axis(1)  # Vertical axis

            # Normalize joystick dead zone
            if abs(x) < 0.1: x = 0
            if abs(y) < 0.1: y = 0

        return x, y

    def get_actions(self, keys):
        """
        Get actions from joystick buttons or keyboard keys.

        :param keys: Currently pressed keys (from pygame.key.get_pressed()).
        :return: List of active actions.
        """
        actions = []

        # Joystick button input
        if self.joystick:
            for button, action in self.joystick_button_mappings.items():
                if self.joystick.get_button(button):
                    actions.append(action)

        # Keyboard input (exclude directional keys)
        for key, action in self.keyboard_mappings.items():
            if keys[key] and action not in ["up", "down", "left", "right"]:
                actions.append(action)

        return actions