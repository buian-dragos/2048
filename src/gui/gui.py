import pygame
from src.domain.constants import FPS, WIDTH, HEIGHT, SQUARE_SIZE
from src.domain.constants import WHITE,BLACK,GRAY, NUMBERS_COLORS

class Gui:
    def __init__(self,serv):
        self._serv = serv

        self._serv.start()

        pygame.init()
        pygame.font.init()

        self._WIN = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('2048')

    def draw_board(self):
        board = self._serv.getBoard()
        font = pygame.font.Font(None, 64)  # You can change the font and size as needed
        for row in range(4):
            for col in range(4):

                numb = board[row][col]

                if numb is None:
                    numb = ""
                    pygame.draw.rect(self._WIN, WHITE, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                else:
                    numb = str(numb)

                    if numb in NUMBERS_COLORS:
                        color = NUMBERS_COLORS[numb]
                    else:
                        color = GRAY
                    pygame.draw.rect(self._WIN, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

                pygame.draw.rect(self._WIN, BLACK, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 8)


                # Create a text surface with the desired text
                text = font.render(numb, True, BLACK)  # Change "Text" to your desired text

                # Calculate the position to center the text inside the rectangle
                text_rect = text.get_rect()
                text_rect.center = (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2)  # Centers text in 200x200 rectangle

                # Blit (draw) the text surface onto the window
                self._WIN.blit(text, text_rect)


    def run(self):
        run = True
        clock = pygame.time.Clock()

        while run:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self._serv.flipFromLeft()
                    if event.key == pygame.K_RIGHT:
                        self._serv.flipFromRight()
                    if event.key == pygame.K_UP:
                        self._serv.flipFromUp()
                    if event.key == pygame.K_DOWN:
                        self._serv.flipFromDown()
                    if event.key == pygame.K_z:
                        self._serv.undo()


            self.draw_board()
            pygame.display.update()

        pygame.quit()
