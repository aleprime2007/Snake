# Import libraries and modules
import pygame
from pygame.locals import *
import constants
# import time module
import time

# 5.4 import random
import random

# 4.6 Creating a Hamburger class
class Hamburger():
    def __init__(self, parent_window):
        self.image = pygame.image.load("images/apple.png")
        self.parent_window = parent_window
        self.x = 120
        self.y = 120
        
    def draw(self):
        self.parent_window.blit(self.image, (self.x, self.y))
        pygame.display.flip()
        
    # 5.5 move method
    def move(self):
        self.x = random.randint(1,12)*64
        self.y = random.randint(1,9)*64
        
class Snake():
    # 4.1 Adding length parameter
    def __init__(self, window, length):
        self.length = length
        self.parent_window = window
        # Load the snake body image
        self.snake_body = pygame.image.load("images/snake_body.png")
        # 4.2 Initial position
        self.x = [constants.SNAKE_BODY_SIZE]*length
        self.y = [constants.SNAKE_BODY_SIZE]*length
        # Initial movement direction of the snake
        self.direction = "down"
        
    # 5.6 Increase lenght
    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)
        
    def move_left(self):
        # setting direction of the snake
        self.direction = "left"
        
    def move_right(self):
        # setting direction of the snake
        self.direction = "right"
        
    def move_up(self):
        # setting direction of the snake
        self.direction = "up"
        
    def move_down(self):
        # setting direction of the snake
        self.direction = "down"
        
    def walk(self):
        # 4.5 check snakes' direction and move it
        for i in range(self.length-1,0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
            
        if self.direction == 'left':
            self.x[0] -= constants.SNAKE_BODY_SIZE
        if self.direction == 'right':
            self.x[0] += constants.SNAKE_BODY_SIZE
        if self.direction == 'up':
            self.y[0] -= constants.SNAKE_BODY_SIZE
        if self.direction == 'down':
            self.y[0] += constants.SNAKE_BODY_SIZE
        
        # draw snake for each chance of direction
        self.draw()
        
        
    def draw(self):
        self.parent_window.fill(constants.BG_COLOR)
        # 4.4 Draw the snake body in diferets coordinates
        for i in range(self.length):
            self.parent_window.blit(self.snake_body, (self.x[i], self.y[i]))
        pygame.display.flip()
    
 
class Game():
    
    def __init__(self):
        # Initialize pygame
        pygame.init()
        # Displaying a window
        self.window = pygame.display.set_mode(constants.SIZE)
        # Setting a window title
        self.title = pygame.display.set_caption(constants.TITTLE)
        # Setting a window icon
        self.icon = pygame.image.load("images/icon.png")
        pygame.display.set_icon(self.icon)
        # Setting a background color
        self.window.fill(constants.BG_COLOR)
        
        # Creating a snake object
        self.snake = Snake(self.window, 8)
        self.snake.draw()
        
        # 4.7 Draw the apple
        self.hamburger = Hamburger(self.window)
        self.hamburger.draw()
        
        #pygame.display.update()
        
    def reset(self):
        self.snake = Snake(self.window, 7)
        self.hamburger = Hamburger(self.window)
        
    # 5.1 Collition
    def if_collition(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + 32:
            if y1 >= y2 and y1 < y2 + 32:
                return True
        return False
    
    # 5.2 Play function
    def play(self):
        self.snake.walk()
        self.hamburger.draw()
        # 5.9 Show score
        self.display_score()
        pygame.display.flip()
        
        if self.if_collition(self.snake.x[0], self.snake.y[0], self.hamburger.x, self.hamburger.y):
            #print("Collition ocurred")
            # 5.7 Call increase length
            self.snake.increase_length()
            # 5.3 move
            self.hamburger.move()
            
        # 6.1 Snake colliding with itself
        for i in range(3, self.snake.length):
            if self.if_collition(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                #print("Game Over")
                #exit(0)
                raise "Game Over"
                #self.show_game_over()
            
    # 6.2 Show game over function
    def show_game_over(self):
        self.window.fill(constants.BG_COLOR)
        font = pygame.font.SysFont("arial", 30)
        message1 = font.render(f"Game Over! Your score is {self.snake.length}", True, (0, 0, 0))
        self.window.blit(message1, (200, 300))
        message2 = font.render("To play again press Enter. To exit press Escape!", True, (0, 0, 0))
        self.window.blit(message2, (100, 350))
        pygame.display.flip()
        
            
    
    # 5.8 Show score
    def display_score(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score: {self.snake.length - 7}",True,(200,200,200))
        self.window.blit(score,(100,10))
            
        
        
        
        
        
    def run(self):
        # Creating a bool value which checks
        # if game is running
        running = True
        
        # 6.3 pause variable
        pause = False
        
        # Keep game running till running is true
        while running:
            
            # Check for event if user has pushed
            # any event in queue
            for event in pygame.event.get():
                
                # If event is of type keydown or quit then 
                # set running bool to false
                if event.type == KEYDOWN:
                    
                    if event.key == K_ESCAPE:
                        running = False
                        
                    # 6.5 Replay the game
                    if event.key == K_RETURN:
                        pause = False
                        
                    # 6.6 Update keystrokes
                    if not pause: 
                    
                        # Movement to left
                        if event.key == K_LEFT:
                            self.snake.move_left()
                        
                        # Movement to right
                        if event.key == K_RIGHT:
                            self.snake.move_right()
                        
                        # Movement to up 
                        if event.key == K_UP:
                            self.snake.move_up()
                        
                        # Movement to down
                        if event.key == K_DOWN:
                            self.snake.move_down()  
                    
                        
                elif event.type == QUIT:
                    running = False
            
            # 6.4 mechanims pause
            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                
                # 6.7 call reset method
                self.reset()
                
            # Call the sleep module
            time.sleep(0.3)

# Creating a game object  
game = Game()
game.run()