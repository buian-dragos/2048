import pygame

class Gui:
    def __init__(self,serv):
        self._serv = serv

        self._serv.randomGenerator()

        self._FPS = 60
        # TODO Add constants to different file
        self._WIDTH = 800
        self._HEIGHT = 800
        self._SQUARE_SIZE = 200
        self._white = (255, 255, 255)
        self._black = (0, 0, 0)

        pygame.init()
        pygame.font.init()

        self._WIN = pygame.display.set_mode((self._WIDTH,self._HEIGHT))
        pygame.display.set_caption('2048')

    # TODO Add colors depending on the value
    # Dict of colors in the constants file
    def draw_board(self):
        board = self._serv.getBoard()
        font = pygame.font.Font(None, 36)  # You can change the font and size as needed
        for row in range(4):
            for col in range(4):
                pygame.draw.rect(self._WIN, self._white, (col * 200, row * 200, 200, 200))
                pygame.draw.rect(self._WIN, self._black, (col * 200, row * 200, 200, 200), 8)

                numb = board[row][col]

                if numb is None:
                    numb = ""

                numb = str(numb)

                # Create a text surface with the desired text
                text = font.render(numb, True, self._black)  # Change "Text" to your desired text

                # Calculate the position to center the text inside the rectangle
                text_rect = text.get_rect()
                text_rect.center = (col * 200 + 100, row * 200 + 100)  # Centers text in 200x200 rectangle

                # Blit (draw) the text surface onto the window
                self._WIN.blit(text, text_rect)


    def run(self):
        run = True
        clock = pygame.time.Clock()

        while run:
            clock.tick(self._FPS)

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
                    if event.key == pygame.K_u:
                        self._serv.undo()


            self.draw_board()
            pygame.display.update()

        pygame.quit()
