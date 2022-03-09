#Red & Blue Square Game
#created by Piotr Ochal
#based on https://www.javatpoint.com/pygame
#and https://github.com/techwithtim/OpenCV-Tutorials/blob/main/tutorial8.py

#liblaries 
import sys
import os
import pygame
import time 
import random 
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

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
h=1
w=1
#random red square position
px=random.uniform(300, x_max-size-300)
py=random.uniform(300, y_max-size-300)
#set square speed
sleeptime=0.01
#round and square number
r=0
square=0
#colors
red=(255,0,0)
black=(0,0,0) 
blue= (0, 128, 255)
#text 
font = pygame.font.SysFont(None, 24)
img = font.render('follow red square, use your face, to reset press "R", to quit press "Q",', True, (255,255,255))
s1_img= font.render('to start press "SPACE"', True, (255,255,255))
font = pygame.font.SysFont(None, 36) 

p_img=font.render('Pjoter Wideło Gejms', True, (240,230,140))
screen.blit(p_img, (100, 2*y_max/4))
pygame.display.flip()
time.sleep(2)
dynamic=0
s2_img=  font.render('Red & Blue Square Game - Face Version', True, (255,255,255))
font = pygame.font.SysFont(None, 24)

p=int(random.uniform(1, 4))
#dynamic square
def wsquare(sized,d):
	if d==0:s=-1
	else:s=int(random.uniform(1, 4))
	if s ==1:
		sx=random.uniform(size+100, x_max-size-100)
		sy=-size
	elif s ==2:
		sx=random.uniform(size+100, x_max-size-100)
		sy=-y_max	
	elif s ==3:
		sy=random.uniform(size+100, y_max-size-100)
		sx=-size
	elif s ==4:
		sy=random.uniform(size+100, y_max-size)
		sx=-x_max
	else:
		sy=random.uniform(100, y_max-size-100)
		sx=random.uniform(100, x_max-size-100)
	return s, sx, sy
#change position square	
def wsp(w,wx,wy,k):
	if w ==1:
		wy+=k
	elif w ==2:
		wy-=k	
	elif w ==3:
		wx+=k
	elif w ==4:
		wx-=k
	return wx, wy


dtxt=['static','dynamic']

while not start:#start wndow
	pygame.draw.rect(screen, black, pygame.Rect(0, 0, x_max, y_max))#clear window
	#write text
	
	s1_img= font.render('to start press "SPACE", game mode: '+dtxt[dynamic], True, (255,255,255))
	screen.blit(img, (100, 2*y_max/4))
	screen.blit(s1_img, (100, 3*y_max/4))
	screen.blit(s2_img, (100, y_max/4))
	
	pressed = pygame.key.get_pressed() 
	for event in pygame.event.get():  
		if event.type == pygame.QUIT or (pressed[pygame.K_q]): #quit window 
			done = True
			start= True
	#change mode static/dynamic		
	if ((pressed[pygame.K_UP] or pressed[pygame.K_w]) ): dynamic=1 
	if ((pressed[pygame.K_DOWN] or pressed[pygame.K_s])): dynamic = 0
	  
	if  pressed[pygame.K_SPACE]:#start game
		ret, frame = cap.read()
		
		start= True
		p,px,py=wsquare(size,dynamic)
		#width and height of camera
		frame=np.fliplr(frame)
		cv2.imwrite('tlo.jpg', frame)
		tlo1 = pygame.image.load(r'tlo.jpg') 
		x_max=tlo1.get_width()
		y_max=tlo1.get_height()
		t0 = time.time()#start time
		screen = pygame.display.set_mode((x_max, y_max)) 
	pygame.display.flip()

while not done:  #game
	pressed = pygame.key.get_pressed()
	for event in pygame.event.get():  
		if event.type == pygame.QUIT or (pressed[pygame.K_q]):   #quit window 
			done = True  
		 
      	
	#face detection and blue box position
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x, y, w, h) in faces:
		roi_gray = gray[y:y+w, x:x+w]
		roi_color = frame[y:y+h, x:x+w]	
	#save imge with use cv2 and read with pygame	
	frame=np.fliplr(frame)
	cv2.imwrite('tlo.jpg', frame)
	tlo1 = pygame.image.load(r'tlo.jpg')   
	#screen is camera image
	screen.blit(tlo1, (0, 0)) 
	 
	
	if (pressed[pygame.K_r]):#reset game
		size=min(x_max/4,y_max/4)
		sleeptime=0.01
		r=0
		square=0
		start=False
		while not start:#start wndow
			pygame.draw.rect(screen, black, pygame.Rect(0, 0, x_max, y_max))#clear window
	#write text
	
			s1_img= font.render('to start press "SPACE", game mode: '+dtxt[dynamic], True, (255,255,255))
			screen.blit(img, (100, 2*y_max/4))
			screen.blit(s1_img, (100, 3*y_max/4))
			screen.blit(s2_img, (100, y_max/4))
	
			pressed = pygame.key.get_pressed() 
			for event in pygame.event.get():  
				if event.type == pygame.QUIT or (pressed[pygame.K_q]): #quit window 
					done = True
					start= True
			#changing gamemode
			if ((pressed[pygame.K_UP] or pressed[pygame.K_w]) ): dynamic=1 
			if ((pressed[pygame.K_DOWN] or pressed[pygame.K_s])): dynamic = 0  
			if  pressed[pygame.K_SPACE]:#start game
	
				start= True
				p,px,py=wsquare(size,dynamic)
				t0 = time.time()#start time
			pygame.display.flip()
	
	#blue square in central face
	x=x_max-x-h/2-size/2
	y=y+w/2-size/2
	if (x>=px-size and y>=py-size and x<=px+size and y<=py+size):#if blue is on red square
		square +=1
		size=size-10# reduce squares 
		if size<10 or (size<2*r and dynamic==1): #if squares are samall 
			r += 1# next round
			size=min(x_max/4,y_max/4)# start size
			sleeptime=sleeptime/2#but faster
		p,px,py=wsquare(size,dynamic)
	elif(px<-size or py<-size or px>x_max or py>y_max):
		p,px,py=wsquare(size,dynamic)
	else: px,py=wsp(p,px,py,r+1)
	
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
#remove image and free camera xd
os.remove("tlo.jpg")
cap.release()
cv2.destroyAllWindows()
	
