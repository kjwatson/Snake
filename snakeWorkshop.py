import pygame
import time
import random

pygame.init()


# These variables are tuples representing different colors' RGB values. 
# Look up the RGB values of the colors listed below and fill in their tuples.
white = ()
black = ()
red = ()
green = ()

display_width = 800
display_height = 600
x_start = display_width / 2
y_start = display_height / 2

clock = pygame.time.Clock() # Returns Python clock object
font = pygame.font.SysFont(None, 25) # Returns Python font object

block_size = 10
fps = 15

gameDisplay = pygame.display.set_mode((display_width, display_height))

#Name your game whatever you'd like! 
pygame.display.set_caption("")

apple = pygame.image.load("Apple.png")

pygame.display.update()

def snake(block_size, snakelist):
	for XnY in snakelist:
		pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])


def displayApple(x, y):
	gameDisplay.blit(apple, (x, y))

def text_objects(text, color):
	textSurface = font.render(text, True, color)
	return textSurface, textSurface.get_rect()

def message_to_screen(msg, color):
	textSurf, textRect = text_objects(msg, color)
	textRect.center = (display_width/2), (display_height/2)
	gameDisplay.blit(textSurf, textRect)

def gameLoop():
	gameExit = False
	gameOver = False

	lead_x = x_start
	lead_y = y_start


	snakeList = []
	snakeLength = 1

	lead_x_change = 0
	lead_y_change = 0

	randAppleX = round(random.randrange(0, display_width - block_size)/10.0) * 10.0 
	randAppleY = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0

	while not gameExit:

		while gameOver == True:
			gameDisplay.fill(white)
			#Feel free to edit the game over message if you want:
			message_to_screen("Game over. Now go outside or press C to play again or Q to quit", red)
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameExit = True
						gameOver = False
					elif event.key == pygame.K_c:
						gameLoop()

		#This loop is used to handle the controls of the game
		#Fill in the if/else statements that would allow your snake to move properly
		#Use this link as a reference: http://www.pygame.org/docs/ref/key.html
		#When the block moves, it moves in increments of the block_size
		#Adjust lead_x_change and lead_y_change to fit the proper movement of snake
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			elif event.type == pygame.KEYDOWN:


		# Fill in the logic below so that if your lead snake square is crossing any 
		# borders of the game, the game ends
		if :
			

		lead_x += lead_x_change
		lead_y += lead_y_change

		gameDisplay.fill(white)
		pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, block_size, block_size])

		snakeHead = []
		snakeHead.append(lead_x)
		snakeHead.append(lead_y)
		snakeList.append(snakeHead)

		if len(snakeList) > snakeLength:
			del snakeList[0]

		# Each segment is a tuple of x-y coordinates, 
		#so if they're equal it means they have collided
		for eachSegment in snakeList[:-1]:
			if eachSegment == snakeHead:
				gameOver = True


		snake(block_size, snakeList)
		displayApple(randAppleX, randAppleY)
		pygame.display.update()

		#This is the part of the code that controls when our snake has eaten an apple
		#Fill in the if statement to check if the coordinates of the apple match that of the snake
		if :
			randAppleX = round(random.randrange(0, display_width - block_size)/10.0) * 10.0 
			randAppleY = round(random.randrange(0, display_height - block_size)/10.0) * 10.0
			gameDisplay.blit(apple, (randAppleX, randAppleY))
			pygame.display.update()
			snakeLength+=1


		clock.tick(fps)

gameLoop()
pygame.quit()
quit()
