import pygame
import time
import random
pygame.init()
#music
start_music=pygame.mixer.music.load("start.mp3")
#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
blue=(0,0,255)
border=(255, 203, 170)
green=(0,255,0)

yello=(248, 124, 75)
#intial window
display_width=800
display_height=600
gameDisplay=pygame.display.set_mode((display_width,display_height))
gameDisplay.fill(white)
pygame.display.set_caption("Snack")
pygame.display.update()
clock=pygame.time.Clock()
#images
snakimg=pygame.image.load("snakhead.png")
start=pygame.image.load("start.jpg")
apple=pygame.image.load("Apple.jpg")
#block variables
block_size=20
FPS=20


direction="right"

def start_screen():
    pygame.mixer.music.load("start.mp3")
    pygame.mixer.music.play(5,0)
    global  FPS
    start=True
    while start:
        gameDisplay.fill(border)
        Message_to_screen("Hello Gamer!",red,-120,50)
        Message_to_screen("This is snack",green, -70, 30)
        Message_to_screen("You have to pass through whole to eat it", green, -50, 30)
        Message_to_screen("Enter Mode of Game:", blue, -20, 30)
        Message_to_screen("1.Easy",blue, 10, 30)
        Message_to_screen("2.Medium",blue, 40, 30)
        Message_to_screen("3.Hard",blue, 80, 30)

        pygame.display.update()
        clock.tick(15)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type==pygame.KEYDOWN:

                if event.key == pygame.K_1:
                    FPS=10
                    start = False
                if event.key == pygame.K_2:
                    FPS=30
                    start = False
                if event.key == pygame.K_3:
                    FPS=40
                    start = False
    pygame.mixer.music.stop()
def snack(block_size,snackList):
    if direction=="left":
        head=pygame.transform.rotate(snakimg,180)
    elif direction=="up":
        head=pygame.transform.rotate(snakimg,90)
    elif direction == "down":
        head = pygame.transform.rotate(snakimg, 270)
    elif direction == "right":
        head = snakimg

    gameDisplay.blit(head,(snackList[-1][0],snackList[-1][1]))
    for xny in snackList[:-1]:
        gameDisplay.fill(yello, rect=[xny[0],xny[1],block_size, block_size])

def Message_to_screen(msg,color,y_displace=0,size=25):

    font = pygame.font.SysFont("Georgia", size)
    screen_text=font.render(msg,True,color)
    screen_surface=screen_text.get_rect()
    screen_surface.center=(display_width/2),(display_height/2)+y_displace
    gameDisplay.blit(screen_text,screen_surface)

def main_loop():
    pygame.mixer.music.load("back.mp3")
    pygame.mixer.music.play(1, 0)
    gameExit=False
    global direction
    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_y_change = 0
    lead_x_change = 10

    gameOver = False
    Applesize=30
    snackList=[]
    snacklength=1
    #Apples variable
    randAppleX=round((random.randrange(0,display_width-block_size))/10.0)*10.0
    randAppleY=round((random.randrange(0,display_height-block_size))/10.0)*10.0

    while not gameExit:


        while not gameOver:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameOver=True
                    gameExit=True
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                       lead_x_change=block_size
                       lead_y_change=0
                       direction="right"
                    elif event.key==pygame.K_LEFT:
                        lead_x_change=-block_size
                        lead_y_change=0
                        direction="left"
                    elif event.key==pygame.K_UP:
                        lead_y_change=-block_size
                        lead_x_change=0
                        direction="up"
                    elif event.key==pygame.K_DOWN:
                         lead_y_change=block_size
                         lead_x_change=0
                         direqction="down"
            if lead_x >=display_width or lead_x <= 0 or lead_y >= display_height or lead_y<=0:
                gameOver = True

            lead_x+=lead_x_change
            lead_y+=lead_y_change

            gameDisplay.fill(white)
            gameDisplay.blit(apple,(randAppleX,randAppleY))

            snackHead=[]
            snackHead.append(lead_x)
            snackHead.append(lead_y)
            snackList.append(snackHead)
            if len(snackList)>snacklength:
                del snackList[0]
            snack( block_size,snackList)
            pygame.display.update()
            clock.tick(FPS)

            if lead_x>=randAppleX and lead_x<=randAppleX+Applesize or lead_x+block_size>=randAppleX and lead_x+block_size<=randAppleX+Applesize:
                if lead_y>=randAppleY and lead_y<=randAppleY+Applesize or lead_y+block_size>=randAppleY and lead_y+block_size<=randAppleY+Applesize:
                    randAppleX = round((random.randrange(0, display_width - block_size)) / 10.0) * 10.0
                    randAppleY = round((random.randrange(0, display_height - block_size)) / 10.0) * 10.0
                    snacklength += 1

        if gameOver==True:
            gameDisplay.fill(white)

            Message_to_screen("Oops You lose!Enter c for continue or q for quit",blue,0)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_c:
                        main_loop()
                    elif event.key==pygame.K_q or event.key==pygame.QUIT:
                        gameExit=True

start_screen()
main_loop()

pygame.quit()
quit()