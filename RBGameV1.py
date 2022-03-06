#Red & Blue Square Game version 1
#created by Piotr Ochal
#based on https://www.javatpoint.com/pygame


#liblaries 
import sys
import pygame
import time 
import random 
import numpy as np

pygame.display.set_caption('Red & Blue Square Game')#name of window
#wndow size
x_max=800
y_max=600
#size of squere
size=min(x_max/4,y_max/4)
wsize=1
pygame.init()  
screen = pygame.display.set_mode((x_max, y_max))  
done = False
start= False 
GO=False
#random blue square position
x = random.uniform(size, x_max-size) 
y = random.uniform(size, y_max-size)
#random red square position
px=random.uniform(size+50, x_max-size-50)
py=random.uniform(size+50, y_max-size-50)
i=[y_max+10,y_max+10,y_max+10,y_max+10,y_max+10,y_max+10,y_max+10,y_max+10,-y_max+10,y_max+10]
wx=np.array(i)
wy=np.array(i)
w=np.array(i)
wsize=np.array(i)
#random white square position
def wsquare(size):
	s=int(random.uniform(1, 4))
	if s ==1:
		sx=random.uniform(size, x_max-size)
		sy=-size
	elif s ==2:
		sx=random.uniform(size, x_max-size)
		sy=y_max	
	elif s ==3:
		sy=random.uniform(size, y_max-size)
		sx=-size
	elif s ==4:
		sy=random.uniform(size, y_max-size)
		sx=x_max
	return s, sx, sy, size
#change position white square	
def wsp(w,wx,wy):
	if w ==1:
		wy+=1
	elif w ==2:
		wy-=1	
	elif w ==3:
		wx+=1
	elif w ==4:
		wx-=1
	return wx, wy
	
#set square speed
sleeptime=0.01
sleep=sleeptime
#round and square number
r=0
square=0
#colors
red=(255,0,0)
black=(0,0,0) 
blue= (0, 128, 255)


#text 
font = pygame.font.SysFont(None, 24)
img = font.render('follow red square, use "WASD" or arows, to reset press "R", to quit press "Q",', True, (240,230,140))
s1_img= font.render('to start press "SPACE"', True, (240,230,140))
font = pygame.font.SysFont(None, 36) 
s2_img=  font.render('Red & Blue Square Game', True, (240,230,140))
font = pygame.font.SysFont(None, 24)
s3_img=  font.render("don't touch whie square!", True, (240,230,140))

while not start:#start wndow
	pygame.draw.rect(screen, black, pygame.Rect(0, 0, x_max, y_max))#clear window
	#write text
	screen.blit(img, (100, 2*y_max/4))
	screen.blit(s1_img, (100, 3*y_max/4))
	screen.blit(s2_img, (100, y_max/4))
	screen.blit(s3_img, (100, 2*y_max/4+30))
	pressed = pygame.key.get_pressed() 
	for event in pygame.event.get():  
		if event.type == pygame.QUIT or (pressed[pygame.K_q]): #quit window 
			done = True
			start= True
			
	
	if  pressed[pygame.K_SPACE]:#start game
		 start= True
		 #w, wx, wy=wsquare()
		 t0 = time.time()#start time
	pygame.display.flip()

while not done:  #game
	pressed = pygame.key.get_pressed()
	for event in pygame.event.get():  
		if event.type == pygame.QUIT or (pressed[pygame.K_q]):   #quit window 
			done = True  
		 
      	
	
	pygame.draw.rect(screen, black, pygame.Rect(0, 0, x_max, y_max))#clear window 
	if (pressed[pygame.K_r]):#reset game
		size=min(x_max/4,y_max/4)
		r=0
		square=0
		t0 = time.time()
		wx=np.array(i)
		wy=np.array(i)
		w=np.array(i)
	

	#changing the position of the blue square
	if ((pressed[pygame.K_UP] or pressed[pygame.K_w]) and y>10): y -= 3  
	if ((pressed[pygame.K_DOWN] or pressed[pygame.K_s]) and y<(y_max-size-10)): y += 3  
	if ((pressed[pygame.K_LEFT] or pressed[pygame.K_a]) and x>10): x -= 3  
	if ((pressed[pygame.K_RIGHT] or pressed[pygame.K_d]) and x<(x_max-size-10)): x += 3  
	
	
	 
	if (x>=px-size and y>=py-size and x<=px+size and y<=py+size):#if blue is on red square
		square +=1
		size=size-10# reduce squares 
		if size<10: #if squares are samall 
			r += 1# next round
			size=size=min(x_max/4,y_max/4)# start size
			
			wx=np.array(i)
			wy=np.array(i)
			w=np.array(i)
		if size<20:#random red square position but not all window
			px=random.uniform(50, x_max-x_max/4-50)
			py=random.uniform(50, y_max-y_max/4-50)
		else:#random red square position
			px=random.uniform(50, x_max-size-50)
			py=random.uniform(50, y_max-size-50)
	
	playtime=str(time.time() - t0)#chek time
	pt_max=playtime.find(".")#find "." in playtime sting 
	#text
	screen.blit(img, (0, 0))
	r_img = font.render('round: '+str(r)+", square: "+str(square)+", time in game: "+playtime[:pt_max]+"s", True, (240,230,140))
	screen.blit(r_img, (0, y_max-24))
	#draw red nad blue square
	pygame.draw.rect(screen, red, pygame.Rect(px, py, size, size))
	pygame.draw.rect(screen, blue, pygame.Rect(x, y, size, size))
	#white square
	b=	int(r/10)+1
	if b>10: b=10
	for a in range(0,b):
		if (wx[a]<-wsize[a] or wy[a]<-wsize[a] or wx[a]>x_max or wy[a]>y_max):#if out of skreen create new
			w[a], wx[a], wy[a], wsize[a] = wsquare(min(x_max/4,y_max/4)/b)
		else: #change position
			wx[a], wy[a]=wsp(w[a],wx[a],wy[a])
			
		
		pygame.draw.rect(screen, (255,255,255), pygame.Rect(wx[a], wy[a], wsize[a], wsize[a]))
		#game over
		if(x>=wx[a]-size and y>=wy[a]-size and x<=wx[a]+wsize[a] and y<=wy[a]+wsize[a]):
			pygame.draw.rect(screen, black, pygame.Rect(0, 0, x_max, y_max))#clear window
			wx=np.array(i)
			wy=np.array(i)
			w=np.array(i)
			font = pygame.font.SysFont(None, 36)
			GO_img = font.render("game over", True, (240,230,140))
			font = pygame.font.SysFont(None, 24)
			screen.blit(GO_img, (100, 2*y_max/4))
			re_img=font.render('to restart press "SPACE"', True, (240,230,140))
			screen.blit(re_img, (100, 3*y_max/4))
			pygame.display.flip() 
			GO=True
			while GO:#game over menu xd
				pressed = pygame.key.get_pressed()
				for event in pygame.event.get():  
					if event.type == pygame.QUIT or (pressed[pygame.K_q]): #quit window 
						done = True
						GO=False
				if  pressed[pygame.K_SPACE]: GO = False#start game
				time.sleep(0.002)
			pygame.draw.rect(screen, black, pygame.Rect(0, 0, x_max, y_max))#clear window
			size=min(x_max/4,y_max/4)
			
			r=0
			square=0
			t0 = time.time()	
		
		
	sleep=2*sleeptime/(r%10+1)#time wait to next move
	time.sleep(sleep)#wait to next press
	pygame.display.flip()  
