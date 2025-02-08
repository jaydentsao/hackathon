import pygame
from helpers.controller_mapping import ControllerMapping

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Example Game")
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (100, 100, 100)

# Load images
beach_background = pygame.image.load("images/beach_background.png").convert()
beach_background = pygame.transform.scale(beach_background, screen.get_size())  # Stretch background
viking_ship = pygame.image.load("images/viking_ship.png").convert_alpha()
red_viking = pygame.image.load("images/red_viking.png").convert_alpha()
blue_viking = pygame.image.load("images/blue_viking.png").convert_alpha()
keyboard_mapping = pygame.image.load("images/keyboard_mapping.png").convert_alpha()

# Scale images
viking_ship = pygame.transform.scale(viking_ship, (240, 240))
red_viking = pygame.transform.scale(red_viking, (120, 90))
blue_viking = pygame.transform.scale(blue_viking, (100, 100))
keyboard_mapping = pygame.transform.scale(keyboard_mapping, (475, 210))

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

# Initialize game variables
red_pos = [100, screen.get_height() - red_viking.get_height() - 100]
blue_pos = [screen.get_width() - blue_viking.get_width() - 110, screen.get_height() - blue_viking.get_height() - 100]
# Intentional Bug: Placing this ship statically will lead to a small bug when shifting screen sizes
ship_pos = [610, 480]
keyboard_mapping_pos = (screen.get_width() // 2 - keyboard_mapping.get_width() // 2, 150)
joystick_radius = 30
joke_displayed = False
joke_color = None
bad_jokes = {
    "red": "Why did the red viking cross the sea? To get to the other fjord!",
    "blue": "What did the blue viking say to the ship? You're oar-some!"
}

# Timer variables for holding button action display
action_display_timer_red = 0
action_display_timer_blue = 0
action_display_duration = 1500  # 1.5 seconds in milliseconds
last_red_action = ""
last_blue_action = ""

running = True

while running:
    # Get current time
    current_time = pygame.time.get_ticks()

    # Clear screen
    screen.fill((0, 0, 0))
    screen.blit(beach_background, (0, 0))

    # Draw keyboard mapping image
    screen.blit(keyboard_mapping, keyboard_mapping_pos)

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
    red_pos[0] += int(red_direction[0] * 5)
    red_pos[1] += int(red_direction[1] * 5)
    blue_pos[0] += int(blue_direction[0] * 5)
    blue_pos[1] += int(blue_direction[1] * 5)

    # Dynamic joystick positions
    red_joystick_center = (screen.get_width() * 0.2, screen.get_height() - 100)
    blue_joystick_center = (screen.get_width() * 0.8, screen.get_height() - 100)

    # Draw red joystick (base and direction)
    pygame.draw.circle(screen, GRAY, red_joystick_center, joystick_radius)
    pygame.draw.circle(screen, RED, 
                    (red_joystick_center[0] + int(red_direction[0] * 15), 
                    red_joystick_center[1] + int(red_direction[1] * 15)), 15)

    # Draw blue joystick (base and direction)
    pygame.draw.circle(screen, GRAY, blue_joystick_center, joystick_radius)
    pygame.draw.circle(screen, BLUE, 
                   (blue_joystick_center[0] + int(blue_direction[0] * 15), 
                    blue_joystick_center[1] + int(blue_direction[1] * 15)), 15)

    # Draw vikings and ship
    screen.blit(red_viking, red_pos)
    screen.blit(blue_viking, blue_pos)
    screen.blit(viking_ship, ship_pos)

    # Check for viking and ship overlap to display jokes
    if red_pos[0] < ship_pos[0] + 200 and red_pos[0] + 80 > ship_pos[0] and red_pos[1] < ship_pos[1] + 200 and red_pos[1] + 80 > ship_pos[1]:
        joke_displayed = True
        joke_color = "red"
    elif blue_pos[0] < ship_pos[0] + 200 and blue_pos[0] + 80 > ship_pos[0] and blue_pos[1] < ship_pos[1] + 200 and blue_pos[1] + 80 > ship_pos[1]:
        joke_displayed = True
        joke_color = "blue"
    else:
        joke_displayed = False

    # Display joke below the ship
    if joke_displayed:
        if joke_color == "red":
            joke_text = pygame.font.Font(None, 28).render(bad_jokes["red"], True, (255, 0, 0))
            screen.blit(joke_text, (460, 440))
        elif joke_color == "blue":
            joke_text = pygame.font.Font(None, 28).render(bad_jokes["blue"], True, (0, 0, 255))
            screen.blit(joke_text, (470, 440))

    # Draw static text above the ship
    title_text = pygame.font.Font(None, 36).render("BOARD ME BOAT TO WIN A JOKE!", True, (255, 255, 255))
    # Dynamic title position (centered)
    title_text_pos = (screen.get_width() // 2 - title_text.get_width() // 2, 
                    screen.get_height() // 2 - title_text.get_height() // 2)
    # Blit title text
    screen.blit(title_text, title_text_pos)


    # Display button action
    if red_actions:
        action_display_timer_red = current_time  # Reset the timer when a new action is detected
        last_red_action = ', '.join([action.upper() for action in red_actions])  # Store the action
    elif current_time - action_display_timer_red > action_display_duration:  # Check if 1.5 seconds have passed
        last_red_action = ""  # Clear the action display after 1.5 seconds

    if blue_actions:
        action_display_timer_blue = current_time  # Reset the timer when a new action is detected
        last_blue_action = ', '.join([action.upper() for action in blue_actions])  # Store the action
    elif current_time - action_display_timer_blue > action_display_duration:  # Check if 1.5 seconds have passed
        last_blue_action = ""  # Clear the action display after 1.5 seconds

    # Draw button action info
    debug_red = font.render(f"Red Position: {red_pos}, Button Action: {last_red_action}", True, RED)
    debug_blue = font.render(f"Blue Position: {blue_pos}, Button Action: {last_blue_action}", True, BLUE)
    # Dynamic debug positions at the top
    debug_red_pos = (screen.get_width() * 0.1, 50)  # 10% from the left
    debug_blue_pos = (screen.get_width() * 0.9 - debug_blue.get_width(), 50)  # 10% from the right
    # Blit debug images
    screen.blit(debug_red, debug_red_pos)
    screen.blit(debug_blue, debug_blue_pos)

    # Red viking actions
    if "a" in red_actions:
        red_pos[1] -= 20  # Viking jumps up
    if "b" in red_actions:
        for angle in range(0, 361, 15):  # Rotate in increments for smooth animation
            screen.blit(beach_background, (0, 0))
            screen.blit(keyboard_mapping, keyboard_mapping_pos)
            screen.blit(blue_viking, blue_pos)
            screen.blit(viking_ship, ship_pos)
            rotated_red_viking = pygame.transform.rotate(red_viking, angle)
            rect = rotated_red_viking.get_rect(center=(red_pos[0] + 60, red_pos[1] + 45))
            screen.blit(rotated_red_viking, rect.topleft)
            pygame.display.flip()
            clock.tick(30)

    # Blue viking actions
    if "a" in blue_actions:
        blue_pos[1] -= 20  # Viking jumps up
    if "b" in blue_actions:
        for angle in range(0, 361, 15):  # Rotate in increments for smooth animation
            screen.blit(beach_background, (0, 0))
            screen.blit(keyboard_mapping, keyboard_mapping_pos)
            screen.blit(red_viking, red_pos)
            screen.blit(viking_ship, ship_pos)
            rotated_blue_viking = pygame.transform.rotate(blue_viking, angle)
            rect = rotated_blue_viking.get_rect(center=(blue_pos[0] + 50, blue_pos[1] + 50))
            screen.blit(rotated_blue_viking, rect.topleft)
            pygame.display.flip()
            clock.tick(30)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
