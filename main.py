import math
import pygame
import pygame.ftfont


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
LETTER_FONT = pygame.ftfont.SysFont('comicsans', 40)
WORD_FONT = pygame.ftfont.SysFont('comicsans', 60)

# load images
images = []
for i in range(7):
    image = pygame.image.load('images/hangman' + str(i) + '.png')
    images.append(image)

# game variables
hangman_status = 0
word = 'DEVELOPER'
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
            win.blit(text, (int(x - text.get_width() / 2 + 1), int(y - text.get_height() / 2) + 3))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


while run:
    clock.tick(FPS)

    draw()

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

    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break

    if won:
        print('won')
        break

    if hangman_status == 6:
        print('lost')
        break

pygame.quit()
