
#Red & Blue Square Game
#created by Piotr Ochal
#based on https://www.javatpoint.com/pygame


#liblaries 
import sys, os
import pygame
import time 
import random 
import numpy as np

pygame.display.set_caption('Red & Blue Square Game')#name of window
#wndow size
x_max=800
y_max=600
#size of squere
size=min(x_max/8,y_max/8)

pygame.init()  
screen = pygame.display.set_mode((x_max, y_max))  
done = False
start= False 
GO=False
easy=1
def easytxt(easy):
	if easy==0:return "easy"
	elif easy==1:return "medium"
	elif easy==2:return "hard"
#random blue square position
x = random.uniform(size+100, x_max-size-100) 
y = random.uniform(size+100, y_max-size-100)
#random red square position
px=random.uniform(size+50, x_max-size-50)
py=random.uniform(size+50, y_max-size-50)
i=[2*y_max+10,2*y_max+10,2*y_max+10,2*y_max+10,2*y_max+10,2*y_max+10,2*y_max+10,2*y_max+10,-2*y_max+10,2*y_max+10]
j=[1,1,1,1,1,1,1,1,1,1,1,1,1]
wx=np.array(i)
wy=np.array(i)
w=np.array(i)
wsize=np.array(j)
wspeed=np.array(j)
#random white square position
def wsquare(size):
	s=int(random.uniform(1, 4.99999))
	speed=int(random.uniform(1, 3.99999))
	if s ==1:
		sx=random.uniform(size, x_max-size)
		sy=1-size
	elif s ==2:
		sx=random.uniform(size, x_max-size)
		sy=y_max-1+size	
	elif s ==3:
		sy=random.uniform(size, y_max-size)
		sx=1-size
	elif s ==4:
		sy=random.uniform(size, y_max-size)
		sx=x_max-1+size
	return s, sx, sy, size, speed
#change position white square	
def wsp(w,wx,wy,speed):
	#a=int(random.uniform(0,4))
	if w ==1:
		wy+=speed
	elif w ==2:
		wy-=speed
	elif w ==3:
		wx+=speed
	elif w ==4:
		wx-=speed
	return wx, wy
	
#set square speed
sleeptime=0.01
sleep=sleeptime
#round and square number
r=0
rmax=0
square=0
#colors
red=(255,0,0)
black=(0,0,0) 
blue= (0, 128, 255)
lives=3
pause=False
#text 
font = pygame.font.SysFont(None, 24)
img = font.render('follow red circle, use "WASD" or arows, to reset press "R", to quit press "Q",', True, (240,230,140))

font = pygame.font.SysFont(None, 36) 
s2_img=  font.render('Red & Blue Circles Game', True, (240,230,140))
p_img=font.render('Pjoter Wideło Gejms', True, (240,230,140))
screen.blit(p_img, (100, 2*y_max/4))
pygame.display.flip()
time.sleep(2)
tp=0
font = pygame.font.SysFont(None, 24)
s3_img=  font.render("don't touch whie circle!", True, (240,230,140))


while not start:#start wndow
	pygame.draw.rect(screen, black, pygame.Rect(0, 0, x_max, y_max))#clear window
	#write text
	s1_img= font.render('to start press "SPACE", difficulty: '+easytxt(easy), True, (240,230,140))
	screen.blit(img, (100, 2*y_max/4))
	screen.blit(s1_img, (100, 3*y_max/4))
	screen.blit(s2_img, (100, y_max/4))
	screen.blit(s3_img, (100, 2*y_max/4+30))
	pressed = pygame.key.get_pressed() 
	for event in pygame.event.get():  
		if event.type == pygame.QUIT or (pressed[pygame.K_q]): #quit window 
			done = True
			start= True
	time.sleep(10*sleeptime)		
	if ((pressed[pygame.K_UP] or pressed[pygame.K_w]) and easy<2): easy += 1  
	if ((pressed[pygame.K_DOWN] or pressed[pygame.K_s]) and easy>0): easy -= 1  
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
		
		wx=np.array(i)
		wy=np.array(i)
		w=np.array(i)
		font = pygame.font.SysFont(None, 36)
		GO_img = font.render("game over", True, (240,230,140))
		font = pygame.font.SysFont(None, 24)
		
			
			
		GO=True
		while GO:#game over menu xd
			pygame.draw.rect(screen, black, pygame.Rect(0, 0, x_max, y_max))#clear window
			pressed = pygame.key.get_pressed()
			for event in pygame.event.get():  
				if event.type == pygame.QUIT or (pressed[pygame.K_q]): #quit window 
					done = True
					GO=False
			if  pressed[pygame.K_SPACE]: GO = False#start game
			re_img=font.render('round/max round: '+str(r)+'/'+str(rmax)+' to restart press "SPACE", difficulty: '+easytxt(easy), True, (240,230,140))
			screen.blit(re_img, (100, 3*y_max/4))
			screen.blit(GO_img, (100, 2*y_max/4))
			pygame.display.flip() 
			time.sleep(sleeptime*10)
			if ((pressed[pygame.K_UP] or pressed[pygame.K_w]) and easy<2): easy += 1  
			if ((pressed[pygame.K_DOWN] or pressed[pygame.K_s]) and easy>0): easy -= 1  
		pygame.draw.rect(screen, black, pygame.Rect(0, 0, x_max, y_max))#clear window
		size=min(x_max/8,y_max/8)
			
		r=0
		square=0
		t0 = time.time()
	

	#changing the position of the blue square
	if ((pressed[pygame.K_UP] or pressed[pygame.K_w]) and y>10+size): y -= 3  
	if ((pressed[pygame.K_DOWN] or pressed[pygame.K_s]) and y<(y_max-size-10)): y += 3  
	if ((pressed[pygame.K_LEFT] or pressed[pygame.K_a]) and x>10+size): x -= 3  
	if ((pressed[pygame.K_RIGHT] or pressed[pygame.K_d]) and x<(x_max-size-10)): x += 3  
	
	
	 
	if (2*size>=np.sqrt((x-px)*(x-px)+(y-py)*(y-py))):#if blue is on red square
		square +=1
		size=size-10# reduce squares 
		if size<10: #if squares are samall 
			r += 1# next round
			size=min(x_max/8,y_max/8)# start size
			if r>rmax:rmax=r
			wx=np.array(i)
			wy=np.array(i)
			w=np.array(i)
		if size<20:#random red square position but not all window
			px=random.uniform(250, x_max-x_max/4-250)
			py=random.uniform(250, y_max-y_max/4-250)
		else:#random red square position
			px=random.uniform(50, x_max-size-50)
			py=random.uniform(50, y_max-size-50)
	
	playtime=str(time.time() - t0)#chek time
	pt_max=playtime.find(".")#find "." in playtime sting 
	#text
	screen.blit(img, (0, 0))
	r_img = font.render('round/max round: '+str(r)+'/'+str(rmax)+", circle: "+str(square)+", time in game: "+playtime[:pt_max]+"s, lives:"+str(lives), True, (240,230,140))
	screen.blit(r_img, (0, y_max-24))
	#draw red nad blue square
	pygame.draw.circle(screen, red, (px, py), size)
	pygame.draw.circle(screen, blue, (x, y), size)
	#white square
	if  pressed[pygame.K_p]: 
		tp= time.time()
		pygame.draw.rect(screen, black, pygame.Rect(0, 0, x_max, y_max))#clear window
		re_img=font.render('pause', True, (240,230,140))
		screen.blit(re_img, (100, 2*y_max/4))
		pygame.display.flip() 
		pause = True#start game
		#time.sleep(1)
		
		
	while pause:
		#pygame.draw.rect(screen, black, pygame.Rect(0, 0, x_max, y_max))#clear window
		pressed = pygame.key.get_pressed()
		for event in pygame.event.get():  
			if event.type == pygame.QUIT or (pressed[pygame.K_q]): #quit window 
				done = True
				GO=False
		time.sleep(sleeptime*10)
		
		
		if  pressed[pygame.K_p]: 
			pause = False#start game
			t0=t0+time.time()-tp
	if (r%10)+1>10 and easy==1: 
		b=10
		sleep=2*sleeptime/(r/10+1)#time wait to next move
	elif easy==0: 
		b=0
		sleep=sleeptime/(1+4*r/10)
	elif easy==1 and not (r%10)+1>10:
		b=int(r%10)+1
		sleep=2*sleeptime/(r/10+1)#time wait to next move
	elif easy==2 and not (r%10)+1>10:
		b=int(r/10)+1
		sleep=2*sleeptime/(r%10+1)#time wait to next move
	elif easy==2 and (r%10)+1>10:
		b=10
		sleep=2*sleeptime/(r%10+1)#time wait to next move
	for a in range(0,b):
		if (wx[a]<-wsize[a] or wy[a]<-wsize[a] or wx[a]>x_max+wsize[a] or wy[a]>y_max+wsize[a]):#if out of skreen create new
			w[a], wx[a], wy[a], wsize[a], wspeed[a] = wsquare(min(x_max/8,y_max/8)/(b))
			print(str(wsize[a]))
		else: #change position
			wx[a], wy[a]=wsp(w[a],wx[a],wy[a],wspeed[a])
			
		
		pygame.draw.circle(screen, (255,255,255), (wx[a], wy[a]), wsize[a] )#pygame.draw.rect(screen, (255,255,255), pygame.Rect(wx[a], wy[a], wsize[a], wsize[a]))
		if(size+wsize[a]>=np.sqrt((x-wx[a])*(x-wx[a])+(y-wy[a])*(y-wy[a]))and lives>0):# and lives>0): 
			lives-=1
			wx=np.array(i)
			wy=np.array(i)
			w=np.array(i)
			print(str(wsize[1])+'    '+str(b)+"      "+str(min(x_max/8,y_max/8)/(b)))
		
		#game over
		elif(size+wsize[a]>=np.sqrt((x-wx[a])*(x-wx[a])+(y-wy[a])*(y-wy[a])) and lives==0):
			pygame.draw.rect(screen, black, pygame.Rect(0, 0, x_max, y_max))#clear window
			wx=np.array(i)
			wy=np.array(i)
			w=np.array(i)
			font = pygame.font.SysFont(None, 36)
			GO_img = font.render("game over", True, (240,230,140))
			font = pygame.font.SysFont(None, 24)
			screen.blit(GO_img, (100, 2*y_max/4))
			lives=3
			
			GO=True
			while GO:#game over menu xd
				pygame.draw.rect(screen, black, pygame.Rect(0, 0, x_max, y_max))#clear window
				pressed = pygame.key.get_pressed()
				for event in pygame.event.get():  
					if event.type == pygame.QUIT or (pressed[pygame.K_q]): #quit window 
						done = True
						GO=False
				if  pressed[pygame.K_SPACE]: GO = False#start game
				re_img=font.render('round/max round: '+str(r)+'/'+str(rmax)+', to restart press "SPACE", difficulty: '+easytxt(easy), True, (240,230,140))
				screen.blit(GO_img, (100, 2*y_max/4))
				screen.blit(re_img, (100, 3*y_max/4))
				pygame.display.flip() 
				time.sleep(sleeptime*10)
				if ((pressed[pygame.K_UP] or pressed[pygame.K_w]) and easy<2): easy += 1  
				if ((pressed[pygame.K_DOWN] or pressed[pygame.K_s]) and easy>0): easy -= 1 
			pygame.draw.rect(screen, black, pygame.Rect(0, 0, x_max, y_max))#clear window
			size=min(x_max/8,y_max/8)
			
			r=0
			square=0
			t0 = time.time()	
		
		
	
	time.sleep(sleep)#wait to next press
	#print(str(sleep))
	pygame.display.flip()  
print(str(int(1.9)))
