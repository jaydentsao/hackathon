import pygame
from helpers.controller_mapping import ControllerMapping

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Keyboard Input Controllers for Local Testing
red_controls = ControllerMapping(
    joystick_id=0,
    keyboard_mappings={
        pygame.K_w: "up", pygame.K_s: "down", pygame.K_a: "left", pygame.K_d: "right",
        pygame.K_1: "a", pygame.K_2: "b", pygame.K_3: "x", pygame.K_4: "y",
        pygame.K_q: "start", pygame.K_e: "select", pygame.K_z: "quit"
    },
    joystick_button_mappings={0: "a", 1: "b", 2: "x", 3: "y", 4: "start", 5: "select", 6: "quit"}
)

blue_controls = ControllerMapping(
    joystick_id=1,
    keyboard_mappings={
        pygame.K_UP: "up", pygame.K_DOWN: "down", pygame.K_LEFT: "left", pygame.K_RIGHT: "right",
        pygame.K_i: "a", pygame.K_o: "b", pygame.K_p: "x", pygame.K_LEFTBRACKET: "y",
        pygame.K_k: "start", pygame.K_l: "select", pygame.K_COMMA: "quit"
    },
    joystick_button_mappings={0: "a", 1: "b", 2: "x", 3: "y", 4: "start", 5: "select", 6: "quit"}
)

# Start Your Game Code Here!

a=3

hi



# End Your Game Code Here
pygame.quit()