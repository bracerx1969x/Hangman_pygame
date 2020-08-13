# Pygame Youtube tutorial for Hangman game
# only minor changes from exactly following tutorial

import math
import pygame
import pygame.ftfont
from random import choice


# setup display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hangman Game! - Pygame')

# button variables
RADIUS = 20
GAP = 15
VISIBILITY = 3
VISIBLE = True
HIDDEN = False
letters = []
start_x = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
start_y = 400
A = 65
for i in range(26):
    x = start_x + GAP * 2 + (RADIUS * 2 + GAP) * (i % 13)
    y = start_y + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), VISIBLE])

# fonts
BASE_FONT_NAME = 'verdana'
LETTER_FONT = pygame.ftfont.SysFont(BASE_FONT_NAME, 28)
WORD_FONT = pygame.ftfont.SysFont(BASE_FONT_NAME, 40)
TITLE_FONT = pygame.ftfont.SysFont(BASE_FONT_NAME, 60)

# load images
images = []
for i in range(7):
    image = pygame.image.load('images/hangman' + str(i) + '.png')
    images.append(image)

# game variables
hangman_status = 0
WORD_CHOICES = ['PYTHON', 'JAVA', 'KOTLIN', 'JAVASCRIPT', 'DEVELOPER']
word = choice(WORD_CHOICES)
guessed = []

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True


def draw():
    win.fill(WHITE)

    # draw title
    text = TITLE_FONT.render('PYGAME HANGMAN', 1, BLACK)
    win.blit(text, (int(WIDTH / 2 - text.get_width() / 2), 10))

    # draw word
    display_word = ''
    for letter in word:
        if letter in guessed:
            display_word += letter + ' '
        else:
            display_word += '_ '
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (int(x - text.get_width() / 2), int(y - text.get_height() / 2)))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()
    pygame.time.delay(250)


def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)


while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                    if dis < RADIUS:
                        letter[VISIBILITY] = HIDDEN
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1

    draw()

    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break

    if won:
        display_message('You Won!')
        break

    if hangman_status == 6:
        display_message('You Lost!')
        break

pygame.quit()
