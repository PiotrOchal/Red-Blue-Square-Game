#Red & Blue Square Game version 0
#created by Piotr Ochal
#based on https://www.javatpoint.com/pygame


#liblaries 
import sys
import pygame
import time 
import random 

pygame.display.set_caption('Red & Blue Square Game')#name of window
#wndow size
x_max=800
y_max=600
#size of squere
size=min(x_max/4,y_max/4)

pygame.init()  
screen = pygame.display.set_mode((x_max, y_max))  
done = False
start= False 
#random blue square position
x = random.uniform(size, x_max-size) 
y = random.uniform(size, y_max-size)
#random red square position
px=random.uniform(size, x_max-size)
py=random.uniform(size, y_max-size)
#set square speed
sleeptime=0.01
#round and square number
r=1
square=0
#colors
red=(255,0,0)
black=(0,0,0) 
blue= (0, 128, 255)

#text 
font = pygame.font.SysFont(None, 24)
img = font.render('follow red square, use "WASD" or arows, to reset press "R", to quit press "Q"', True, (255,255,255))
s1_img= font.render('to start press "SPACE"', True, (255,255,255))
font = pygame.font.SysFont(None, 36) 
s2_img=  font.render('Red & Blue Square Game', True, (255,255,255))
font = pygame.font.SysFont(None, 24)

while not start:#start wndow
	pygame.draw.rect(screen, black, pygame.Rect(0, 0, x_max, y_max))#clear window
	#write text
	screen.blit(img, (100, 2*y_max/4))
	screen.blit(s1_img, (100, 3*y_max/4))
	screen.blit(s2_img, (100, y_max/4))
	
	pressed = pygame.key.get_pressed() 
	for event in pygame.event.get():  
		if event.type == pygame.QUIT or (pressed[pygame.K_q]): #quit window 
			done = True
			start= True
			
	
	if  pressed[pygame.K_SPACE]:#start game
		 start= True
		 t0 = time.time()#start time
	pygame.display.flip()

while not done:  #game
	pressed = pygame.key.get_pressed()
	for event in pygame.event.get():  
		if event.type == pygame.QUIT or (pressed[pygame.K_q]):   #quit window 
			done = True  
		 
      	
	
	 
	if (pressed[pygame.K_r]):#reset game
		size=min(x_max/4,y_max/4)
		sleeptime=0.01
		r=1
		square=0
		t0 = time.time()
	#changing the position of the blue square
	if ((pressed[pygame.K_UP] or pressed[pygame.K_w]) and y>10): y -= 3  
	if ((pressed[pygame.K_DOWN] or pressed[pygame.K_s]) and y<(y_max-size-10)): y += 3  
	if ((pressed[pygame.K_LEFT] or pressed[pygame.K_a]) and x>10): x -= 3  
	if ((pressed[pygame.K_RIGHT] or pressed[pygame.K_d]) and x<(x_max-size-10)): x += 3  
	
	pygame.draw.rect(screen, black, pygame.Rect(0, 0, x_max, y_max))#clear window
	 
	if (x>=px-size and y>=py-size and x<=px+size and y<=py+size):#if blue is on red square
		square +=1
		size=size-10# reduce squares 
		if size<10: #if squares are samall 
			r += 1# next round
			size=size=min(x_max/4,y_max/4)# start size
			sleeptime=sleeptime/2#but faster
		if size<20:#random red square position but not all window
			px=random.uniform(10, x_max-x_max/4-10)
			py=random.uniform(10, y_max-y_max/4-10)
		else:#random red square position
			px=random.uniform(10, x_max-size-10)
			py=random.uniform(10, y_max-size-10)
	
	playtime=str(time.time() - t0)#chek time
	pt_max=playtime.find(".")#find "." in playtime sting 
	#text
	screen.blit(img, (0, 0))
	r_img = font.render('round: '+str(r)+", square: "+str(square)+", time in game: "+playtime[:pt_max]+"s", True, (255,255,255))
	screen.blit(r_img, (0, y_max-24))
	#draw red nad blue square
	pygame.draw.rect(screen, red, pygame.Rect(px, py, size, size))
	pygame.draw.rect(screen, blue, pygame.Rect(x, y, size, size))
	
	time.sleep(sleeptime)#wait to next press
      
	pygame.display.flip()  
	
