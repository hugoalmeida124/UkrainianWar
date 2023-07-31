from Configs import *

font = Font.TEXT_FONT
screen = pygame.display.set_mode([Window.WIDTH, Window.HEIGHT])


def draw_text_with_line_breaks(text, font, color, x, y):
    lines = text.split('\n')
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        screen.blit(text_surface, (x, y + i * 30))


text_about_1 = (
    "Welcome to UkrainianWar, the main objective is to defend your side by doing that you can't let Russians go further "
    "in the screen, otherwise\nyou will lose all your lives, if they reach you.\n\n"
    "This game has 5 levels:\n"
    "- Level 1 is from 0-5 kills\n"
    "- Level 2 is from 5-10 kills\n"
    "- Level 3 is from 10-20 kills\n"
    "- Level 4 is from 20-30 kills\n"
    "- Level 5 is from 30-50 kills.\n"
    "\nEach level adds 1 Russian soldier. To keep up, you have to walk and pick bullets from the ground so you can shoot "
    "against the Russian army,\nand also you have to keep an eye on their shots in case you have to dodge some.\n"
    "Remember, you can't shoot while you're crouching.\n"
    "\nYou can:\n"
    "- Walk left (LEFT ARROW)\n"
    "- Walk right (RIGHT ARROW)\n"
    "- Crouch (DOWN ARROW)\n"
    "- Go up (UP ARROW)\n"
    "- Shoot (SPACE)"
)
