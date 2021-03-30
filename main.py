import pygame
pygame.init()
import random

width, height = 720, 720
screen = pygame.display.set_mode((width, height))
running = True

#colours
red = (255, 0, 0)
green = (0, 170, 0)
blue = (0, 0, 255)
orange = (200, 145, 0)
magenta = (255, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
grey = (140, 140, 140)
cyan = (0, 255, 255)
lime = (0, 255, 128)
yellow = (255, 255, 0)

#playground
pWidth = 20
rex = []

#pac man
x, y = 100, 100
direction = "Right"
temp = "Right"
speed = 10
score = 0

#power up
pX, pY = random.randint(40, width-40), random.randint(40, height-40)

#ghost
ghostPos = [(50, 600), (600, 600), (600, 100), (350, 350)]
p = random.randint(0, 3)
ghostX1, ghostY1 = ghostPos[p][0], ghostPos[p][1]
ghostPos.remove(ghostPos[p])
p = random.randint(0, 2)
ghostX2, ghostY2 = ghostPos[p][0], ghostPos[p][1]
directions = ["Right", "Left", "Up", "Down"]
ghostDir1 = directions[random.randint(0, 3)]
temp1 = ghostDir1

ghostDir2 = directions[random.randint(0, 3)]
temp2 = ghostDir2
j = 0

game_over = False

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP or event.key == pygame.K_w:
				direction = "Up"
			elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
				direction = "Down"
			elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
				direction = "Right"
			elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
				direction = "Left"

	#playground
	#border
	pygame.draw.rect(screen, blue, (10, 10, width-20, height-20))
	pygame.draw.rect(screen, black, (20, 20, width-40, height-40))
	
	#score label
	font = pygame.font.Font('freesansbold.ttf', 20)
	text = font.render(f"Score: {score}", True, (255, 255, 255), (0, 0, 0))
	textRect = text.get_rect()
	textRect.center = (50, 10)
	screen.blit(text, textRect)
	
	#4 pillars connected to border
	rex.append(pygame.draw.rect(screen, blue, (width*0.25, 20, pWidth, height*0.2)))
	rex.append(pygame.draw.rect(screen, blue, (width*0.75-pWidth, 20, pWidth, height*0.2)))
	rex.append(pygame.draw.rect(screen, blue, (width*0.25, (height-20)-(height*0.2), pWidth, height*0.2)))
	rex.append(pygame.draw.rect(screen, blue, (width*0.75-pWidth, (height-20)-(height*0.2), pWidth, height*0.2)))
	
	#2 pillars between the above 4
	rex.append(pygame.draw.rect(screen, blue, (20, height*0.5, height*0.1, pWidth)))
	rex.append(pygame.draw.rect(screen, blue, (height-(height*0.1)-20, height*0.5, height*0.1, pWidth)))
	
	#center
	rex.append(pygame.draw.rect(screen, blue, (height*0.35, height*0.6, height*0.3, pWidth)))	
	rex.append(pygame.draw.rect(screen, blue, (height*0.35, height*0.6-(height*0.2), pWidth, height*0.2)))
	rex.append(pygame.draw.rect(screen, blue, (height*0.65-pWidth, height*0.6-(height*0.2), pWidth, height*0.2)))
	rex.append(pygame.draw.rect(screen, blue, (height*0.35+pWidth-1, height*0.6-(height*0.2), height*0.03, pWidth)))
	rex.append(pygame.draw.rect(screen, blue, (height*0.65-pWidth-(height*0.03), height*0.6-(height*0.2), height*0.05, pWidth)))
	
	#pac man
	pac = pygame.draw.rect(screen, black, (x-40, y-40, 80, 80))
	pygame.draw.circle(screen, yellow, (x, y), 40)
	if direction == "Right":
		pygame.draw.polygon(screen, black, [(x, y), (x+16.3, y+36.5), (x+16.3, y-36.5)])
		mouth = pygame.draw.rect(screen, black, (x+16.3, y-36.5, 24, 73))
	if direction == "Left":
		pygame.draw.polygon(screen, black, [(x, y), (x-16.3, y+36.5), (x-16.3, y-36.5)])
		mouth = pygame.draw.rect(screen, black, (x-16.3-24, y-36.5, 24, 73))
		
	if direction == "Up":
		pygame.draw.polygon(screen, black, [(x, y), (x+36.5, y-16.3), (x-36.5, y-16.3)])
		mouth = pygame.draw.rect(screen, black, (x-36.5, y-40, 73, 24))
	if direction == "Down":
		pygame.draw.polygon(screen, black, [(x, y), (x+36.5, y+16.3), (x-36.5, y+16.3)])
		mouth = pygame.draw.rect(screen, black, (x-36.5, y+16.3, 73, 24))
		
	#player movement
	flag = True
	for i in rex:
		if temp == direction:
			if i.colliderect(mouth) or x-40 <= 20 or y-40 <= 20 or x+40 >= width-20 or y+40 >= height-20:
				flag = False

	if flag == True:
		if direction == "Right":
			x += speed
		elif direction == "Left":
			x -= speed
		elif direction == "Up":
			y -= speed
		elif direction == "Down":
			y += speed
		temp = direction

	#power up
	powerUp = pygame.draw.rect(screen, black, (pX-20, pY-20, 40, 40))
	pygame.draw.circle(screen, red, (pX, pY), 20)
	for i in rex:
		if powerUp.colliderect(i):
			pX, pY = random.randint(40, width-40), random.randint(40, height-40)
	
	if powerUp.colliderect(mouth):
		pX, pY = random.randint(40, width-40), random.randint(40, height-40)
		score += 1
		
	#ghosts
	ghost1 = pygame.draw.rect(screen, black, (ghostX1, ghostY1-25, 50, 95))
	pygame.draw.rect(screen, cyan, (ghostX1, ghostY1, 50, 70))
	pygame.draw.circle(screen, cyan, (ghostX1+25, ghostY1), 25)
	pygame.draw.circle(screen, white, (ghostX1+10, ghostY1), 7)
	pygame.draw.circle(screen, white, (ghostX1+36, ghostY1), 7)
	pygame.draw.circle(screen, black, (ghostX1+10, ghostY1), 4)
	pygame.draw.circle(screen, black, (ghostX1+36, ghostY1), 4)
	
	ghost2 = pygame.draw.rect(screen, black, (ghostX2, ghostY2-25, 50, 95))
	pygame.draw.rect(screen, lime, (ghostX2, ghostY2, 50, 70))
	pygame.draw.circle(screen, lime, (ghostX2+25, ghostY2), 25)
	pygame.draw.circle(screen, white, (ghostX2+10, ghostY2), 7)
	pygame.draw.circle(screen, white, (ghostX2+36, ghostY2), 7)
	pygame.draw.circle(screen, black, (ghostX2+10, ghostY2), 4)
	pygame.draw.circle(screen, black, (ghostX2+36, ghostY2), 4)
	
	#ghost movement
	flag = True
	for i in rex:
		if temp1 == ghostDir1:
			if i.colliderect(ghost1):
				flag = False

	if ghostX1+50 >= width - 20:
		ghostX1 = 30
	elif ghostX1 <= 30:
		ghostX1 = width-100
		
	if ghostY1+70 >= height - 20:
		ghostY1 = 30
	elif ghostY1 <= 30:
		ghostY1 = height -100

	if flag == True:
		if ghostDir1 == "Right":
			ghostX1 += speed
		elif ghostDir1 == "Left":
			ghostX1 -= speed
		elif ghostDir1 == "Up":
			ghostY1 -= speed
		elif ghostDir1 == "Down":
			ghostY1 += speed
		temp1 = ghostDir1
	else:
		ghostDir1 = directions[random.randint(0, 3)]
		
	flag = True
	for i in rex:
		if temp2 == ghostDir2:
			if i.colliderect(ghost2):
				flag = False

	if ghostX2+50 >= width - 20:
		ghostX2 = 30
	elif ghostX2 <= 30:
		ghostX2 = width-100
		
	if ghostY2+70 >= height - 20:
		ghostY2 = 30
	elif ghostY2 <= 30:
		ghostY2 = height -100
		
	if flag == True:
		if ghostDir2 == "Right":
			ghostX2 += speed
		elif ghostDir2 == "Left":
			ghostX2 -= speed
		elif ghostDir2 == "Up":
			ghostY2 -= speed
		elif ghostDir2 == "Down":
			ghostY2 += speed
		temp2 = ghostDir2
	else:
		ghostDir2 = directions[random.randint(0, 3)]
	
	if j % 10 == 0:
		ghostDir1 = directions[random.randint(0, 3)]
		ghostDir2 = directions[random.randint(0, 3)]
		
	j += 1
	
	#game over
	if pac.colliderect(ghost1) or pac.colliderect(ghost2):
		game_over = True
	
	if game_over == True:
		while running:
			screen.fill(black)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False

			font = pygame.font.Font('freesansbold.ttf', 40)
			text = font.render("Game Over!", True, red, black)
			textRect = text.get_rect()
			textRect.center = (width/2, height/2)
			screen.blit(text, textRect)
			
			text = font.render(f"Score: {score}", True, red, black)
			textRect = text.get_rect()
			textRect.center = (width/2, (height/2)+40)
			screen.blit(text, textRect)
			
			pygame.display.flip()
	
	pygame.display.flip()

pygame.quit()
