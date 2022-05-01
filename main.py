import pygame,sys,random

from pygame.constants import SYSTEM_CURSOR_SIZEWE
pygame.init()

worldx = 900
worldy = 600

WHITE = (246,244,244)
BLACK = (0,0,0)
RED = (255,0,0)
GREY = (167,167,167)
GREEN = (0,150,0)

screen = pygame.display.set_mode((worldx,worldy))
pygame.display.set_caption("< DEATH >")
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT + 1, 10000)
gravity = 1
enemy_speed = 4
tick = 0

#fonts
pygame.font.init()
scorefont = pygame.font.SysFont('Arial Black', 20)
titlefont = pygame.font.SysFont('Consolas', 40)
quitfont = pygame.font.SysFont('Consolas', 30)
gqfont = pygame.font.SysFont('Consolas', 20)
gamefont = pygame.font.SysFont('Lucida Console',120)
creditfont = pygame.font.SysFont('Consolas',20)
hsfont = pygame.font.SysFont('Consolas', 80)

#load horses
h2 = pygame.image.load("img/horse2.png")
h3 = pygame.image.load("img/horse3.png")
h4 = pygame.image.load("img/horse4.png")
h5 = pygame.image.load("img/horse5.png")
h6 = pygame.image.load("img/horse6.png")
h7 = pygame.image.load("img/horse7.png")
h8 = pygame.image.load("img/horse8.png")
horselist = [h2,h3,h4,h5,h6,h7,h8]

#load_skulls
skull_w = pygame.transform.scale(pygame.image.load("img/skull(w).png"),(20,30))
skull_b = pygame.transform.scale(pygame.image.load('img/skull(b).png'),(20,30))
skull60 = pygame.transform.scale(pygame.image.load('img/skull60.png'),(18,28))
skull40 = pygame.transform.scale(pygame.image.load('img/skull40.png'),(16,26))
skull20 = pygame.transform.scale(pygame.image.load('img/skull20.png'),(14,24))
skull5 = pygame.transform.scale(pygame.image.load('img/skull5.png'),(12,22))
skulls = [skull_w,skull_b,skull60,skull40,skull20,skull5]

#load_firework
fw5 = pygame.image.load("img/fw5.png")

#load character animation
players = []
def character_load():
    for i in range(10):
        img = pygame.transform.scale(pygame.image.load('img/player'+str(i)+'.png'),(18,37))
        players.append(img)
	
character_load()

class Highscore():
    def __init__(self):
        hisc=open("txt/highscore.txt","r")
        j = hisc.read()
        self.val = int(j)

    def setval(self,score):
        hisc=open("txt/highscore.txt","w")
        hisc.write(str(score))
        hisc.close()

        #highscore animation
        fireworks = True
        screen.fill(BLACK)
        cgrect,cgsurf = title_text(WHITE,(worldx/2,worldy/2),"CONGRATULATIONS",hsfont)
        chrect,chsurf = title_text(WHITE,(worldx/2,(worldy/2)-100),"NEW HIGHSCORE",titlefont)
        screct,scsurf = title_text(WHITE,(worldx/2,(worldy/2)+100),str(score),hsfont)
        screen.blit(cgsurf,cgrect)
        screen.blit(chsurf,chrect)
        screen.blit(scsurf,screct)
        pygame.display.update()
        fwind = 0
        while fwind < 30:
            ogx = random.randint(0,worldx-80)
            ogy = random.randint(0,worldy-85)
            sze = random.randint(60,120)
            fw = pygame.transform.scale(fw5,(sze,sze-10))
            screen.blit(fw,(ogx,ogy))
            pygame.display.update()
            pygame.time.wait(100)
            if fwind == 29:
                pygame.time.wait(3000)
                fwind += 1
            else:
                fwind += 1

def pause(h,sc):
    pygame.draw.rect(screen, WHITE,(((worldx/2)-200,(worldy/2)-125),(400,250)))
    brect,bsurf = title_text(BLACK,(worldx/2,worldy/2),'back to game',h)
    screen.blit(bsurf,brect)
    Qrect,Qsurf = title_text(BLACK, ((worldx/2)+150,((worldy/2)+100)),'quit',creditfont)
    screen.blit(Qsurf,Qrect)
    FSrect,FSsurf = title_text(WHITE,(worldx/2, (worldy/2)+200), 'Current Score = '+str(sc),quitfont)
    screen.blit(FSsurf,FSrect)
    pygame.display.update()
    bcount = 0
    Qcount = 0
    block = True
    while block:
        clock.tick(5)
        x,y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if brect.collidepoint(x,y):
                    block = False
                if Qrect.collidepoint(x,y):
                    pygame.quit()
                    quit()
        if brect.collidepoint(x,y) and bcount == 0:
            brect,bsurf = title_text(GREY,(worldx/2,worldy/2),'back to game',h)
            pygame.draw.rect(screen, WHITE,(((worldx/2)-200,(worldy/2)-125),(400,250)))
            screen.blit(Qsurf,Qrect)
            screen.blit(bsurf,brect)
            bcount = 1
            pygame.display.update()
        elif not brect.collidepoint(x,y) and bcount == 1:
            brect,bsurf = title_text(BLACK,(worldx/2,worldy/2),'back to game',h)
            pygame.draw.rect(screen, WHITE,(((worldx/2)-200,(worldy/2)-125),(400,250)))
            screen.blit(Qsurf,Qrect)
            screen.blit(bsurf,brect)
            bcount = 0
            pygame.display.update()
        elif Qrect.collidepoint(x,y) and Qcount == 0:
            Qrect,Qsurf = title_text(GREY,((worldx/2)+150,((worldy/2)+100)),'quit',creditfont)
            pygame.draw.rect(screen, WHITE,(((worldx/2)-200,(worldy/2)-125),(400,250)))
            screen.blit(Qsurf,Qrect)
            screen.blit(bsurf,brect)
            Qcount = 1
            pygame.display.update()
        elif not Qrect.collidepoint(x,y) and Qcount == 1:
            Qrect,Qsurf = title_text(BLACK,((worldx/2)+150,((worldy/2)+100)),'quit',creditfont)
            pygame.draw.rect(screen, WHITE,(((worldx/2)-200,(worldy/2)-125),(400,250)))
            screen.blit(Qsurf,Qrect)
            screen.blit(bsurf,brect)
            Qcount = 0
            pygame.display.update()

def write_score(a):
    a = '+'+str(a)
    textsurface = scorefont.render(a, False, WHITE)
    screen.blit(textsurface,(649-(len(a)*10),14))

def title_text(color,loc,text,font):
    text_surface = font.render(text,True,color)
    text_rect = text_surface.get_rect()
    text_rect.center = (loc)
    return text_rect,text_surface

def credits(j):
    screen.fill(BLACK)
    arect,asurf = title_text(WHITE,(worldx/2,worldy/2),'a3n9d3r4e5w',j)
    screen.blit(asurf,arect)
    pygame.display.update()
    acount = 0
    lock = True
    while lock: 
        clock.tick(10)
        x,y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if arect.collidepoint(x,y):
                    lock = False
        if arect.collidepoint(x,y) and acount == 0:
            arect,asurf = title_text(GREY,(worldx/2,worldy/2),'a3n9d3r4e5w',j)
            screen.fill(BLACK)
            screen.blit(asurf,arect)
            acount = 1
            pygame.display.update()
        elif not arect.collidepoint(x,y) and acount == 1:
            arect,asurf = title_text(WHITE,(worldx/2,worldy/2),'a3n9d3r4e5w',j)
            screen.fill(BLACK)
            screen.blit(asurf,arect)
            acount = 0
            pygame.diplay.update()

def start_menu():
    intro = True
    #print(str(highscore()))
    hirect,hisurf = title_text(WHITE,(((worldx/15)*2,(worldy/10))),"highscore : "+str(highscore.val),creditfont)
    screen.blit(hisurf,hirect)
    Trect,Tsurf = title_text(WHITE,(worldx/2,(worldy/2)-50),'Start Game',titlefont)
    screen.blit(Tsurf,Trect)
    Qrect,Qsurf = title_text(WHITE, (worldx/2,(worldy/2)),'Quit',quitfont)
    screen.blit(Qsurf,Qrect)
    Crect,Csurf = title_text(WHITE,((worldx/6)*5,(worldy/6)*5),'Credits',creditfont)
    screen.blit(Csurf,Crect)
    pygame.display.update()
    Tcount = 0
    Qcount = 0
    Ccount = 0
    while intro:
        clock.tick(10)
        x,y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if Trect.collidepoint(x,y):
                    intro = False
                elif Qrect.collidepoint(x,y):
                    pygame.quit()
                    quit()
                elif Crect.collidepoint(x,y):
                    credits(creditfont)

        if Trect.collidepoint(x,y) and Tcount == 0:
            Trect,Tsurf = title_text(GREY,(worldx/2,(worldy/2)-50),'Start Game',titlefont)
            screen.fill(BLACK)
            screen.blit(hisurf,hirect)
            screen.blit(Tsurf,Trect)
            screen.blit(Qsurf,Qrect)
            screen.blit(Csurf,Crect)
            Tcount = 1
        elif not Trect.collidepoint(x,y) and Tcount == 1:
            Trect,Tsurf = title_text(WHITE,(worldx/2,(worldy/2)-50),'Start Game',titlefont)
            screen.fill(BLACK)
            screen.blit(hisurf,hirect)
            screen.blit(Tsurf,Trect)
            screen.blit(Qsurf,Qrect)
            screen.blit(Csurf,Crect)
            Tcount = 0
        elif Qrect.collidepoint(x,y) and Qcount == 0:
            Qrect,Qsurf = title_text(GREY,(worldx/2,(worldy/2)),'Quit',quitfont)
            screen.fill(BLACK)
            screen.blit(hisurf,hirect)
            screen.blit(Qsurf,Qrect)
            screen.blit(Tsurf,Trect)
            screen.blit(Csurf,Crect)
            Qcount = 1
        elif not Qrect.collidepoint(x,y) and Qcount == 1:
            Qrect,Qsurf = title_text(WHITE,(worldx/2,(worldy/2)),'Quit',quitfont)
            screen.fill(BLACK)
            screen.blit(hisurf,hirect)
            screen.blit(Qsurf,Qrect)
            screen.blit(Tsurf,Trect)
            screen.blit(Csurf,Crect)
            Qcount = 0
        elif Crect.collidepoint(x,y) and Ccount == 0:
            Crect,Csurf = title_text(GREY,((worldx/6)*5,(worldy/6)*5),'Credits',creditfont)
            screen.fill(BLACK)
            screen.blit(hisurf,hirect)
            screen.blit(Qsurf,Qrect)
            screen.blit(Tsurf,Trect)
            screen.blit(Csurf,Crect)
            Ccount = 1
        elif not Crect.collidepoint(x,y) and Ccount == 1:
            Crect,Csurf = title_text(WHITE,((worldx/6)*5,(worldy/6)*5),'Credits',creditfont)
            screen.fill(BLACK)
            screen.blit(hisurf,hirect)
            screen.blit(Qsurf,Qrect)
            screen.blit(Tsurf,Trect)
            screen.blit(Csurf,Crect)
            Ccount = 0
            
        pygame.display.update()

def game_over(x):
    outro = True
    screen.fill(BLACK)
    Rrect,Rsurf = title_text(WHITE,(worldx/2,(worldy/2)+50),'Restart',quitfont)
    screen.blit(Rsurf,Rrect)
    Qrect,Qsurf = title_text(WHITE, (worldx/2,(worldy/2)+100),'Quit',gqfont)
    screen.blit(Qsurf,Qrect)
    Grect,Gsurf = title_text(WHITE,(worldx/2,(worldy/2)-100),'Game Over',gamefont)
    screen.blit(Gsurf,Grect)
    FSrect,FSsurf = title_text(WHITE,(worldx/2, (worldy/2)+200), 'Final Score = '+str(x),quitfont)
    screen.blit(FSsurf,FSrect)
    pygame.display.update()
    Rcount = 0
    Qcount = 0
    while outro:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if Rrect.collidepoint(x,y):
                    player.lives = 3
                    coin.count = 0
                    enemy.x_speed = 2
                    spears.y_speed = -2
                    game_loop(tick)
                if Qrect.collidepoint(x,y):
                    pygame.quit()
                    quit()

        x,y = pygame.mouse.get_pos()
        if Rrect.collidepoint(x,y) and Rcount == 0:
            Rrect,Rsurf = title_text(GREY,(worldx/2,(worldy/2)+50),'Restart',quitfont)
            screen.fill(BLACK)
            screen.blit(Gsurf,Grect)
            screen.blit(Rsurf,Rrect)
            screen.blit(Qsurf,Qrect)
            screen.blit(FSsurf,FSrect)
            Rcount = 1
        elif not Rrect.collidepoint(x,y) and Rcount == 1:
            Rrect,Rsurf = title_text(WHITE,(worldx/2,(worldy/2)+50),'Restart',quitfont)
            screen.fill(BLACK)
            screen.blit(Gsurf,Grect)
            screen.blit(Rsurf,Rrect)
            screen.blit(Qsurf,Qrect)
            screen.blit(FSsurf,FSrect)
            Rcount = 0
        elif Qrect.collidepoint(x,y) and Qcount == 0:
            Qrect,Qsurf = title_text(GREY, (worldx/2,(worldy/2)+100),'Quit',gqfont)
            screen.fill(BLACK)
            screen.blit(Gsurf,Grect)
            screen.blit(Qsurf,Qrect)
            screen.blit(Rsurf,Rrect)
            screen.blit(FSsurf,FSrect)
            Qcount = 1
        elif not Qrect.collidepoint(x,y) and Qcount == 1:
            Qrect,Qsurf = title_text(WHITE, (worldx/2,(worldy/2)+100),'Quit',gqfont)
            screen.fill(BLACK)
            screen.blit(Gsurf,Grect)
            screen.blit(Qsurf,Qrect)
            screen.blit(Rsurf,Rrect)
            screen.blit(FSsurf,FSrect)
            Qcount = 0
        pygame.display.update()

class Platform():
    def __init__(self,sizex,sizey,posx,posy):
        self.surf = pygame.surface.Surface((sizex,sizey))
        self.rect = self.surf.get_rect(midbottom=(posx,posy))
        self.px = posx
        self.py = posy
        self.sx = sizex
        self.sy = sizey
        self.brick = pygame.image.load("img/brick.png")
    def draw(self):
        #pygame.draw.rect(screen, self.colour, ((self.pos),(self.dimensions)))
        for i in range(self.sx//30):
            screen.blit(self.brick,(self.px - (self.sx/2)+i*30,(self.py - self.sy)))

class Player():
    def __init__(self):
        self.jump = False
        self.left = False
        self.right = False
        self.lives = 3
        self.status = 'alive'
        self.index = 0
        self.heart = pygame.transform.scale(pygame.image.load('img/heart.png'),(20,20))
        self.surf = players[self.index]
        self.rect = self.surf.get_rect(midbottom=(worldx//2,worldy-100))
        self.y_speed = 0
        self.orient = 'right'
        self.land = False
        self.track = False
        self.jump_delay = 10
        self.velocity = 4
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE or event.key == pygame.K_UP) and self.on_ground():
                    self.jump = True
                    self.track = True
                elif event.type == pygame.USEREVENT + 1:
                    enemy.timer = True
                elif event.key == pygame.K_ESCAPE:
                    pause(creditfont,coin.count)
        self.left = False
        self.right = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.left = True
        if keys[pygame.K_RIGHT]:
            self.right = True
            
    def move(self):
        if self.right == False and self.left == False:
            self.index = 0
        if self.right == True and self.left == True:
            self.index = 0
        if self.jump:
            self.y_speed = -14
            self.jump = False
        self.rect.bottom += self.y_speed
	        
        if self.left and self.rect.left > 0:
            self.rect.centerx -= self.velocity
            self.orient = 'left'
            if self.index< 8 and self.index >= 2:
                self.index += 1
            else:
                self.index = 2

        if self.right and self.rect.right > 0:
            self.rect.centerx += self.velocity
            self.orient = 'right'
            if self.index<8 and self.index >= 2:
                self.index += 1
            else:
                self.index = 2
		
        if self.rect.centerx <= 5:
            self.rect.centerx = 5
        if self.rect.centerx >= 885:
            self.rect.centerx = 885
            
        if self.on_ground():
            if self.track == True:
                self.land = True
                self.track = False
            if self.y_speed >= 0:
                self.rect.bottom = p_rects[self.rect.collidelist(p_rects)].top + 1
                self.y_speed = 0
            else:
                self.rect.top = p_rects[self.rect.collidelist(p_rects)].bottom
                self.y_speed = 1
        else:
            self.y_speed += gravity
            self.index = 0
    
    def on_ground(self):
        collision = self.rect.collidelist(p_rects)
        if collision > -1:
            return True
        else: 
            return False
    
    def draw(self):
        if self.land == True:
            if self.jump_delay > 0:
                self.jump_delay -= 1
                self.index = 1
            if self.jump_delay == 0:
                self.land = False
                self.jump_delay = 10
        self.surf = players[self.index]
        if self.orient == 'left':
            self.surf = pygame.transform.flip(self.surf,True,False)
        screen.blit(self.surf,self.rect)
        for i in range(self.lives):
            screen.blit(self.heart,[i*20+20,20])

class Enemy():
    
    def __init__(self):
        self.count = 0
        self.surf = pygame.transform.scale(pygame.image.load('img/horse1.png'),(50,50))
        self.anime = 1
        self.orient = 'right'
        self.rect = self.surf.get_rect(midtop=(worldx//2,0))
        self.x_speed = 2
        self.y_speed = 0
        self.timer = False
        self.count = 0
        self.Hz = 4
        
    def move(self):
        self.count += 1
        self.surf = pygame.transform.scale((horselist[self.anime]),(50,50))
        if self.anime < 6 and self.count% self.Hz == 0:
            self.anime += 1
            self.Hz = random.randint(3,5)
        elif self.anime == 6 and self.count% self.Hz == 0:
            self.anime = 0
            self.Hz = random.randint(3,5)
            
        if self.rect.left <= 0 and self.orient=="left":
            self.x_speed *= -1
            self.orient = 'right'
        if self.rect.right >= worldx:
            self.x_speed *= -1
            self.orient = 'left'
        elif self.rect.right < worldx and self.rect.left > 0 and self.orient == 'left' and self.x_speed>0:
            self.x_speed *= -1
        elif self.rect.right < worldx and self.rect.left > 0 and self.orient == 'right' and self.x_speed <0:
            self.x_speed *= -1
        self.rect.centerx += self.x_speed
        enemy.orientation()
        
        if self.on_ground():
            self.rect.bottom = p_rects[self.rect.collidelist(p_rects)].top + 1
            self.y_speed = 0
        else:
            self.y_speed += gravity
        self.rect.bottom += self.y_speed
        self.hit()
        if self.timer:
            self.timer = False
            self.rect.midtop = (worldx//2,0)
            self.x_speed = (16)*((self.x_speed > 0) - (self.x_speed <0))

    def on_ground(self):
        collision = self.rect.collidelist(p_rects)
        if collision > -1:
            return True
        else:
            return False
    
    def orientation(self):
        if self.orient == 'left':
            self.surf = pygame.transform.flip(self.surf,True,False)
            
    def hit(self):
        if player.rect.colliderect(self.rect):
            player.status = 'dead'
            player.lives -= 1
            player.rect.midbottom = (worldx//2,worldy-202)
            self.rect = self.surf.get_rect(midtop=(worldx//2,0))
    
    def draw(self):
        screen.blit(self.surf,self.rect)
    
    def difficulty(self):
        if self.orient == 'left':
            self.x_speed -=0.5
        elif self.orient == 'right':
            self.x_speed +=0.5

class Vertical_Enemies():
    def __init__(self):
        self.start_pos = [(3*worldx/4,worldy),(worldx/4,worldy),(worldx/2,worldy),(worldx/5,worldy),(2*worldx/5,worldy),
                            (3*worldx/5,worldy),(4*worldx/5,worldy),(20,worldy),(worldx-20,worldy)]
        self.surf = skull_w
        self.rect = self.surf.get_rect(midbottom=random.choice(self.start_pos))
        self.x_speed = 0
        self.y_speed = -2
        self.shots = 0
        self.dist = 0
        self.warning = 0.4
    
    def move(self):
        if self.rect.centery < 500:
            self.rect.centery += self.y_speed
        if self.rect.centery < 500:
            self.rect.centery += self.warning

        if self.rect.bottom >= 0:
            self.rect.bottom += self.y_speed
        else:
            self.shots += 1
            self.chc = random.choice([2,3,4])
            if self.shots%self.chc == 0:
                self.rect= self.surf.get_rect(midbottom = (player.rect.centerx+(random.randint(-20,20)),worldy))
                self.shots = 0
                #print(self.shots)
            else:
                self.rect = self.surf.get_rect(midbottom=random.choice(self.start_pos))
            
    def hit(self):
        if player.rect.colliderect(self.rect):
            player.status = 'dead'
            self.shots += 1
            player.lives -= 1
            player.rect.midbottom = (worldx//2,worldy-202)
            self.rect = self.surf.get_rect(midbottom=random.choice(self.start_pos))
            
    def draw(self):
        if self.rect.centery < 500:
            self.surf = skulls[0]
            if 500 - self.rect.bottom > 50:
                self.dist = (500 - self.rect.bottom)/30
                if self.dist >= 1:
                    screen.blit(skulls[2],(self.rect.centerx - 9,self.rect.centery + 6))
                if self.dist >= 2:
                    screen.blit(skulls[3],(self.rect.centerx - 8,self.rect.centery + 26))
                if self.dist >= 3:
                    screen.blit(skulls[4],(self.rect.centerx - 7,self.rect.centery + 46))
                if self.dist >= 4:
                    screen.blit(skulls[5],(self.rect.centerx - 6,self.rect.centery + 66))
        else:
            self.surf = skulls[1]
        screen.blit(self.surf,self.rect)

    def difficulty(self):
        self.y_speed -=0.5

class Fire_Animation():
    def __init__(self):
        self.surf = pygame.transform.scale(pygame.image.load('img/fl1.png'),(30,60))
        self.rect = self.surf.get_rect(bottom = worldy)
        self.flamesqt = 12
        self.anime = random.randint(0,self.flamesqt)
        self.framepause = 16
        self.tick = 0
    
    def draw(self):
        self.surf = pygame.transform.scale(pygame.image.load('img/fl'+str(self.anime)+'.png'),(30,60))
        for i in range(worldx//15):
            screen.blit(self.surf,(((-7)+i*15),540,30,60))
        self.tick+=1
        if (self.tick/self.framepause).is_integer():
            if self.anime == self.flamesqt:
                self.anime = 0
            else:
                self.anime += 1

class Coin():
    def __init__(self):
        self.positions = [(155,160),(590, 240), (250, 320), (40, 500), (850, 500),(830, 240),
                            (800, 320),(525,80),(250,500),(690,500),(490,240)]
        self.surf = pygame.transform.scale(pygame.image.load('img/baddge1.png'),(30,30))
        self.rect = self.surf.get_rect(midbottom=random.choice(self.positions))
        self.count = 0
        self.small_surf = pygame.transform.scale(self.surf,(20,20))
        self.anime = 1
        self.con = 1
        self.prect,self.psurf = title_text(BLACK,((worldx/10)*9,(worldy/25)*24),'ESC = PAUSE',creditfont)

    def hit(self):
        if player.rect.colliderect(self.rect):
            n_pos = random.choice(self.positions)
            if n_pos != self.rect.midbottom:
                self.rect.midbottom = n_pos
            else:
                while n_pos == self.rect.midbottom:
                    n_pos = random.choice(self.positions)
                self.rect.midbottom = n_pos
            self.count += 1
            if self.count//2 == 0:
                pass
        
    def draw(self):
        self.surf = pygame.transform.scale(pygame.image.load('img/baddge'+str(self.anime)+'.png'),(30,30))
        screen.blit(self.surf,self.rect)
        self.con += 1
        if self.anime < 4 and self.con%6 == 0:
            self.anime += 1
        elif self.anime == 4 and self.con%6 == 0:
            self.anime = 1
        
        if self.count < 11:
            for i in range(self.count):
                screen.blit(self.small_surf,[850-i*21,20])
        else:
            for i in range(10):
                screen.blit(self.small_surf,[850-i*21,20])
            write_score(self.count)
        screen.blit(self.psurf,self.prect)

platforms = []
platforms.append(Platform(worldx, 100, worldx//2, worldy))
platforms.append(Platform(210, 20, 500, worldy-180))
platforms.append(Platform(300, 20, 200, 340))
platforms.append(Platform(240, 20, 480, 260))
platforms.append(Platform(300, 20, 150, 180))
platforms.append(Platform(300, 20, 500, 100))
platforms.append(Platform(90, 20, 830, 260))
platforms.append(Platform(150, 20, 750, 340))
p_rects = [p.rect for p in platforms]

player = Player()
enemy = Enemy()
coin = Coin()
spears = Vertical_Enemies()
flames = Fire_Animation()
highscore = Highscore()
tick = 0

def game_loop(tick):
    while True:
        if player.status == 'dead':
            player.index = 0
            enemy.rect = enemy.surf.get_rect(midtop=(worldx//2,0))
            enemy.orient = random.choice(["left","right"])
            enemy.orientation()
            pygame.time.wait(200)
            player.status = 'alive'
        
        clock.tick(60)
        screen.fill(BLACK)
        flames.draw()
        player.events()
        player.move()
        enemy.move()
        spears.move()
        coin.hit()
        spears.hit()

        player.draw()
        enemy.draw()
        
        for p in platforms:
            p.draw()
        spears.draw()
        
        coin.draw()
        
        if player.lives == 0:
            if highscore.val < coin.count:
                highscore.setval(coin.count)
            game_over(coin.count)

        if (coin.count/6).is_integer() and abs(spears.y_speed) < 6 and (coin.count - 6) == tick:
            tick = coin.count
            spears.difficulty()
            enemy.difficulty()
        elif (coin.count/6).is_integer() and abs(spears.y_speed) == 6 and (coin.count - 6) == tick and abs(enemy_speed) < 8:
            enemy.difficulty()
            tick = coin.count
        
        pygame.display.update()

start_menu()
game_loop(tick)