import pygame
from helpers.controller_mapping import ControllerMapping

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Untitled 2.8.2025")
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

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
p1_pos=[]
p2_pos=[]

running = True
while running:

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    # Clear screen
    screen.fill((0, 0, 0))
   # screen.blit(, (0, 0))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get inputs
    keys = pygame.key.get_pressed()

    red_direction = red_controls.get_direction(keys)
    red_actions = red_controls.get_actions(keys)
    blue_direction = blue_controls.get_direction(keys)
    blue_actions = blue_controls.get_actions(keys)

    # Check for quit action
    if "quit" in red_actions or "quit" in blue_actions:
        running = False

    # Update positions
    # red_pos[0] += int(red_direction[0] * 5)
    # red_pos[1] += int(red_direction[1] * 5)
    # blue_pos[0] += int(blue_direction[0] * 5)
    # blue_pos[1] += int(blue_direction[1] * 5)

    

    

    # Blue ninja actions
    if "a" in blue_actions:
        blue_pos[1] -= 20  # ninja jumps up
    if "b" in blue_actions:
        for angle in range(0, 361, 15):  # Rotate in increments for smooth animation
            screen.blit(beach_background, (0, 0))
            screen.blit(keyboard_mapping, keyboard_mapping_pos)
            screen.blit(red_ninja, red_pos)
            screen.blit(ninja_ship, ship_pos)
            rotated_blue_ninja = pygame.transform.rotate(blue_ninja, angle)
            rect = rotated_blue_ninja.get_rect(center=(blue_pos[0] + 50, blue_pos[1] + 50))
            screen.blit(rotated_blue_ninja, rect.topleft)
            pygame.display.flip()
            clock.tick(30)
    # Red ninja actions
    if "a" in red_actions:
        red_pos[1] -= 20  # ninja jumps up

    if "b" in red_actions:
        for angle in range(0, 361, 15):  # Rotate in increments for smooth animation
            screen.blit(beach_background, (0, 0))
            screen.blit(keyboard_mapping, keyboard_mapping_pos)
            screen.blit(blue_ninja, blue_pos)
            screen.blit(ninja_ship, ship_pos)
            rotated_red_ninja = pygame.transform.rotate(red_ninja, angle)
            rect = rotated_red_ninja.get_rect(center=(red_pos[0] + 60, red_pos[1] + 45))
            screen.blit(rotated_red_ninja, rect.topleft)
            pygame.display.flip()
            clock.tick(30)

    pygame.display.flip()
    clock.tick(60)


# End Your Game Code Here
pygame.quit()